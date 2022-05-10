import sodll
import os
import platform
import json
import shutil
p = platform.platform().lower()
HERE = os.path.dirname(os.path.realpath(__file__))

if "nt" in p or "win" in p:
    library = os.path.join(HERE, "vulkan", "vulkan-1.dll")
else:
    # (if x86)
    library = os.path.join(HERE, "vulkan", "libvulkan.so")

# clang dict created from headers with createInterfaceJSON.sh
with open("vulkan/vulkanInterface.json", "r") as f:
    clangDict = json.loads(f.read())

s = sodll.Sodll(
    dynamicLibraryFilenameIn = library, 
    clangDictIn = clangDict, 
    libnameOut  = "jvulkan")

shutil.copyfile("jvulkan.py", "../vulkanese/vulkanese/jvulkan.py")


# now we can import it (!)
from jvulkan import *


def VK_MAKE_VERSION(major, minor, patch):
    return (((major) << 22) | ((minor) << 12) | (patch))


def VK_VERSION_MAJOR(version):
    return version >> 22


def VK_VERSION_MINOR(version):
    return (version >> 12) & 0x3ff


def VK_VERSION_PATCH(version):
    return version & 0xfff

       
print("getting extensions: ")

pApiVersion = POINTER(c_uint)
c = vkEnumerateInstanceVersion({})
for k, v in c.items():
    print(v.contents)

pLayerName = ""

extenstions = vkEnumerateInstanceExtensionProperties({"pLayerName" : None})
for k, v in extenstions.items():
    print(k + ": " + str(v))
print(extenstions["pPropertyCount"].contents)
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
