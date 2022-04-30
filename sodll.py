import ctypes
import os
import sys
import subprocess
import json
from hierarchy import *

HERE = os.path.dirname(os.path.realpath(__file__))

c2ctypes = {
	"_Bool"  : "c_bool",
	"char"   : "c_char",
	"wchar_t": "c_wchar",
	"char"   : "c_byte",
	"unsigned char": "c_ubyte",
	"short"  : "c_short",
	"unsigned short": "c_ushort",
	"int"    : "c_int",
	"unsigned int"    : "c_uint",
	"long long"    : "c_longlong",
	"long"    : "c_long",
	"unsigned long"    : "c_ulong",
	"__int64"    : "c_longlong",
	"unsigned __int64"    : "c_ulonglong",
	"unsigned long long"  : "c_ulonglong",
	"size_t"  : "c_size_t",
	"ssize_t"  : "c_ssize_t",
	"Py_ssize_t"  : "c_ssize_t",
	"float"  : "c_float",
	"double"  : "c_double",
	"long double"  : "c_longdouble",
	"char*"  : "c_char_p", #(NUL terminated)",
	"wchar_t*"  : "c_wchar_p", #(NUL terminated)
	"void*"     : "c_void_p"
}

# the c field definition comes in (from header file)
# the proper ctype goes out
def getCtypeFromString(cstring):
	if cstring in c2ctypes.keys():
		return c2ctypes[cstring]
	else:
		for cstr, ctype in c2ctypes.items():
			if cstring.startswith(cstr):
				base = c2ctypes[cstr]
				remainder = cstring.replace(cstr, "")
				try:
					l = eval(remainder)
					if type(l) == list: # ex [2]
						return base + "*" + str(l[0])
				except:
					die
				break
		die

def sodllGenerate(dynamicLibraryFilenameIn, clangDictIn, libnameOut):
	clangDictIn = hierarchize("headers", clangDictIn)
	loadSoDLLString = """
from ctypes import *
OUTLIBNAMELib = CDLL("LIBRARY") 

def cdataStr(instr):
    return ffi.new(\"char[]\", instr.encode('ascii'))
	
# Generate Constants (ex VK_ACCELERATION_STRUCTURE_BUILD_TYPE_DEVICE_KHR)
"""
	print("making replacements")
	loadSoDLLString = loadSoDLLString.replace("LIBRARY", dynamicLibraryFilenameIn )
	loadSoDLLString = loadSoDLLString.replace("OUTLIBNAME", libnameOut )
	
	alias2real = {}
	
	allClasses   = ""
	allFunctions = ""
	# everything goes into inner
	for k, v in clangDictIn["inner"].items():
		if k == "descriptor":
			continue
		if v["kind"] == "FunctionDecl":
			fdict = v["inner"]
			argstring = ""
			convertstring = ""
			for l, w in fdict.items():
				if l == "descriptor":
					continue
				else:
					argstring += ", " + l
					argtype = w["type"]["qualType"]
					convertstring += "    " + l + " = " + argtype + "(" + l + ")\n"
			argstring = argstring[2:]
			fnstring  = "def " + k + "(" + argstring + "):\n"
			fnstring += convertstring
			fnstring += "    " + libnameOut + "Lib." + k + "(" + argstring + ")\n"
			
			allFunctions += fnstring
			#print(json.dumps(fdict, indent=2))
			
		elif v["kind"] == "TypedefDecl":
			print("TypedefDecl : " + k)
			alias2real[k] = v['inner']['inner']['type']['qualType']
		elif v["kind"] == "RecordDecl":
			# ig these are structs
			print("RecordDecl : " + k)
			
			# no inner is a placeholder struct?
			if "inner" not in v.keys():
				continue
			
			classstring  = "class NAME(Structure):\n".replace("NAME", k)
			classstring += "    _fields_ = [\n"
			#print(json.dumps(v["inner"], indent=2))
			for k, v in v["inner"].items():
				ctype = getCtypeFromString(v["type"]["qualType"])
				#print(k)
				classstring += "             (\"K\", V),\n".replace("K", k).replace("V",ctype)
			classstring = classstring[:-2]+"\n    ]\n"
			allClasses += classstring
			
		elif v["kind"] == "VarDecl":
			print("VarDecl : " + k)
		else:
			print(k)
			print(v["kind"])
			die
			
	loadSoDLLString += allClasses
	loadSoDLLString += allFunctions
	with open(libnameOut + ".py", 'w+') as f:
		f.write(loadSoDLLString)
	
	