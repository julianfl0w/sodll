import ctypes
import os
import sys
import subprocess
import json
from hierarchy import *

import logging
logger = logging.getLogger('dtfm')
logger.setLevel(0)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('{%(filename)s:%(lineno)d %(message)s}')
handler.setFormatter(formatter)
logger.addHandler(handler)

HERE = os.path.dirname(os.path.realpath(__file__))

# Pythons stupid scope rules dictate this bs
class Sodll:
	def __init__(self, dllFilename, soFilename, clangDictIn, libnameOut):
		self.conversions = {}
		self.alias2real = {}
		self.voidtypes = {}
		self.allStructs = []
		
		self.c2ctypes = {
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
			"char *"  : "c_char_p", #(NUL terminated)",
			"wchar_t*"  : "c_wchar_p", #(NUL terminated)
			"void*"     : "c_void_p",
			"void **"    : "POINTER(c_void_p)",
			"void *"     : "c_void_p"
		}
		
		self.generate(dllFilename, soFilename, clangDictIn, libnameOut)
	
	# the c field definition comes in (from header file)
	# the proper ctype goes out
	def getCtypeFromString(self, cstring, isClassDef = True):
		
		logger.debug(cstring)
		
		instring = cstring
		logger.debug("finding equivalent for " + cstring)

		# preformatting
		csarray = cstring.split("[")
		dims = []
		multiplier = 1
		for i in range(1, len(csarray)):
			thisDim = int(csarray[1].split("]")[0])
			dims += [thisDim]
			multiplier *= thisDim

		basetypes = {}
		remainder = csarray[0]
		# reduction loop
		dereferentiation = 0
		lastRem = ""
		while len(remainder):
			#print("rem " + remainder)
			if remainder == lastRem:
				basetypes[remainder] = dereferentiation
				break
				
			lastRem = remainder
			remainder = remainder.strip() # strip out whitespace
			
			# remove const, union, struct qualifiers
			for s in ["const ", "struct ", "union "]:
				if remainder.startswith(s):
					remainder = remainder[len(s):]
					
			#idgaf
			remainder = remainder.replace("*const ", "*")
			
			if remainder in self.alias2real.keys():
				remainder = self.alias2real[remainder]
					
			if remainder in self.c2ctypes.keys():
				basetypes[self.c2ctypes[remainder]] = dereferentiation
				break

			# (*) is the hallmark of a function pointer
			if "(*)" in remainder:
				basetypes["c_void_p"] = 0
				break
				
			# remove pointer indicator
			while remainder.endswith("*"):
				remainder = remainder[:-2]
				dereferentiation += 1

			# we are treating enums as integers
			if remainder.startswith("enum"):
				basetypes["c_int"] = 0
				break
				
			if remainder in self.allStructs:
				basetypes[remainder] = dereferentiation
				break
				
		#if "uint8_t" in basetypes.keys():
		#	die
		
		# expansion loop
		# dereference appropriately
		outtype = ""
		for t, d in basetypes.items():
			
			# remove const, union, struct qualifiers
			for s in ["const ", "struct ", "union "]:
				if t.startswith(s):
					t = t[len(s):]
					
			outtype = t
			if not isClassDef:
				outtype += "()"
			# IDGAFOS. VOIDS EVERYWHERE
			if t in self.voidtypes.keys():
				dereferentiation = max(0, d-1)

			# ctypes treats structs as pointers already
			if t in self.allStructs:
				dereferentiation = max(0, d-1)
			
			for i in range(dereferentiation):
				if isClassDef:
					outtype = "POINTER(" + outtype + ")"
				else:
					outtype = "pointer(" + outtype + ")"

			if dims != []:
				outtype += " *" + str(multiplier)
		
		if not isClassDef:
			self.conversions[instring] = outtype
		return outtype


	def dict2ClassString(self, name, fieldlist):
		namestring   = "class JNAME(Structure):\n".replace("JNAME", name)
		initstring   = "    def __init__(self, indict):\n"
		classstring  = "JNAME._fields_ = [\n".replace("JNAME", name)
		logger.debug(name)
		logger.debug(json.dumps(fieldlist, indent=2))
		for v in fieldlist:
			try:
				desugaredType = v["type"]["desugaredQualType"]
			except:
				desugaredType = v["type"]["qualType"]
			logger.debug(desugaredType)
			ctype = self.getCtypeFromString(desugaredType)
			#logger.debug(k)
			classstring += "    (\"JKEY\", JVALUE),\n".replace("JKEY", v["name"]).replace("JVALUE",ctype)
			initstring  += "        modval = preprocess(indict.get(\"JKEY\"))\n".replace("JKEY", v["name"])
			initstring  += "        if \"cast\" in indict.keys(): \n"
			initstring  += "            try: \n"
			initstring  += "                modval = cast(modval, type(self.JKEY))\n".replace("JKEY", v["name"])
			initstring  += "            except: \n"
			initstring  += "                pass\n"
			initstring  += "        self.JKEY = modval\n"
		classstring = classstring[:-2]+"\n    ]\n\n"

		return namestring + initstring + classstring

	def generate(self, dllFilename, soFilename, clangDictIn, libnameOut, vulkan=True):
		loadSoDLLString = """
from enum import Enum
from ctypes import *
import platform

if "nt" in platform.platform().lower() or "win" in platform.platform().lower() :
	OUTLIBNAMELib = CDLL('JDLL') 
else:
	OUTLIBNAMELib = CDLL('JSO') 
	
def array2ctype(inarray):
	return (type(inarray[0]) * len(inarray))(*inarray)

def ctype2array(inctype):
	return inctype[:]

def preprocess(indict):
	if type(indict) is dict:
		for k, v in indict.items():
			indict[k] = preprocess(v)
	elif type(indict) is list:
		if type(indict[0]) is list or type(indict[0]) is dict:
			for i, e in enumerate(indict):
				indict[i] = preprocess(e)
		else:
			indict = array2ctype(indict)
	else:
		pass
	return indict 
	
# Generate Constants (ex VK_ACCELERATION_STRUCTURE_BUILD_TYPE_DEVICE_KHR)
"""
		logger.debug("making replacements")
		loadSoDLLString = loadSoDLLString.replace("JDLL", dllFilename )
		loadSoDLLString = loadSoDLLString.replace("JSO", soFilename )
		loadSoDLLString = loadSoDLLString.replace("OUTLIBNAME", libnameOut )


		allClasses   = ""
		allFunctions = ""
		allTypeDecl  = ""
		allEnum      = ""
		allVar       = ""


		ALLOCATE_PREFIX = ('vkCreate', 'vkGet', 'vkEnumerate', 'vkAllocate',
											 'vkMap', 'vkAcquire')
		ALLOCATE_EXCEPTION = ('vkGetFenceStatus', 'vkGetEventStatus',
													'vkGetQueryPoolResults',
													'vkGetPhysicalDeviceXlibPresentationSupportKHR')
		COUNT_EXCEPTION = ('vkAcquireNextImageKHR', 'vkEnumerateInstanceVersion')


		# CLANG puts all useful items into a list called "inner"
		# First pass: get all the typedefs
		for i, v in enumerate(clangDictIn["inner"]):
			if v["kind"] == "TypedefDecl":
				logger.debug("TypedefDecl : " + v["name"])
				#logger.debug(v["type"]["qualType"])
				self.alias2real[v["name"]] = v["type"]["qualType"]
				logger.debug(v["type"]["qualType"])
				#die

			# also, gather up a list of class types. everything else will be void *
			elif v["kind"] == "RecordDecl":
				if "name" not in v.keys():
					continue
				if "inner" not in v.keys():
					# if there is no inner, typedef this to the void (typeless) pointer
					allClasses += v["name"] + " =  c_void_p \n"
					self.voidtypes[v["name"]] = ""

		# second pass: structs 
		for i, v in enumerate(clangDictIn["inner"]):
			if v["kind"] == "RecordDecl":
				if "name" not in v.keys():
					continue
				if "inner" not in v.keys():
					continue

				## ig these are structs
				#if "VkInstanceCreateInfo" in v["name"]:
				#	print("FUCK")
				#	pass
				logger.debug(json.dumps(v, indent=2))
				allClasses += self.dict2ClassString(v["name"], v["inner"])
				self.allStructs += [v["name"]]
				
		# Third pass: everything else
		for i, v in enumerate(clangDictIn["inner"]):
			if v["kind"] == "FunctionDecl":
				convertstring = ""
				argstring = ""
				typesList = []
				hasCountParam  = False
				hasStringParam = False
				retstring = "    return {"
				
				# 3.1 pass (Vulkan only): identify function type
				for j, arg in enumerate(v["inner"]):
					argname = arg["name"]
					argtype2 = self.getCtypeFromString(arg["type"]["qualType"], isClassDef=True)
					if argtype2 == "POINTER(c_uint)" and v["name"] not in COUNT_EXCEPTION:
						hasCountParam = True
					if "char" in argtype2:
						hasStringParam = True
				
				# 3.2 pass: create function
				for j, arg in enumerate(v["inner"]):
					argname = arg["name"]
					argtype = self.getCtypeFromString(arg["type"]["qualType"], isClassDef=False)
					argtype2 = self.getCtypeFromString(arg["type"]["qualType"], isClassDef=True)
						
					typesList += [argtype2]
					if argtype in self.allStructs:
						argtype += "()"
					argstring += ", " + argname
					#logger.debug(json.dumps(arg, indent=2))

					# if the argument is not supplied, create an empty pointer
					convertstring += "    if \"" + argname + "\" in indict.keys():\n"
					convertstring += "         " + argname + " = indict[\"" + argname + "\"]\n"
					convertstring += "    else: \n"
					convertstring += "         " + argname + " = " + argtype + "\n"
					retstring += "\"" + argname + "\" : " + argname + ","
				
				argstring = argstring[2:]
				fnstring  = "def " + v["name"] + "(indict):\n"
				fnstring += "    indict = preprocess(indict)\n"
				fnstring += convertstring
				fnstring += "    print(" + libnameOut + "Lib." + v["name"] + ")\n"
				#fnstring += "    " + libnameOut + "Lib." + v["name"] + ".argtypes = [" + ", ".join(typesList) + "]\n"
				fnstring += "    retval = " + libnameOut + "Lib." + v["name"] + "(" + argstring + ")\n"
				fnstring += "    if retval:\n"
				fnstring += "       raise(BaseException(str(retval)))\n"
				retstring += "\"retval\" : retval"
				retstring = retstring + "}\n"

				allFunctions += fnstring + retstring
				#logger.debug(json.dumps(fdict, indent=2))

			elif v["kind"] == "RecordDecl":
				continue

			# ENUM Type
			elif v["kind"] == "EnumDecl":
				#spill2file(v)
				thisEnum = ""
				#thisEnum += "class " + v["name"] + "(Enum):\n"
				for innerDict in v["inner"]:
				
					if innerDict["kind"] == "EnumConstantDecl":
						# CLANG FUCKING NESTED AF
						try:
							valueDict = innerDict
							while "value" not in valueDict.keys():
								#logger.debug(json.dumps(valueDict, indent=2))
								valueDict = valueDict["inner"][0]
							thisEnum += innerDict["name"] + \
								" = " + str(valueDict["value"]) + "\n"
						except:
							print("wtf")
					else:
						die
						

				allEnum += thisEnum
				logger.debug(thisEnum)

			elif v["kind"] == "VarDecl":
				allVar += v["name"] + " = " + v["inner"][0]["inner"][0]["value"]
				#logger.debug(json.dumps(v, indent = 2))
				logger.debug("VarDecl : " + v["name"])
			elif v["kind"] == "TypedefDecl":
				continue # handled in first pass
			else:
				logger.debug(k)
				logger.debug(v["kind"])
				die

		aliasString = "typeDef = " + json.dumps(self.alias2real, indent = 2) + "\n"
		loadSoDLLString += aliasString
		loadSoDLLString += allTypeDecl
		loadSoDLLString += allEnum
		loadSoDLLString += allClasses
		loadSoDLLString += allFunctions
		with open(libnameOut + ".py", 'w+') as f:
			f.write(loadSoDLLString)

		with open("conversions.json", "w+") as f:
			f.write(json.dumps(self.conversions, indent=2))

		with open("alias2real.json", "w+") as f:
			f.write(json.dumps(self.alias2real, indent=2))
			
		with open("allStructs.json", "w+") as f:
			f.write(json.dumps(self.allStructs, indent=2))

