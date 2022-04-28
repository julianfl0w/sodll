from ctypes import *
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

def sodllGenerate(library, header, libname, compilation = False):
	libc = CDLL(library)
	print(dir(libc))
	basedir = os.path.dirname(library)
	ffi = FFI()

	# read file
	with open(header) as f:
		cdef = f.read()

	# configure cffi
	# cdef() expects a single string declaring the C types, functions and
	# globals needed to use the shared object. It must be in valid C syntax.
	print("sending the string")
	ffi.cdef(cdef)

	if compilation:
		# set_source() gives the name of the python extension module to
		# produce, and some C source code as a string.  This C code needs
		# to make the declarated functions, types and globals available,
		# so it is often just the "#include".
		print("setting the source")

		ffi.set_source(libname, None)
		ffi.compile(verbose=True)
	
	return ffi

library = sys.argv[1]
header  = sys.argv[2]

outdir  = os.path.dirname(library)
cdefFile = os.path.join(outdir, "cdef.h")
print("generating cdef")
generate_cdef(header, os.path.dirname(header), cdefFile)
print("generating sodll")
libname = 'outlib'
libffi = sodllGenerate(library, cdefFile, libname)

from outlib import *
print(dir(libffi))
types = libffi.list_types()[0]
with open(libname + "_types.txt", 'w+') as f:
	f.write(json.dumps(types, indent=2))

for t in types:
	if t.startswith("PFN_"):
		fname = t.replace("PFN_", "")
		print(fname)
		
