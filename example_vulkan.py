import sodll
import os
import platform
import json
p = platform.platform().lower()
HERE = os.path.dirname(os.path.realpath(__file__))

if "nt" in p or "win" in p:
    library = os.path.join(HERE, "vulkan", "vulkan-1.dll")
else:
    library = os.path.join(HERE, "vulkan", "libvulkan.so")

header  = os.path.join(HERE, "vulkan", "cdef.h")
sodll.sodllGenerate(
    dynamicLibraryFilenameIn = library, 
    formattedHeaderIn = header, 
    libnameOut = "jvulkan")

# now we can import it (!)
from jvulkan import *

# If you want to view all the types
#print(dir(jvulkanDynamicLibrary))
types = jvulkanInterface.list_types()[0]
with open("vulkan_types.txt", 'w+') as f:
    f.write(json.dumps(types, indent=2))

def printObj(obj):
    print("Object " + str(obj))
    for item in dir(obj):
        if not item.startswith("__"):
            print("  " + str(item))
           
print("CFFI Interface (contains structs):")
#printObj(jvulkanInterface     )
print("CFFI Interface (contains executable code):")
#printObj(jvulkanDynamicLibrary)

print("trying DL")

image = jvulkanInterface.new("uint32_t *")
c = jvulkanDynamicLibrary.vkEnumerateInstanceVersion(image)
print(image[0])

#print("trying IF") 
#c = jvulkanInterface.vkEnumerateInstanceVersion()
