from cffi import FFI
import os
import sys
import subprocess
import json
from CppHeaderParser import CppHeader, CppParseError
from pycparser import c_parser

HERE = os.path.dirname(os.path.realpath(__file__))


# windows
#if "nt" in os.name.lower():
fake_libc_path = os.path.join(HERE, "fake_libc_include")
def generate_cdef(header,
				  include_path, 
				  out_file,
				  fake_libc = False):
	"""Generate the cdef output file"""
	if fake_libc:
		fake_path = fake_libc_path
	else:
		fake_path = ""
		
	command = ['cpp',
			   '-std=c99',
			   '-P',
			   '-nostdinc',
			   '-I' + include_path,
			   '-I' + fake_path,
			   '-o' + out_file,
			   '-DVK_USE_PLATFORM_XCB_KHR',
			   '-DVK_USE_PLATFORM_WAYLAND_KHR',
			   '-DVK_USE_PLATFORM_ANDROID_KHR',
			   '-DVK_USE_PLATFORM_WIN32_KHR',
			   '-DVK_USE_PLATFORM_XLIB_KHR',
			   header]
	print(" ".join(command))
	subprocess.run(command, check=True)
	print("generated cdef")

import platform
def cpp_args(args=[]):
    """Turn args into a suitable format for passing to cpp."""
    if isinstance(args, str):
        args = [args]
    if platform.system() == 'Darwin':
        return ['-E'] + args
    return args

def sodllGenerate(dynamicLibraryFilenameIn, formattedHeaderIn, libnameOut):

	basedir = os.path.dirname(dynamicLibraryFilenameIn)
	ffi = FFI()

	# read file
	with open(formattedHeaderIn) as f:
		cdef = f.read()

	# configure cffi
	# cdef() expects a single string declaring the C types, functions and
	# globals needed to use the shared object. It must be in valid C syntax.
	print("sending the string")
	ffi.cdef(cdef)
	

	parser = c_parser.CParser()
	addl = """
typedef char uint8_t;
typedef int size_t;
typedef int int32_t;
typedef int uint32_t;
typedef short uint16_t;
typedef long int64_t;
typedef int wchar_t; 
typedef unsigned long uint64_t; 
"""
	ddef = addl + cdef
	ast = parser.parse(ddef, filename='<none>')
	ast.show()
	die
	for e in ast.ext:
		try:
			print(e)
		except:
			pass
	with open("ast.txt", "w+") as f:
		f.write(str([str(a) for a in ast]))
	die
	
	# set_source() gives the name of the python extension module to
	# produce, and some C source code as a string.  This C code needs
	# to make the declarated functions, types and globals available,
	# so it is often just the "#include".
	print("compiling header to a python file")
	ffi.set_source(libnameOut, None)
	ffi.compile(verbose=True)
	
	print("adding helper functions to the file we just generated")
	loadSoDLLString = """
from ctypes import *


OUTLIBNAMELib = ffi.dlopen("LIBRARY")
OUTLIBNAMEInterface = ffi
OUTLIBNAMECtypes = CDLL("LIBRARY") 

def cdataStr(instr):
    return ffi.new(\"char[]\", instr.encode('ascii'))
	
# Generate Constants (ex VK_ACCELERATION_STRUCTURE_BUILD_TYPE_DEVICE_KHR)
"""
	loadSoDLLString = loadSoDLLString.replace("LIBRARY", dynamicLibraryFilenameIn )
	loadSoDLLString = loadSoDLLString.replace("OUTLIBNAME", libnameOut )
	

	(typedef_names, names_of_structs, names_of_unions) = ffi.list_types()
	#print(typedef_names)
	#print(names_of_structs)
	#print(names_of_unions)
	lib = ffi.dlopen(dynamicLibraryFilenameIn)
	loadSoDLLString += "UNSTATABLE = []\n"
	
	
	# FOR SOME REASON, DEFINES ARE IN THE FUCKING LIBRARY
	for name in dir(lib):
		if name.startswith("__"):
			continue
		loadSoDLLString += "try:\n"
		loadSoDLLString += "    " + name + " = " + libnameOut + "Lib." + name + "\n"
		loadSoDLLString += "    #print(\"statd " + name + "\")\n"
		loadSoDLLString += "except Exception as e:\n"
		#loadSoDLLString += "    print(e)\n"
		loadSoDLLString += "    pass\n"
		loadSoDLLString += "    UNSTATABLE += [\"" + name + "\"]\n"
		
		
	# or we can do if from FFI?
	#for s in names_of_structs:
	#	print("trying " + s)
	#	try:
	#		appInfo = ffi.getctype(s + " *")
	#	except:
	#		continue
	#	print(appInfo.args)
	#	loadSoDLLString += "class " + s + ":\n"
	#	loadSoDLLString += "    pass\n"
	#	print("finished " + s)
		
		
	loadSoDLLString += """
with open("UNSTATABLE", 'w+') as f:
	f.write(str(UNSTATABLE))
"""
	
	
	with open(libnameOut + ".py", 'a') as f:
		f.write(loadSoDLLString)
	
	return ffi

def getLibrary(library, header):

	outdir  = os.path.dirname(library)
	cdefFile = os.path.join(outdir, "cdef.h")
	
	# THIS STEP SHOULD BE DONE ONCE, WITH EVERY UPDATE
	#print("generating cdef")
	#generate_cdef(header, os.path.dirname(header), cdefFile)
	print("generating sodll")
	libname = 'outlib'
	libffi = sodllGenerate(library, cdefFile, libname)
