import sodll
import os
import platform
import json
p = platform.platform().lower()
HERE = os.path.dirname(os.path.realpath(__file__))

if "nt" in p or "win" in p:
    library = os.path.join(HERE, "vulkan", "vulkan-1.dll")
    header  = os.path.join(HERE, "vulkan", "windows_cdef.h")
else:
    # PUT CPP COMMAND HERE
    
    # (if x86)
    library = os.path.join(HERE, "vulkan", "libvulkan.so")
    header  = os.path.join(HERE, "vulkan", "cdef.h")

ast = sodll.sodllGenerate(
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
            print(str(item))
           
print("CFFI Interface (contains structs):")
#print(dir(jvulkanCtypes))

#print(jvulkanInterface.integer_const("VK_BUFFER_USAGE_SHADER_DEVICE_ADDRESS_BIT"))
print("CFFI Library (contains executable code):")
#print(dir(jvulkanLib))
print("trying DL")



def VK_MAKE_VERSION(major, minor, patch):
    return (((major) << 22) | ((minor) << 12) | (patch))


def VK_VERSION_MAJOR(version):
    return version >> 22


def VK_VERSION_MINOR(version):
    return (version >> 12) & 0x3ff


def VK_VERSION_PATCH(version):
    return version & 0xfff
def getArguments(fn):
    arguments = str(fn).split("(")[2].split(")")[0].split(",")
    return arguments
       
print("getting extensions: ")

version = jvulkanInterface.new("uint32_t *")
c = jvulkanLib.vkEnumerateInstanceVersion(version)
print(version[0])

arguments = getArguments(vkEnumerateInstanceExtensionProperties)
die
pLayerName     = ffi.new("const char[]          ", "".encode('ascii'))
pPropertyCount = ffi.new("uint32_t*             ", 0)
#pProperties    = ffi.new("VkExtensionProperties*")  
pProperties    = ffi.NULL
    
extensions = vkEnumerateInstanceExtensionProperties(pLayerName, pPropertyCount, pProperties)
newtype = "VkExtensionProperties[" + str(pPropertyCount[0]) + "]"
print(newtype)
pProperties = ffi.cast(newtype, pProperties)
extensions = [e.extensionName for e in pProperties]
print("available extensions: ")
for e in pProperties:
    print("    " + str(e))
die
layers = vkEnumerateInstanceLayerProperties()
layers = [l.layerName for l in layers]
print("available layers:")
for l in layers:
    print("    " + l)
    
print(VK_STRUCTURE_TYPE_APPLICATION_INFO)
appInfo = jvulkanInterface.new("VkApplicationInfo *")
print(dir(appInfo))
print(jvulkanInterface.list_types())

appInfo.sType              = VK_STRUCTURE_TYPE_APPLICATION_INFO
appInfo.pApplicationName   = cdataStr("Hello Triangle")
appInfo.applicationVersion = VK_MAKE_VERSION(1, 0, 0)
appInfo.pEngineName        = cdataStr("No Engine")
appInfo.engineVersion      = VK_MAKE_VERSION(1, 0, 0)
appInfo.apiVersion         = VK_MAKE_VERSION(1, 0, 0)


createInfo = jvulkanInterface.new("VkInstanceCreateInfo *")
createInfo.sType=VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO
createInfo.flags=0
createInfo.pApplicationInfo=appInfo
createInfo.enabledExtensionCount=len(extensions)
createInfo.ppEnabledExtensionNames=extensions
createInfo.enabledLayerCount=len(layers)
createInfo.ppEnabledLayerNames=layers



vkInstance = vkCreateInstance(createInfo, None)
    
deviceIndex = 0
physical_device = vkEnumeratePhysicalDevices(vkInstance)[deviceIndex]

device_create = VkDeviceCreateInfo(
    sType=VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO,
    pNext = self.pFeatures2,
    pQueueCreateInfos    =queues_create,
    queueCreateInfoCount =len(queues_create),
    pEnabledFeatures     =self.pFeatures, # NEED TO PUT PFEATURES2 or something
    flags                =0,
    enabledLayerCount    =len(self.instance.layers),
    ppEnabledLayerNames  =self.instance.layers,
    enabledExtensionCount=len(extensions),
    ppEnabledExtensionNames=extensions
)

vkDevice = vkCreateDevice(
    physicalDevice = self.physical_device, 
    pCreateInfo    = self.device_create, 
    pAllocator     = None)
		
       
image = jvulkanInterface.new("bufferDeviceAddressInfo *")
c = jvulkanLib.vkGetBufferDeviceAddressKHR(vkDevice, image)



#print("trying IF") 
#c = jvulkanInterface.vkEnumerateInstanceVersion()
