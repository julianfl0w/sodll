from cffi import FFI
import os
import sys
import subprocess
import json

HERE = os.path.dirname(os.path.realpath(__file__))

# windows
#if "nt" in os.name.lower():

def generate_cdef(header,
				  include_path, 
				  out_file):
	"""Generate the cdef output file"""
	fake_path = os.path.join(HERE, "fake_libc_include")
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

	# set_source() gives the name of the python extension module to
	# produce, and some C source code as a string.  This C code needs
	# to make the declarated functions, types and globals available,
	# so it is often just the "#include".
	print("compiling header to a python file")
	ffi.set_source(libnameOut, None)
	ffi.compile(verbose=True)
	
	print("adding helper functions to the file we just generated")
	loadSoDLLString = """
OUTLIBNAMEDynamicLibrary = ffi.dlopen("LIBRARY")
OUTLIBNAMEInterface = ffi
"""
	with open(libnameOut + ".py", 'a') as f:
		loadSoDLLString = loadSoDLLString.replace("LIBRARY", dynamicLibraryFilenameIn )
		loadSoDLLString = loadSoDLLString.replace("OUTLIBNAME", libnameOut )
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
