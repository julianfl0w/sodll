
from ctypes import *
jvulkanLib = CDLL("/home/julian/Documents/sodll/vulkan/libvulkan.so") 

def cdataStr(instr):
    return ffi.new("char[]", instr.encode('ascii'))
	
# Generate Constants (ex VK_ACCELERATION_STRUCTURE_BUILD_TYPE_DEVICE_KHR)
class wchar_t(Structure):
    _fields_ = [
             ("__clang_max_align_nonce1", c_longlong),
             ("__clang_max_align_nonce2", c_longdouble)
    ]
class __pid_t(Structure):
    _fields_ = [
             ("__val", c_int*2)
    ]
def vkCreateInstance(pCreateInfo, pAllocator, pInstance):
    jvulkanLib.vkCreateInstance(pCreateInfo, pAllocator, pInstance)
def vkDestroyInstance(instance, pAllocator):
    jvulkanLib.vkDestroyInstance(instance, pAllocator)
def vkEnumeratePhysicalDevices(instance, pPhysicalDeviceCount, pPhysicalDevices):
    jvulkanLib.vkEnumeratePhysicalDevices(instance, pPhysicalDeviceCount, pPhysicalDevices)
def vkGetPhysicalDeviceFeatures(physicalDevice, pFeatures):
    jvulkanLib.vkGetPhysicalDeviceFeatures(physicalDevice, pFeatures)
def vkGetPhysicalDeviceFormatProperties(physicalDevice, format, pFormatProperties):
    jvulkanLib.vkGetPhysicalDeviceFormatProperties(physicalDevice, format, pFormatProperties)
def vkGetPhysicalDeviceImageFormatProperties(physicalDevice, format, type, tiling, usage, flags, pImageFormatProperties):
    jvulkanLib.vkGetPhysicalDeviceImageFormatProperties(physicalDevice, format, type, tiling, usage, flags, pImageFormatProperties)
def vkGetPhysicalDeviceProperties(physicalDevice, pProperties):
    jvulkanLib.vkGetPhysicalDeviceProperties(physicalDevice, pProperties)
def vkGetPhysicalDeviceQueueFamilyProperties(physicalDevice, pQueueFamilyPropertyCount, pQueueFamilyProperties):
    jvulkanLib.vkGetPhysicalDeviceQueueFamilyProperties(physicalDevice, pQueueFamilyPropertyCount, pQueueFamilyProperties)
def vkGetPhysicalDeviceMemoryProperties(physicalDevice, pMemoryProperties):
    jvulkanLib.vkGetPhysicalDeviceMemoryProperties(physicalDevice, pMemoryProperties)
def vkGetInstanceProcAddr(instance, pName):
    jvulkanLib.vkGetInstanceProcAddr(instance, pName)
def vkGetDeviceProcAddr(device, pName):
    jvulkanLib.vkGetDeviceProcAddr(device, pName)
def vkCreateDevice(physicalDevice, pCreateInfo, pAllocator, pDevice):
    jvulkanLib.vkCreateDevice(physicalDevice, pCreateInfo, pAllocator, pDevice)
def vkDestroyDevice(device, pAllocator):
    jvulkanLib.vkDestroyDevice(device, pAllocator)
def vkEnumerateInstanceExtensionProperties(pLayerName, pPropertyCount, pProperties):
    jvulkanLib.vkEnumerateInstanceExtensionProperties(pLayerName, pPropertyCount, pProperties)
def vkEnumerateDeviceExtensionProperties(physicalDevice, pLayerName, pPropertyCount, pProperties):
    jvulkanLib.vkEnumerateDeviceExtensionProperties(physicalDevice, pLayerName, pPropertyCount, pProperties)
def vkEnumerateInstanceLayerProperties(pPropertyCount, pProperties):
    jvulkanLib.vkEnumerateInstanceLayerProperties(pPropertyCount, pProperties)
def vkEnumerateDeviceLayerProperties(physicalDevice, pPropertyCount, pProperties):
    jvulkanLib.vkEnumerateDeviceLayerProperties(physicalDevice, pPropertyCount, pProperties)
def vkGetDeviceQueue(device, queueFamilyIndex, queueIndex, pQueue):
    jvulkanLib.vkGetDeviceQueue(device, queueFamilyIndex, queueIndex, pQueue)
def vkQueueSubmit(queue, submitCount, pSubmits, fence):
    jvulkanLib.vkQueueSubmit(queue, submitCount, pSubmits, fence)
def vkQueueWaitIdle(queue):
    jvulkanLib.vkQueueWaitIdle(queue)
def vkDeviceWaitIdle(device):
    jvulkanLib.vkDeviceWaitIdle(device)
def vkAllocateMemory(device, pAllocateInfo, pAllocator, pMemory):
    jvulkanLib.vkAllocateMemory(device, pAllocateInfo, pAllocator, pMemory)
def vkFreeMemory(device, memory, pAllocator):
    jvulkanLib.vkFreeMemory(device, memory, pAllocator)
def vkMapMemory(device, memory, offset, size, flags, ppData):
    jvulkanLib.vkMapMemory(device, memory, offset, size, flags, ppData)
def vkUnmapMemory(device, memory):
    jvulkanLib.vkUnmapMemory(device, memory)
def vkFlushMappedMemoryRanges(device, memoryRangeCount, pMemoryRanges):
    jvulkanLib.vkFlushMappedMemoryRanges(device, memoryRangeCount, pMemoryRanges)
def vkInvalidateMappedMemoryRanges(device, memoryRangeCount, pMemoryRanges):
    jvulkanLib.vkInvalidateMappedMemoryRanges(device, memoryRangeCount, pMemoryRanges)
def vkGetDeviceMemoryCommitment(device, memory, pCommittedMemoryInBytes):
    jvulkanLib.vkGetDeviceMemoryCommitment(device, memory, pCommittedMemoryInBytes)
def vkBindBufferMemory(device, buffer, memory, memoryOffset):
    jvulkanLib.vkBindBufferMemory(device, buffer, memory, memoryOffset)
def vkBindImageMemory(device, image, memory, memoryOffset):
    jvulkanLib.vkBindImageMemory(device, image, memory, memoryOffset)
def vkGetBufferMemoryRequirements(device, buffer, pMemoryRequirements):
    jvulkanLib.vkGetBufferMemoryRequirements(device, buffer, pMemoryRequirements)
def vkGetImageMemoryRequirements(device, image, pMemoryRequirements):
    jvulkanLib.vkGetImageMemoryRequirements(device, image, pMemoryRequirements)
def vkGetImageSparseMemoryRequirements(device, image, pSparseMemoryRequirementCount, pSparseMemoryRequirements):
    jvulkanLib.vkGetImageSparseMemoryRequirements(device, image, pSparseMemoryRequirementCount, pSparseMemoryRequirements)
def vkGetPhysicalDeviceSparseImageFormatProperties(physicalDevice, format, type, samples, usage, tiling, pPropertyCount, pProperties):
    jvulkanLib.vkGetPhysicalDeviceSparseImageFormatProperties(physicalDevice, format, type, samples, usage, tiling, pPropertyCount, pProperties)
def vkQueueBindSparse(queue, bindInfoCount, pBindInfo, fence):
    jvulkanLib.vkQueueBindSparse(queue, bindInfoCount, pBindInfo, fence)
def vkCreateFence(device, pCreateInfo, pAllocator, pFence):
    jvulkanLib.vkCreateFence(device, pCreateInfo, pAllocator, pFence)
def vkDestroyFence(device, fence, pAllocator):
    jvulkanLib.vkDestroyFence(device, fence, pAllocator)
def vkResetFences(device, fenceCount, pFences):
    jvulkanLib.vkResetFences(device, fenceCount, pFences)
def vkGetFenceStatus(device, fence):
    jvulkanLib.vkGetFenceStatus(device, fence)
def vkWaitForFences(device, fenceCount, pFences, waitAll, timeout):
    jvulkanLib.vkWaitForFences(device, fenceCount, pFences, waitAll, timeout)
def vkCreateSemaphore(device, pCreateInfo, pAllocator, pSemaphore):
    jvulkanLib.vkCreateSemaphore(device, pCreateInfo, pAllocator, pSemaphore)
def vkDestroySemaphore(device, semaphore, pAllocator):
    jvulkanLib.vkDestroySemaphore(device, semaphore, pAllocator)
def vkCreateEvent(device, pCreateInfo, pAllocator, pEvent):
    jvulkanLib.vkCreateEvent(device, pCreateInfo, pAllocator, pEvent)
def vkDestroyEvent(device, event, pAllocator):
    jvulkanLib.vkDestroyEvent(device, event, pAllocator)
def vkGetEventStatus(device, event):
    jvulkanLib.vkGetEventStatus(device, event)
def vkSetEvent(device, event):
    jvulkanLib.vkSetEvent(device, event)
def vkResetEvent(device, event):
    jvulkanLib.vkResetEvent(device, event)
def vkCreateQueryPool(device, pCreateInfo, pAllocator, pQueryPool):
    jvulkanLib.vkCreateQueryPool(device, pCreateInfo, pAllocator, pQueryPool)
def vkDestroyQueryPool(device, queryPool, pAllocator):
    jvulkanLib.vkDestroyQueryPool(device, queryPool, pAllocator)
def vkGetQueryPoolResults(device, queryPool, firstQuery, queryCount, dataSize, pData, stride, flags):
    jvulkanLib.vkGetQueryPoolResults(device, queryPool, firstQuery, queryCount, dataSize, pData, stride, flags)
def vkCreateBuffer(device, pCreateInfo, pAllocator, pBuffer):
    jvulkanLib.vkCreateBuffer(device, pCreateInfo, pAllocator, pBuffer)
def vkDestroyBuffer(device, buffer, pAllocator):
    jvulkanLib.vkDestroyBuffer(device, buffer, pAllocator)
def vkCreateBufferView(device, pCreateInfo, pAllocator, pView):
    jvulkanLib.vkCreateBufferView(device, pCreateInfo, pAllocator, pView)
def vkDestroyBufferView(device, bufferView, pAllocator):
    jvulkanLib.vkDestroyBufferView(device, bufferView, pAllocator)
def vkCreateImage(device, pCreateInfo, pAllocator, pImage):
    jvulkanLib.vkCreateImage(device, pCreateInfo, pAllocator, pImage)
def vkDestroyImage(device, image, pAllocator):
    jvulkanLib.vkDestroyImage(device, image, pAllocator)
def vkGetImageSubresourceLayout(device, image, pSubresource, pLayout):
    jvulkanLib.vkGetImageSubresourceLayout(device, image, pSubresource, pLayout)
def vkCreateImageView(device, pCreateInfo, pAllocator, pView):
    jvulkanLib.vkCreateImageView(device, pCreateInfo, pAllocator, pView)
def vkDestroyImageView(device, imageView, pAllocator):
    jvulkanLib.vkDestroyImageView(device, imageView, pAllocator)
def vkCreateShaderModule(device, pCreateInfo, pAllocator, pShaderModule):
    jvulkanLib.vkCreateShaderModule(device, pCreateInfo, pAllocator, pShaderModule)
def vkDestroyShaderModule(device, shaderModule, pAllocator):
    jvulkanLib.vkDestroyShaderModule(device, shaderModule, pAllocator)
def vkCreatePipelineCache(device, pCreateInfo, pAllocator, pPipelineCache):
    jvulkanLib.vkCreatePipelineCache(device, pCreateInfo, pAllocator, pPipelineCache)
def vkDestroyPipelineCache(device, pipelineCache, pAllocator):
    jvulkanLib.vkDestroyPipelineCache(device, pipelineCache, pAllocator)
def vkGetPipelineCacheData(device, pipelineCache, pDataSize, pData):
    jvulkanLib.vkGetPipelineCacheData(device, pipelineCache, pDataSize, pData)
def vkMergePipelineCaches(device, dstCache, srcCacheCount, pSrcCaches):
    jvulkanLib.vkMergePipelineCaches(device, dstCache, srcCacheCount, pSrcCaches)
def vkCreateGraphicsPipelines(device, pipelineCache, createInfoCount, pCreateInfos, pAllocator, pPipelines):
    jvulkanLib.vkCreateGraphicsPipelines(device, pipelineCache, createInfoCount, pCreateInfos, pAllocator, pPipelines)
def vkCreateComputePipelines(device, pipelineCache, createInfoCount, pCreateInfos, pAllocator, pPipelines):
    jvulkanLib.vkCreateComputePipelines(device, pipelineCache, createInfoCount, pCreateInfos, pAllocator, pPipelines)
def vkDestroyPipeline(device, pipeline, pAllocator):
    jvulkanLib.vkDestroyPipeline(device, pipeline, pAllocator)
def vkCreatePipelineLayout(device, pCreateInfo, pAllocator, pPipelineLayout):
    jvulkanLib.vkCreatePipelineLayout(device, pCreateInfo, pAllocator, pPipelineLayout)
def vkDestroyPipelineLayout(device, pipelineLayout, pAllocator):
    jvulkanLib.vkDestroyPipelineLayout(device, pipelineLayout, pAllocator)
def vkCreateSampler(device, pCreateInfo, pAllocator, pSampler):
    jvulkanLib.vkCreateSampler(device, pCreateInfo, pAllocator, pSampler)
def vkDestroySampler(device, sampler, pAllocator):
    jvulkanLib.vkDestroySampler(device, sampler, pAllocator)
def vkCreateDescriptorSetLayout(device, pCreateInfo, pAllocator, pSetLayout):
    jvulkanLib.vkCreateDescriptorSetLayout(device, pCreateInfo, pAllocator, pSetLayout)
def vkDestroyDescriptorSetLayout(device, descriptorSetLayout, pAllocator):
    jvulkanLib.vkDestroyDescriptorSetLayout(device, descriptorSetLayout, pAllocator)
def vkCreateDescriptorPool(device, pCreateInfo, pAllocator, pDescriptorPool):
    jvulkanLib.vkCreateDescriptorPool(device, pCreateInfo, pAllocator, pDescriptorPool)
def vkDestroyDescriptorPool(device, descriptorPool, pAllocator):
    jvulkanLib.vkDestroyDescriptorPool(device, descriptorPool, pAllocator)
def vkResetDescriptorPool(device, descriptorPool, flags):
    jvulkanLib.vkResetDescriptorPool(device, descriptorPool, flags)
def vkAllocateDescriptorSets(device, pAllocateInfo, pDescriptorSets):
    jvulkanLib.vkAllocateDescriptorSets(device, pAllocateInfo, pDescriptorSets)
def vkFreeDescriptorSets(device, descriptorPool, descriptorSetCount, pDescriptorSets):
    jvulkanLib.vkFreeDescriptorSets(device, descriptorPool, descriptorSetCount, pDescriptorSets)
def vkUpdateDescriptorSets(device, descriptorWriteCount, pDescriptorWrites, descriptorCopyCount, pDescriptorCopies):
    jvulkanLib.vkUpdateDescriptorSets(device, descriptorWriteCount, pDescriptorWrites, descriptorCopyCount, pDescriptorCopies)
def vkCreateFramebuffer(device, pCreateInfo, pAllocator, pFramebuffer):
    jvulkanLib.vkCreateFramebuffer(device, pCreateInfo, pAllocator, pFramebuffer)
def vkDestroyFramebuffer(device, framebuffer, pAllocator):
    jvulkanLib.vkDestroyFramebuffer(device, framebuffer, pAllocator)
def vkCreateRenderPass(device, pCreateInfo, pAllocator, pRenderPass):
    jvulkanLib.vkCreateRenderPass(device, pCreateInfo, pAllocator, pRenderPass)
def vkDestroyRenderPass(device, renderPass, pAllocator):
    jvulkanLib.vkDestroyRenderPass(device, renderPass, pAllocator)
def vkGetRenderAreaGranularity(device, renderPass, pGranularity):
    jvulkanLib.vkGetRenderAreaGranularity(device, renderPass, pGranularity)
def vkCreateCommandPool(device, pCreateInfo, pAllocator, pCommandPool):
    jvulkanLib.vkCreateCommandPool(device, pCreateInfo, pAllocator, pCommandPool)
def vkDestroyCommandPool(device, commandPool, pAllocator):
    jvulkanLib.vkDestroyCommandPool(device, commandPool, pAllocator)
def vkResetCommandPool(device, commandPool, flags):
    jvulkanLib.vkResetCommandPool(device, commandPool, flags)
def vkAllocateCommandBuffers(device, pAllocateInfo, pCommandBuffers):
    jvulkanLib.vkAllocateCommandBuffers(device, pAllocateInfo, pCommandBuffers)
def vkFreeCommandBuffers(device, commandPool, commandBufferCount, pCommandBuffers):
    jvulkanLib.vkFreeCommandBuffers(device, commandPool, commandBufferCount, pCommandBuffers)
def vkBeginCommandBuffer(commandBuffer, pBeginInfo):
    jvulkanLib.vkBeginCommandBuffer(commandBuffer, pBeginInfo)
def vkEndCommandBuffer(commandBuffer):
    jvulkanLib.vkEndCommandBuffer(commandBuffer)
def vkResetCommandBuffer(commandBuffer, flags):
    jvulkanLib.vkResetCommandBuffer(commandBuffer, flags)
def vkCmdBindPipeline(commandBuffer, pipelineBindPoint, pipeline):
    jvulkanLib.vkCmdBindPipeline(commandBuffer, pipelineBindPoint, pipeline)
def vkCmdSetViewport(commandBuffer, firstViewport, viewportCount, pViewports):
    jvulkanLib.vkCmdSetViewport(commandBuffer, firstViewport, viewportCount, pViewports)
def vkCmdSetScissor(commandBuffer, firstScissor, scissorCount, pScissors):
    jvulkanLib.vkCmdSetScissor(commandBuffer, firstScissor, scissorCount, pScissors)
def vkCmdSetLineWidth(commandBuffer, lineWidth):
    jvulkanLib.vkCmdSetLineWidth(commandBuffer, lineWidth)
def vkCmdSetDepthBias(commandBuffer, depthBiasConstantFactor, depthBiasClamp, depthBiasSlopeFactor):
    jvulkanLib.vkCmdSetDepthBias(commandBuffer, depthBiasConstantFactor, depthBiasClamp, depthBiasSlopeFactor)
def vkCmdSetBlendConstants(commandBuffer, blendConstants):
    jvulkanLib.vkCmdSetBlendConstants(commandBuffer, blendConstants)
def vkCmdSetDepthBounds(commandBuffer, minDepthBounds, maxDepthBounds):
    jvulkanLib.vkCmdSetDepthBounds(commandBuffer, minDepthBounds, maxDepthBounds)
def vkCmdSetStencilCompareMask(commandBuffer, faceMask, compareMask):
    jvulkanLib.vkCmdSetStencilCompareMask(commandBuffer, faceMask, compareMask)
def vkCmdSetStencilWriteMask(commandBuffer, faceMask, writeMask):
    jvulkanLib.vkCmdSetStencilWriteMask(commandBuffer, faceMask, writeMask)
def vkCmdSetStencilReference(commandBuffer, faceMask, reference):
    jvulkanLib.vkCmdSetStencilReference(commandBuffer, faceMask, reference)
def vkCmdBindDescriptorSets(commandBuffer, pipelineBindPoint, layout, firstSet, descriptorSetCount, pDescriptorSets, dynamicOffsetCount, pDynamicOffsets):
    jvulkanLib.vkCmdBindDescriptorSets(commandBuffer, pipelineBindPoint, layout, firstSet, descriptorSetCount, pDescriptorSets, dynamicOffsetCount, pDynamicOffsets)
def vkCmdBindIndexBuffer(commandBuffer, buffer, offset, indexType):
    jvulkanLib.vkCmdBindIndexBuffer(commandBuffer, buffer, offset, indexType)
def vkCmdBindVertexBuffers(commandBuffer, firstBinding, bindingCount, pBuffers, pOffsets):
    jvulkanLib.vkCmdBindVertexBuffers(commandBuffer, firstBinding, bindingCount, pBuffers, pOffsets)
def vkCmdDraw(commandBuffer, vertexCount, instanceCount, firstVertex, firstInstance):
    jvulkanLib.vkCmdDraw(commandBuffer, vertexCount, instanceCount, firstVertex, firstInstance)
def vkCmdDrawIndexed(commandBuffer, indexCount, instanceCount, firstIndex, vertexOffset, firstInstance):
    jvulkanLib.vkCmdDrawIndexed(commandBuffer, indexCount, instanceCount, firstIndex, vertexOffset, firstInstance)
def vkCmdDrawIndirect(commandBuffer, buffer, offset, drawCount, stride):
    jvulkanLib.vkCmdDrawIndirect(commandBuffer, buffer, offset, drawCount, stride)
def vkCmdDrawIndexedIndirect(commandBuffer, buffer, offset, drawCount, stride):
    jvulkanLib.vkCmdDrawIndexedIndirect(commandBuffer, buffer, offset, drawCount, stride)
def vkCmdDispatch(commandBuffer, groupCountX, groupCountY, groupCountZ):
    jvulkanLib.vkCmdDispatch(commandBuffer, groupCountX, groupCountY, groupCountZ)
def vkCmdDispatchIndirect(commandBuffer, buffer, offset):
    jvulkanLib.vkCmdDispatchIndirect(commandBuffer, buffer, offset)
def vkCmdCopyBuffer(commandBuffer, srcBuffer, dstBuffer, regionCount, pRegions):
    jvulkanLib.vkCmdCopyBuffer(commandBuffer, srcBuffer, dstBuffer, regionCount, pRegions)
def vkCmdCopyImage(commandBuffer, srcImage, srcImageLayout, dstImage, dstImageLayout, regionCount, pRegions):
    jvulkanLib.vkCmdCopyImage(commandBuffer, srcImage, srcImageLayout, dstImage, dstImageLayout, regionCount, pRegions)
def vkCmdBlitImage(commandBuffer, srcImage, srcImageLayout, dstImage, dstImageLayout, regionCount, pRegions, filter):
    jvulkanLib.vkCmdBlitImage(commandBuffer, srcImage, srcImageLayout, dstImage, dstImageLayout, regionCount, pRegions, filter)
def vkCmdCopyBufferToImage(commandBuffer, srcBuffer, dstImage, dstImageLayout, regionCount, pRegions):
    jvulkanLib.vkCmdCopyBufferToImage(commandBuffer, srcBuffer, dstImage, dstImageLayout, regionCount, pRegions)
def vkCmdCopyImageToBuffer(commandBuffer, srcImage, srcImageLayout, dstBuffer, regionCount, pRegions):
    jvulkanLib.vkCmdCopyImageToBuffer(commandBuffer, srcImage, srcImageLayout, dstBuffer, regionCount, pRegions)
def vkCmdUpdateBuffer(commandBuffer, dstBuffer, dstOffset, dataSize, pData):
    jvulkanLib.vkCmdUpdateBuffer(commandBuffer, dstBuffer, dstOffset, dataSize, pData)
def vkCmdFillBuffer(commandBuffer, dstBuffer, dstOffset, size, data):
    jvulkanLib.vkCmdFillBuffer(commandBuffer, dstBuffer, dstOffset, size, data)
def vkCmdClearColorImage(commandBuffer, image, imageLayout, pColor, rangeCount, pRanges):
    jvulkanLib.vkCmdClearColorImage(commandBuffer, image, imageLayout, pColor, rangeCount, pRanges)
def vkCmdClearDepthStencilImage(commandBuffer, image, imageLayout, pDepthStencil, rangeCount, pRanges):
    jvulkanLib.vkCmdClearDepthStencilImage(commandBuffer, image, imageLayout, pDepthStencil, rangeCount, pRanges)
def vkCmdClearAttachments(commandBuffer, attachmentCount, pAttachments, rectCount, pRects):
    jvulkanLib.vkCmdClearAttachments(commandBuffer, attachmentCount, pAttachments, rectCount, pRects)
def vkCmdResolveImage(commandBuffer, srcImage, srcImageLayout, dstImage, dstImageLayout, regionCount, pRegions):
    jvulkanLib.vkCmdResolveImage(commandBuffer, srcImage, srcImageLayout, dstImage, dstImageLayout, regionCount, pRegions)
def vkCmdSetEvent(commandBuffer, event, stageMask):
    jvulkanLib.vkCmdSetEvent(commandBuffer, event, stageMask)
def vkCmdResetEvent(commandBuffer, event, stageMask):
    jvulkanLib.vkCmdResetEvent(commandBuffer, event, stageMask)
def vkCmdWaitEvents(commandBuffer, eventCount, pEvents, srcStageMask, dstStageMask, memoryBarrierCount, pMemoryBarriers, bufferMemoryBarrierCount, pBufferMemoryBarriers, imageMemoryBarrierCount, pImageMemoryBarriers):
    jvulkanLib.vkCmdWaitEvents(commandBuffer, eventCount, pEvents, srcStageMask, dstStageMask, memoryBarrierCount, pMemoryBarriers, bufferMemoryBarrierCount, pBufferMemoryBarriers, imageMemoryBarrierCount, pImageMemoryBarriers)
def vkCmdPipelineBarrier(commandBuffer, srcStageMask, dstStageMask, dependencyFlags, memoryBarrierCount, pMemoryBarriers, bufferMemoryBarrierCount, pBufferMemoryBarriers, imageMemoryBarrierCount, pImageMemoryBarriers):
    jvulkanLib.vkCmdPipelineBarrier(commandBuffer, srcStageMask, dstStageMask, dependencyFlags, memoryBarrierCount, pMemoryBarriers, bufferMemoryBarrierCount, pBufferMemoryBarriers, imageMemoryBarrierCount, pImageMemoryBarriers)
def vkCmdBeginQuery(commandBuffer, queryPool, query, flags):
    jvulkanLib.vkCmdBeginQuery(commandBuffer, queryPool, query, flags)
def vkCmdEndQuery(commandBuffer, queryPool, query):
    jvulkanLib.vkCmdEndQuery(commandBuffer, queryPool, query)
def vkCmdResetQueryPool(commandBuffer, queryPool, firstQuery, queryCount):
    jvulkanLib.vkCmdResetQueryPool(commandBuffer, queryPool, firstQuery, queryCount)
def vkCmdWriteTimestamp(commandBuffer, pipelineStage, queryPool, query):
    jvulkanLib.vkCmdWriteTimestamp(commandBuffer, pipelineStage, queryPool, query)
def vkCmdCopyQueryPoolResults(commandBuffer, queryPool, firstQuery, queryCount, dstBuffer, dstOffset, stride, flags):
    jvulkanLib.vkCmdCopyQueryPoolResults(commandBuffer, queryPool, firstQuery, queryCount, dstBuffer, dstOffset, stride, flags)
def vkCmdPushConstants(commandBuffer, layout, stageFlags, offset, size, pValues):
    jvulkanLib.vkCmdPushConstants(commandBuffer, layout, stageFlags, offset, size, pValues)
def vkCmdBeginRenderPass(commandBuffer, pRenderPassBegin, contents):
    jvulkanLib.vkCmdBeginRenderPass(commandBuffer, pRenderPassBegin, contents)
def vkCmdNextSubpass(commandBuffer, contents):
    jvulkanLib.vkCmdNextSubpass(commandBuffer, contents)
def vkCmdEndRenderPass(commandBuffer):
    jvulkanLib.vkCmdEndRenderPass(commandBuffer)
def vkCmdExecuteCommands(commandBuffer, commandBufferCount, pCommandBuffers):
    jvulkanLib.vkCmdExecuteCommands(commandBuffer, commandBufferCount, pCommandBuffers)
def vkEnumerateInstanceVersion(pApiVersion):
    jvulkanLib.vkEnumerateInstanceVersion(pApiVersion)
def vkBindBufferMemory2(device, bindInfoCount, pBindInfos):
    jvulkanLib.vkBindBufferMemory2(device, bindInfoCount, pBindInfos)
def vkBindImageMemory2(device, bindInfoCount, pBindInfos):
    jvulkanLib.vkBindImageMemory2(device, bindInfoCount, pBindInfos)
def vkGetDeviceGroupPeerMemoryFeatures(device, heapIndex, localDeviceIndex, remoteDeviceIndex, pPeerMemoryFeatures):
    jvulkanLib.vkGetDeviceGroupPeerMemoryFeatures(device, heapIndex, localDeviceIndex, remoteDeviceIndex, pPeerMemoryFeatures)
def vkCmdSetDeviceMask(commandBuffer, deviceMask):
    jvulkanLib.vkCmdSetDeviceMask(commandBuffer, deviceMask)
def vkCmdDispatchBase(commandBuffer, baseGroupX, baseGroupY, baseGroupZ, groupCountX, groupCountY, groupCountZ):
    jvulkanLib.vkCmdDispatchBase(commandBuffer, baseGroupX, baseGroupY, baseGroupZ, groupCountX, groupCountY, groupCountZ)
def vkEnumeratePhysicalDeviceGroups(instance, pPhysicalDeviceGroupCount, pPhysicalDeviceGroupProperties):
    jvulkanLib.vkEnumeratePhysicalDeviceGroups(instance, pPhysicalDeviceGroupCount, pPhysicalDeviceGroupProperties)
def vkGetImageMemoryRequirements2(device, pInfo, pMemoryRequirements):
    jvulkanLib.vkGetImageMemoryRequirements2(device, pInfo, pMemoryRequirements)
def vkGetBufferMemoryRequirements2(device, pInfo, pMemoryRequirements):
    jvulkanLib.vkGetBufferMemoryRequirements2(device, pInfo, pMemoryRequirements)
def vkGetImageSparseMemoryRequirements2(device, pInfo, pSparseMemoryRequirementCount, pSparseMemoryRequirements):
    jvulkanLib.vkGetImageSparseMemoryRequirements2(device, pInfo, pSparseMemoryRequirementCount, pSparseMemoryRequirements)
def vkGetPhysicalDeviceFeatures2(physicalDevice, pFeatures):
    jvulkanLib.vkGetPhysicalDeviceFeatures2(physicalDevice, pFeatures)
def vkGetPhysicalDeviceProperties2(physicalDevice, pProperties):
    jvulkanLib.vkGetPhysicalDeviceProperties2(physicalDevice, pProperties)
def vkGetPhysicalDeviceFormatProperties2(physicalDevice, format, pFormatProperties):
    jvulkanLib.vkGetPhysicalDeviceFormatProperties2(physicalDevice, format, pFormatProperties)
def vkGetPhysicalDeviceImageFormatProperties2(physicalDevice, pImageFormatInfo, pImageFormatProperties):
    jvulkanLib.vkGetPhysicalDeviceImageFormatProperties2(physicalDevice, pImageFormatInfo, pImageFormatProperties)
def vkGetPhysicalDeviceQueueFamilyProperties2(physicalDevice, pQueueFamilyPropertyCount, pQueueFamilyProperties):
    jvulkanLib.vkGetPhysicalDeviceQueueFamilyProperties2(physicalDevice, pQueueFamilyPropertyCount, pQueueFamilyProperties)
def vkGetPhysicalDeviceMemoryProperties2(physicalDevice, pMemoryProperties):
    jvulkanLib.vkGetPhysicalDeviceMemoryProperties2(physicalDevice, pMemoryProperties)
def vkGetPhysicalDeviceSparseImageFormatProperties2(physicalDevice, pFormatInfo, pPropertyCount, pProperties):
    jvulkanLib.vkGetPhysicalDeviceSparseImageFormatProperties2(physicalDevice, pFormatInfo, pPropertyCount, pProperties)
def vkTrimCommandPool(device, commandPool, flags):
    jvulkanLib.vkTrimCommandPool(device, commandPool, flags)
def vkGetDeviceQueue2(device, pQueueInfo, pQueue):
    jvulkanLib.vkGetDeviceQueue2(device, pQueueInfo, pQueue)
def vkCreateSamplerYcbcrConversion(device, pCreateInfo, pAllocator, pYcbcrConversion):
    jvulkanLib.vkCreateSamplerYcbcrConversion(device, pCreateInfo, pAllocator, pYcbcrConversion)
def vkDestroySamplerYcbcrConversion(device, ycbcrConversion, pAllocator):
    jvulkanLib.vkDestroySamplerYcbcrConversion(device, ycbcrConversion, pAllocator)
def vkCreateDescriptorUpdateTemplate(device, pCreateInfo, pAllocator, pDescriptorUpdateTemplate):
    jvulkanLib.vkCreateDescriptorUpdateTemplate(device, pCreateInfo, pAllocator, pDescriptorUpdateTemplate)
def vkDestroyDescriptorUpdateTemplate(device, descriptorUpdateTemplate, pAllocator):
    jvulkanLib.vkDestroyDescriptorUpdateTemplate(device, descriptorUpdateTemplate, pAllocator)
def vkUpdateDescriptorSetWithTemplate(device, descriptorSet, descriptorUpdateTemplate, pData):
    jvulkanLib.vkUpdateDescriptorSetWithTemplate(device, descriptorSet, descriptorUpdateTemplate, pData)
def vkGetPhysicalDeviceExternalBufferProperties(physicalDevice, pExternalBufferInfo, pExternalBufferProperties):
    jvulkanLib.vkGetPhysicalDeviceExternalBufferProperties(physicalDevice, pExternalBufferInfo, pExternalBufferProperties)
def vkGetPhysicalDeviceExternalFenceProperties(physicalDevice, pExternalFenceInfo, pExternalFenceProperties):
    jvulkanLib.vkGetPhysicalDeviceExternalFenceProperties(physicalDevice, pExternalFenceInfo, pExternalFenceProperties)
def vkGetPhysicalDeviceExternalSemaphoreProperties(physicalDevice, pExternalSemaphoreInfo, pExternalSemaphoreProperties):
    jvulkanLib.vkGetPhysicalDeviceExternalSemaphoreProperties(physicalDevice, pExternalSemaphoreInfo, pExternalSemaphoreProperties)
def vkGetDescriptorSetLayoutSupport(device, pCreateInfo, pSupport):
    jvulkanLib.vkGetDescriptorSetLayoutSupport(device, pCreateInfo, pSupport)
def vkCmdDrawIndirectCount(commandBuffer, buffer, offset, countBuffer, countBufferOffset, maxDrawCount, stride):
    jvulkanLib.vkCmdDrawIndirectCount(commandBuffer, buffer, offset, countBuffer, countBufferOffset, maxDrawCount, stride)
def vkCmdDrawIndexedIndirectCount(commandBuffer, buffer, offset, countBuffer, countBufferOffset, maxDrawCount, stride):
    jvulkanLib.vkCmdDrawIndexedIndirectCount(commandBuffer, buffer, offset, countBuffer, countBufferOffset, maxDrawCount, stride)
def vkCreateRenderPass2(device, pCreateInfo, pAllocator, pRenderPass):
    jvulkanLib.vkCreateRenderPass2(device, pCreateInfo, pAllocator, pRenderPass)
def vkCmdBeginRenderPass2(commandBuffer, pRenderPassBegin, pSubpassBeginInfo):
    jvulkanLib.vkCmdBeginRenderPass2(commandBuffer, pRenderPassBegin, pSubpassBeginInfo)
def vkCmdNextSubpass2(commandBuffer, pSubpassBeginInfo, pSubpassEndInfo):
    jvulkanLib.vkCmdNextSubpass2(commandBuffer, pSubpassBeginInfo, pSubpassEndInfo)
def vkCmdEndRenderPass2(commandBuffer, pSubpassEndInfo):
    jvulkanLib.vkCmdEndRenderPass2(commandBuffer, pSubpassEndInfo)
def vkResetQueryPool(device, queryPool, firstQuery, queryCount):
    jvulkanLib.vkResetQueryPool(device, queryPool, firstQuery, queryCount)
def vkGetSemaphoreCounterValue(device, semaphore, pValue):
    jvulkanLib.vkGetSemaphoreCounterValue(device, semaphore, pValue)
def vkWaitSemaphores(device, pWaitInfo, timeout):
    jvulkanLib.vkWaitSemaphores(device, pWaitInfo, timeout)
def vkSignalSemaphore(device, pSignalInfo):
    jvulkanLib.vkSignalSemaphore(device, pSignalInfo)
def vkGetBufferDeviceAddress(device, pInfo):
    jvulkanLib.vkGetBufferDeviceAddress(device, pInfo)
def vkGetBufferOpaqueCaptureAddress(device, pInfo):
    jvulkanLib.vkGetBufferOpaqueCaptureAddress(device, pInfo)
def vkGetDeviceMemoryOpaqueCaptureAddress(device, pInfo):
    jvulkanLib.vkGetDeviceMemoryOpaqueCaptureAddress(device, pInfo)
def vkGetPhysicalDeviceToolProperties(physicalDevice, pToolCount, pToolProperties):
    jvulkanLib.vkGetPhysicalDeviceToolProperties(physicalDevice, pToolCount, pToolProperties)
def vkCreatePrivateDataSlot(device, pCreateInfo, pAllocator, pPrivateDataSlot):
    jvulkanLib.vkCreatePrivateDataSlot(device, pCreateInfo, pAllocator, pPrivateDataSlot)
def vkDestroyPrivateDataSlot(device, privateDataSlot, pAllocator):
    jvulkanLib.vkDestroyPrivateDataSlot(device, privateDataSlot, pAllocator)
def vkSetPrivateData(device, objectType, objectHandle, privateDataSlot, data):
    jvulkanLib.vkSetPrivateData(device, objectType, objectHandle, privateDataSlot, data)
def vkGetPrivateData(device, objectType, objectHandle, privateDataSlot, pData):
    jvulkanLib.vkGetPrivateData(device, objectType, objectHandle, privateDataSlot, pData)
def vkCmdSetEvent2(commandBuffer, event, pDependencyInfo):
    jvulkanLib.vkCmdSetEvent2(commandBuffer, event, pDependencyInfo)
def vkCmdResetEvent2(commandBuffer, event, stageMask):
    jvulkanLib.vkCmdResetEvent2(commandBuffer, event, stageMask)
def vkCmdWaitEvents2(commandBuffer, eventCount, pEvents, pDependencyInfos):
    jvulkanLib.vkCmdWaitEvents2(commandBuffer, eventCount, pEvents, pDependencyInfos)
def vkCmdPipelineBarrier2(commandBuffer, pDependencyInfo):
    jvulkanLib.vkCmdPipelineBarrier2(commandBuffer, pDependencyInfo)
def vkCmdWriteTimestamp2(commandBuffer, stage, queryPool, query):
    jvulkanLib.vkCmdWriteTimestamp2(commandBuffer, stage, queryPool, query)
def vkQueueSubmit2(queue, submitCount, pSubmits, fence):
    jvulkanLib.vkQueueSubmit2(queue, submitCount, pSubmits, fence)
def vkCmdCopyBuffer2(commandBuffer, pCopyBufferInfo):
    jvulkanLib.vkCmdCopyBuffer2(commandBuffer, pCopyBufferInfo)
def vkCmdCopyImage2(commandBuffer, pCopyImageInfo):
    jvulkanLib.vkCmdCopyImage2(commandBuffer, pCopyImageInfo)
def vkCmdCopyBufferToImage2(commandBuffer, pCopyBufferToImageInfo):
    jvulkanLib.vkCmdCopyBufferToImage2(commandBuffer, pCopyBufferToImageInfo)
def vkCmdCopyImageToBuffer2(commandBuffer, pCopyImageToBufferInfo):
    jvulkanLib.vkCmdCopyImageToBuffer2(commandBuffer, pCopyImageToBufferInfo)
def vkCmdBlitImage2(commandBuffer, pBlitImageInfo):
    jvulkanLib.vkCmdBlitImage2(commandBuffer, pBlitImageInfo)
def vkCmdResolveImage2(commandBuffer, pResolveImageInfo):
    jvulkanLib.vkCmdResolveImage2(commandBuffer, pResolveImageInfo)
def vkCmdBeginRendering(commandBuffer, pRenderingInfo):
    jvulkanLib.vkCmdBeginRendering(commandBuffer, pRenderingInfo)
def vkCmdEndRendering(commandBuffer):
    jvulkanLib.vkCmdEndRendering(commandBuffer)
def vkCmdSetCullMode(commandBuffer, cullMode):
    jvulkanLib.vkCmdSetCullMode(commandBuffer, cullMode)
def vkCmdSetFrontFace(commandBuffer, frontFace):
    jvulkanLib.vkCmdSetFrontFace(commandBuffer, frontFace)
def vkCmdSetPrimitiveTopology(commandBuffer, primitiveTopology):
    jvulkanLib.vkCmdSetPrimitiveTopology(commandBuffer, primitiveTopology)
def vkCmdSetViewportWithCount(commandBuffer, viewportCount, pViewports):
    jvulkanLib.vkCmdSetViewportWithCount(commandBuffer, viewportCount, pViewports)
def vkCmdSetScissorWithCount(commandBuffer, scissorCount, pScissors):
    jvulkanLib.vkCmdSetScissorWithCount(commandBuffer, scissorCount, pScissors)
def vkCmdBindVertexBuffers2(commandBuffer, firstBinding, bindingCount, pBuffers, pOffsets, pSizes, pStrides):
    jvulkanLib.vkCmdBindVertexBuffers2(commandBuffer, firstBinding, bindingCount, pBuffers, pOffsets, pSizes, pStrides)
def vkCmdSetDepthTestEnable(commandBuffer, depthTestEnable):
    jvulkanLib.vkCmdSetDepthTestEnable(commandBuffer, depthTestEnable)
def vkCmdSetDepthWriteEnable(commandBuffer, depthWriteEnable):
    jvulkanLib.vkCmdSetDepthWriteEnable(commandBuffer, depthWriteEnable)
def vkCmdSetDepthCompareOp(commandBuffer, depthCompareOp):
    jvulkanLib.vkCmdSetDepthCompareOp(commandBuffer, depthCompareOp)
def vkCmdSetDepthBoundsTestEnable(commandBuffer, depthBoundsTestEnable):
    jvulkanLib.vkCmdSetDepthBoundsTestEnable(commandBuffer, depthBoundsTestEnable)
def vkCmdSetStencilTestEnable(commandBuffer, stencilTestEnable):
    jvulkanLib.vkCmdSetStencilTestEnable(commandBuffer, stencilTestEnable)
def vkCmdSetStencilOp(commandBuffer, faceMask, failOp, passOp, depthFailOp, compareOp):
    jvulkanLib.vkCmdSetStencilOp(commandBuffer, faceMask, failOp, passOp, depthFailOp, compareOp)
def vkCmdSetRasterizerDiscardEnable(commandBuffer, rasterizerDiscardEnable):
    jvulkanLib.vkCmdSetRasterizerDiscardEnable(commandBuffer, rasterizerDiscardEnable)
def vkCmdSetDepthBiasEnable(commandBuffer, depthBiasEnable):
    jvulkanLib.vkCmdSetDepthBiasEnable(commandBuffer, depthBiasEnable)
def vkCmdSetPrimitiveRestartEnable(commandBuffer, primitiveRestartEnable):
    jvulkanLib.vkCmdSetPrimitiveRestartEnable(commandBuffer, primitiveRestartEnable)
def vkGetDeviceBufferMemoryRequirements(device, pInfo, pMemoryRequirements):
    jvulkanLib.vkGetDeviceBufferMemoryRequirements(device, pInfo, pMemoryRequirements)
def vkGetDeviceImageMemoryRequirements(device, pInfo, pMemoryRequirements):
    jvulkanLib.vkGetDeviceImageMemoryRequirements(device, pInfo, pMemoryRequirements)
def vkGetDeviceImageSparseMemoryRequirements(device, pInfo, pSparseMemoryRequirementCount, pSparseMemoryRequirements):
    jvulkanLib.vkGetDeviceImageSparseMemoryRequirements(device, pInfo, pSparseMemoryRequirementCount, pSparseMemoryRequirements)
def vkDestroySurfaceKHR(instance, surface, pAllocator):
    jvulkanLib.vkDestroySurfaceKHR(instance, surface, pAllocator)
def vkGetPhysicalDeviceSurfaceSupportKHR(physicalDevice, queueFamilyIndex, surface, pSupported):
    jvulkanLib.vkGetPhysicalDeviceSurfaceSupportKHR(physicalDevice, queueFamilyIndex, surface, pSupported)
def vkGetPhysicalDeviceSurfaceCapabilitiesKHR(physicalDevice, surface, pSurfaceCapabilities):
    jvulkanLib.vkGetPhysicalDeviceSurfaceCapabilitiesKHR(physicalDevice, surface, pSurfaceCapabilities)
def vkGetPhysicalDeviceSurfaceFormatsKHR(physicalDevice, surface, pSurfaceFormatCount, pSurfaceFormats):
    jvulkanLib.vkGetPhysicalDeviceSurfaceFormatsKHR(physicalDevice, surface, pSurfaceFormatCount, pSurfaceFormats)
def vkGetPhysicalDeviceSurfacePresentModesKHR(physicalDevice, surface, pPresentModeCount, pPresentModes):
    jvulkanLib.vkGetPhysicalDeviceSurfacePresentModesKHR(physicalDevice, surface, pPresentModeCount, pPresentModes)
def vkCreateSwapchainKHR(device, pCreateInfo, pAllocator, pSwapchain):
    jvulkanLib.vkCreateSwapchainKHR(device, pCreateInfo, pAllocator, pSwapchain)
def vkDestroySwapchainKHR(device, swapchain, pAllocator):
    jvulkanLib.vkDestroySwapchainKHR(device, swapchain, pAllocator)
def vkGetSwapchainImagesKHR(device, swapchain, pSwapchainImageCount, pSwapchainImages):
    jvulkanLib.vkGetSwapchainImagesKHR(device, swapchain, pSwapchainImageCount, pSwapchainImages)
def vkAcquireNextImageKHR(device, swapchain, timeout, semaphore, fence, pImageIndex):
    jvulkanLib.vkAcquireNextImageKHR(device, swapchain, timeout, semaphore, fence, pImageIndex)
def vkQueuePresentKHR(queue, pPresentInfo):
    jvulkanLib.vkQueuePresentKHR(queue, pPresentInfo)
def vkGetDeviceGroupPresentCapabilitiesKHR(device, pDeviceGroupPresentCapabilities):
    jvulkanLib.vkGetDeviceGroupPresentCapabilitiesKHR(device, pDeviceGroupPresentCapabilities)
def vkGetDeviceGroupSurfacePresentModesKHR(device, surface, pModes):
    jvulkanLib.vkGetDeviceGroupSurfacePresentModesKHR(device, surface, pModes)
def vkGetPhysicalDevicePresentRectanglesKHR(physicalDevice, surface, pRectCount, pRects):
    jvulkanLib.vkGetPhysicalDevicePresentRectanglesKHR(physicalDevice, surface, pRectCount, pRects)
def vkAcquireNextImage2KHR(device, pAcquireInfo, pImageIndex):
    jvulkanLib.vkAcquireNextImage2KHR(device, pAcquireInfo, pImageIndex)
def vkGetPhysicalDeviceDisplayPropertiesKHR(physicalDevice, pPropertyCount, pProperties):
    jvulkanLib.vkGetPhysicalDeviceDisplayPropertiesKHR(physicalDevice, pPropertyCount, pProperties)
def vkGetPhysicalDeviceDisplayPlanePropertiesKHR(physicalDevice, pPropertyCount, pProperties):
    jvulkanLib.vkGetPhysicalDeviceDisplayPlanePropertiesKHR(physicalDevice, pPropertyCount, pProperties)
def vkGetDisplayPlaneSupportedDisplaysKHR(physicalDevice, planeIndex, pDisplayCount, pDisplays):
    jvulkanLib.vkGetDisplayPlaneSupportedDisplaysKHR(physicalDevice, planeIndex, pDisplayCount, pDisplays)
def vkGetDisplayModePropertiesKHR(physicalDevice, display, pPropertyCount, pProperties):
    jvulkanLib.vkGetDisplayModePropertiesKHR(physicalDevice, display, pPropertyCount, pProperties)
def vkCreateDisplayModeKHR(physicalDevice, display, pCreateInfo, pAllocator, pMode):
    jvulkanLib.vkCreateDisplayModeKHR(physicalDevice, display, pCreateInfo, pAllocator, pMode)
def vkGetDisplayPlaneCapabilitiesKHR(physicalDevice, mode, planeIndex, pCapabilities):
    jvulkanLib.vkGetDisplayPlaneCapabilitiesKHR(physicalDevice, mode, planeIndex, pCapabilities)
def vkCreateDisplayPlaneSurfaceKHR(instance, pCreateInfo, pAllocator, pSurface):
    jvulkanLib.vkCreateDisplayPlaneSurfaceKHR(instance, pCreateInfo, pAllocator, pSurface)
def vkCreateSharedSwapchainsKHR(device, swapchainCount, pCreateInfos, pAllocator, pSwapchains):
    jvulkanLib.vkCreateSharedSwapchainsKHR(device, swapchainCount, pCreateInfos, pAllocator, pSwapchains)
def vkCmdBeginRenderingKHR(commandBuffer, pRenderingInfo):
    jvulkanLib.vkCmdBeginRenderingKHR(commandBuffer, pRenderingInfo)
def vkCmdEndRenderingKHR(commandBuffer):
    jvulkanLib.vkCmdEndRenderingKHR(commandBuffer)
def vkGetPhysicalDeviceFeatures2KHR(physicalDevice, pFeatures):
    jvulkanLib.vkGetPhysicalDeviceFeatures2KHR(physicalDevice, pFeatures)
def vkGetPhysicalDeviceProperties2KHR(physicalDevice, pProperties):
    jvulkanLib.vkGetPhysicalDeviceProperties2KHR(physicalDevice, pProperties)
def vkGetPhysicalDeviceFormatProperties2KHR(physicalDevice, format, pFormatProperties):
    jvulkanLib.vkGetPhysicalDeviceFormatProperties2KHR(physicalDevice, format, pFormatProperties)
def vkGetPhysicalDeviceImageFormatProperties2KHR(physicalDevice, pImageFormatInfo, pImageFormatProperties):
    jvulkanLib.vkGetPhysicalDeviceImageFormatProperties2KHR(physicalDevice, pImageFormatInfo, pImageFormatProperties)
def vkGetPhysicalDeviceQueueFamilyProperties2KHR(physicalDevice, pQueueFamilyPropertyCount, pQueueFamilyProperties):
    jvulkanLib.vkGetPhysicalDeviceQueueFamilyProperties2KHR(physicalDevice, pQueueFamilyPropertyCount, pQueueFamilyProperties)
def vkGetPhysicalDeviceMemoryProperties2KHR(physicalDevice, pMemoryProperties):
    jvulkanLib.vkGetPhysicalDeviceMemoryProperties2KHR(physicalDevice, pMemoryProperties)
def vkGetPhysicalDeviceSparseImageFormatProperties2KHR(physicalDevice, pFormatInfo, pPropertyCount, pProperties):
    jvulkanLib.vkGetPhysicalDeviceSparseImageFormatProperties2KHR(physicalDevice, pFormatInfo, pPropertyCount, pProperties)
def vkGetDeviceGroupPeerMemoryFeaturesKHR(device, heapIndex, localDeviceIndex, remoteDeviceIndex, pPeerMemoryFeatures):
    jvulkanLib.vkGetDeviceGroupPeerMemoryFeaturesKHR(device, heapIndex, localDeviceIndex, remoteDeviceIndex, pPeerMemoryFeatures)
def vkCmdSetDeviceMaskKHR(commandBuffer, deviceMask):
    jvulkanLib.vkCmdSetDeviceMaskKHR(commandBuffer, deviceMask)
def vkCmdDispatchBaseKHR(commandBuffer, baseGroupX, baseGroupY, baseGroupZ, groupCountX, groupCountY, groupCountZ):
    jvulkanLib.vkCmdDispatchBaseKHR(commandBuffer, baseGroupX, baseGroupY, baseGroupZ, groupCountX, groupCountY, groupCountZ)
def vkTrimCommandPoolKHR(device, commandPool, flags):
    jvulkanLib.vkTrimCommandPoolKHR(device, commandPool, flags)
def vkEnumeratePhysicalDeviceGroupsKHR(instance, pPhysicalDeviceGroupCount, pPhysicalDeviceGroupProperties):
    jvulkanLib.vkEnumeratePhysicalDeviceGroupsKHR(instance, pPhysicalDeviceGroupCount, pPhysicalDeviceGroupProperties)
def vkGetPhysicalDeviceExternalBufferPropertiesKHR(physicalDevice, pExternalBufferInfo, pExternalBufferProperties):
    jvulkanLib.vkGetPhysicalDeviceExternalBufferPropertiesKHR(physicalDevice, pExternalBufferInfo, pExternalBufferProperties)
def vkGetMemoryFdKHR(device, pGetFdInfo, pFd):
    jvulkanLib.vkGetMemoryFdKHR(device, pGetFdInfo, pFd)
def vkGetMemoryFdPropertiesKHR(device, handleType, fd, pMemoryFdProperties):
    jvulkanLib.vkGetMemoryFdPropertiesKHR(device, handleType, fd, pMemoryFdProperties)
def vkGetPhysicalDeviceExternalSemaphorePropertiesKHR(physicalDevice, pExternalSemaphoreInfo, pExternalSemaphoreProperties):
    jvulkanLib.vkGetPhysicalDeviceExternalSemaphorePropertiesKHR(physicalDevice, pExternalSemaphoreInfo, pExternalSemaphoreProperties)
def vkImportSemaphoreFdKHR(device, pImportSemaphoreFdInfo):
    jvulkanLib.vkImportSemaphoreFdKHR(device, pImportSemaphoreFdInfo)
def vkGetSemaphoreFdKHR(device, pGetFdInfo, pFd):
    jvulkanLib.vkGetSemaphoreFdKHR(device, pGetFdInfo, pFd)
def vkCmdPushDescriptorSetKHR(commandBuffer, pipelineBindPoint, layout, set, descriptorWriteCount, pDescriptorWrites):
    jvulkanLib.vkCmdPushDescriptorSetKHR(commandBuffer, pipelineBindPoint, layout, set, descriptorWriteCount, pDescriptorWrites)
def vkCmdPushDescriptorSetWithTemplateKHR(commandBuffer, descriptorUpdateTemplate, layout, set, pData):
    jvulkanLib.vkCmdPushDescriptorSetWithTemplateKHR(commandBuffer, descriptorUpdateTemplate, layout, set, pData)
def vkCreateDescriptorUpdateTemplateKHR(device, pCreateInfo, pAllocator, pDescriptorUpdateTemplate):
    jvulkanLib.vkCreateDescriptorUpdateTemplateKHR(device, pCreateInfo, pAllocator, pDescriptorUpdateTemplate)
def vkDestroyDescriptorUpdateTemplateKHR(device, descriptorUpdateTemplate, pAllocator):
    jvulkanLib.vkDestroyDescriptorUpdateTemplateKHR(device, descriptorUpdateTemplate, pAllocator)
def vkUpdateDescriptorSetWithTemplateKHR(device, descriptorSet, descriptorUpdateTemplate, pData):
    jvulkanLib.vkUpdateDescriptorSetWithTemplateKHR(device, descriptorSet, descriptorUpdateTemplate, pData)
def vkCreateRenderPass2KHR(device, pCreateInfo, pAllocator, pRenderPass):
    jvulkanLib.vkCreateRenderPass2KHR(device, pCreateInfo, pAllocator, pRenderPass)
def vkCmdBeginRenderPass2KHR(commandBuffer, pRenderPassBegin, pSubpassBeginInfo):
    jvulkanLib.vkCmdBeginRenderPass2KHR(commandBuffer, pRenderPassBegin, pSubpassBeginInfo)
def vkCmdNextSubpass2KHR(commandBuffer, pSubpassBeginInfo, pSubpassEndInfo):
    jvulkanLib.vkCmdNextSubpass2KHR(commandBuffer, pSubpassBeginInfo, pSubpassEndInfo)
def vkCmdEndRenderPass2KHR(commandBuffer, pSubpassEndInfo):
    jvulkanLib.vkCmdEndRenderPass2KHR(commandBuffer, pSubpassEndInfo)
def vkGetSwapchainStatusKHR(device, swapchain):
    jvulkanLib.vkGetSwapchainStatusKHR(device, swapchain)
def vkGetPhysicalDeviceExternalFencePropertiesKHR(physicalDevice, pExternalFenceInfo, pExternalFenceProperties):
    jvulkanLib.vkGetPhysicalDeviceExternalFencePropertiesKHR(physicalDevice, pExternalFenceInfo, pExternalFenceProperties)
def vkImportFenceFdKHR(device, pImportFenceFdInfo):
    jvulkanLib.vkImportFenceFdKHR(device, pImportFenceFdInfo)
def vkGetFenceFdKHR(device, pGetFdInfo, pFd):
    jvulkanLib.vkGetFenceFdKHR(device, pGetFdInfo, pFd)
def vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR(physicalDevice, queueFamilyIndex, pCounterCount, pCounters, pCounterDescriptions):
    jvulkanLib.vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR(physicalDevice, queueFamilyIndex, pCounterCount, pCounters, pCounterDescriptions)
def vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR(physicalDevice, pPerformanceQueryCreateInfo, pNumPasses):
    jvulkanLib.vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR(physicalDevice, pPerformanceQueryCreateInfo, pNumPasses)
def vkAcquireProfilingLockKHR(device, pInfo):
    jvulkanLib.vkAcquireProfilingLockKHR(device, pInfo)
def vkReleaseProfilingLockKHR(device):
    jvulkanLib.vkReleaseProfilingLockKHR(device)
def vkGetPhysicalDeviceSurfaceCapabilities2KHR(physicalDevice, pSurfaceInfo, pSurfaceCapabilities):
    jvulkanLib.vkGetPhysicalDeviceSurfaceCapabilities2KHR(physicalDevice, pSurfaceInfo, pSurfaceCapabilities)
def vkGetPhysicalDeviceSurfaceFormats2KHR(physicalDevice, pSurfaceInfo, pSurfaceFormatCount, pSurfaceFormats):
    jvulkanLib.vkGetPhysicalDeviceSurfaceFormats2KHR(physicalDevice, pSurfaceInfo, pSurfaceFormatCount, pSurfaceFormats)
def vkGetPhysicalDeviceDisplayProperties2KHR(physicalDevice, pPropertyCount, pProperties):
    jvulkanLib.vkGetPhysicalDeviceDisplayProperties2KHR(physicalDevice, pPropertyCount, pProperties)
def vkGetPhysicalDeviceDisplayPlaneProperties2KHR(physicalDevice, pPropertyCount, pProperties):
    jvulkanLib.vkGetPhysicalDeviceDisplayPlaneProperties2KHR(physicalDevice, pPropertyCount, pProperties)
def vkGetDisplayModeProperties2KHR(physicalDevice, display, pPropertyCount, pProperties):
    jvulkanLib.vkGetDisplayModeProperties2KHR(physicalDevice, display, pPropertyCount, pProperties)
def vkGetDisplayPlaneCapabilities2KHR(physicalDevice, pDisplayPlaneInfo, pCapabilities):
    jvulkanLib.vkGetDisplayPlaneCapabilities2KHR(physicalDevice, pDisplayPlaneInfo, pCapabilities)
def vkGetImageMemoryRequirements2KHR(device, pInfo, pMemoryRequirements):
    jvulkanLib.vkGetImageMemoryRequirements2KHR(device, pInfo, pMemoryRequirements)
def vkGetBufferMemoryRequirements2KHR(device, pInfo, pMemoryRequirements):
    jvulkanLib.vkGetBufferMemoryRequirements2KHR(device, pInfo, pMemoryRequirements)
def vkGetImageSparseMemoryRequirements2KHR(device, pInfo, pSparseMemoryRequirementCount, pSparseMemoryRequirements):
    jvulkanLib.vkGetImageSparseMemoryRequirements2KHR(device, pInfo, pSparseMemoryRequirementCount, pSparseMemoryRequirements)
def vkCreateSamplerYcbcrConversionKHR(device, pCreateInfo, pAllocator, pYcbcrConversion):
    jvulkanLib.vkCreateSamplerYcbcrConversionKHR(device, pCreateInfo, pAllocator, pYcbcrConversion)
def vkDestroySamplerYcbcrConversionKHR(device, ycbcrConversion, pAllocator):
    jvulkanLib.vkDestroySamplerYcbcrConversionKHR(device, ycbcrConversion, pAllocator)
def vkBindBufferMemory2KHR(device, bindInfoCount, pBindInfos):
    jvulkanLib.vkBindBufferMemory2KHR(device, bindInfoCount, pBindInfos)
def vkBindImageMemory2KHR(device, bindInfoCount, pBindInfos):
    jvulkanLib.vkBindImageMemory2KHR(device, bindInfoCount, pBindInfos)
def vkGetDescriptorSetLayoutSupportKHR(device, pCreateInfo, pSupport):
    jvulkanLib.vkGetDescriptorSetLayoutSupportKHR(device, pCreateInfo, pSupport)
def vkCmdDrawIndirectCountKHR(commandBuffer, buffer, offset, countBuffer, countBufferOffset, maxDrawCount, stride):
    jvulkanLib.vkCmdDrawIndirectCountKHR(commandBuffer, buffer, offset, countBuffer, countBufferOffset, maxDrawCount, stride)
def vkCmdDrawIndexedIndirectCountKHR(commandBuffer, buffer, offset, countBuffer, countBufferOffset, maxDrawCount, stride):
    jvulkanLib.vkCmdDrawIndexedIndirectCountKHR(commandBuffer, buffer, offset, countBuffer, countBufferOffset, maxDrawCount, stride)
def vkGetSemaphoreCounterValueKHR(device, semaphore, pValue):
    jvulkanLib.vkGetSemaphoreCounterValueKHR(device, semaphore, pValue)
def vkWaitSemaphoresKHR(device, pWaitInfo, timeout):
    jvulkanLib.vkWaitSemaphoresKHR(device, pWaitInfo, timeout)
def vkSignalSemaphoreKHR(device, pSignalInfo):
    jvulkanLib.vkSignalSemaphoreKHR(device, pSignalInfo)
def vkGetPhysicalDeviceFragmentShadingRatesKHR(physicalDevice, pFragmentShadingRateCount, pFragmentShadingRates):
    jvulkanLib.vkGetPhysicalDeviceFragmentShadingRatesKHR(physicalDevice, pFragmentShadingRateCount, pFragmentShadingRates)
def vkCmdSetFragmentShadingRateKHR(commandBuffer, pFragmentSize, combinerOps):
    jvulkanLib.vkCmdSetFragmentShadingRateKHR(commandBuffer, pFragmentSize, combinerOps)
def vkWaitForPresentKHR(device, swapchain, presentId, timeout):
    jvulkanLib.vkWaitForPresentKHR(device, swapchain, presentId, timeout)
def vkGetBufferDeviceAddressKHR(device, pInfo):
    jvulkanLib.vkGetBufferDeviceAddressKHR(device, pInfo)
def vkGetBufferOpaqueCaptureAddressKHR(device, pInfo):
    jvulkanLib.vkGetBufferOpaqueCaptureAddressKHR(device, pInfo)
def vkGetDeviceMemoryOpaqueCaptureAddressKHR(device, pInfo):
    jvulkanLib.vkGetDeviceMemoryOpaqueCaptureAddressKHR(device, pInfo)
def vkCreateDeferredOperationKHR(device, pAllocator, pDeferredOperation):
    jvulkanLib.vkCreateDeferredOperationKHR(device, pAllocator, pDeferredOperation)
def vkDestroyDeferredOperationKHR(device, operation, pAllocator):
    jvulkanLib.vkDestroyDeferredOperationKHR(device, operation, pAllocator)
def vkGetDeferredOperationMaxConcurrencyKHR(device, operation):
    jvulkanLib.vkGetDeferredOperationMaxConcurrencyKHR(device, operation)
def vkGetDeferredOperationResultKHR(device, operation):
    jvulkanLib.vkGetDeferredOperationResultKHR(device, operation)
def vkDeferredOperationJoinKHR(device, operation):
    jvulkanLib.vkDeferredOperationJoinKHR(device, operation)
def vkGetPipelineExecutablePropertiesKHR(device, pPipelineInfo, pExecutableCount, pProperties):
    jvulkanLib.vkGetPipelineExecutablePropertiesKHR(device, pPipelineInfo, pExecutableCount, pProperties)
def vkGetPipelineExecutableStatisticsKHR(device, pExecutableInfo, pStatisticCount, pStatistics):
    jvulkanLib.vkGetPipelineExecutableStatisticsKHR(device, pExecutableInfo, pStatisticCount, pStatistics)
def vkGetPipelineExecutableInternalRepresentationsKHR(device, pExecutableInfo, pInternalRepresentationCount, pInternalRepresentations):
    jvulkanLib.vkGetPipelineExecutableInternalRepresentationsKHR(device, pExecutableInfo, pInternalRepresentationCount, pInternalRepresentations)
def vkCmdSetEvent2KHR(commandBuffer, event, pDependencyInfo):
    jvulkanLib.vkCmdSetEvent2KHR(commandBuffer, event, pDependencyInfo)
def vkCmdResetEvent2KHR(commandBuffer, event, stageMask):
    jvulkanLib.vkCmdResetEvent2KHR(commandBuffer, event, stageMask)
def vkCmdWaitEvents2KHR(commandBuffer, eventCount, pEvents, pDependencyInfos):
    jvulkanLib.vkCmdWaitEvents2KHR(commandBuffer, eventCount, pEvents, pDependencyInfos)
def vkCmdPipelineBarrier2KHR(commandBuffer, pDependencyInfo):
    jvulkanLib.vkCmdPipelineBarrier2KHR(commandBuffer, pDependencyInfo)
def vkCmdWriteTimestamp2KHR(commandBuffer, stage, queryPool, query):
    jvulkanLib.vkCmdWriteTimestamp2KHR(commandBuffer, stage, queryPool, query)
def vkQueueSubmit2KHR(queue, submitCount, pSubmits, fence):
    jvulkanLib.vkQueueSubmit2KHR(queue, submitCount, pSubmits, fence)
def vkCmdWriteBufferMarker2AMD(commandBuffer, stage, dstBuffer, dstOffset, marker):
    jvulkanLib.vkCmdWriteBufferMarker2AMD(commandBuffer, stage, dstBuffer, dstOffset, marker)
def vkGetQueueCheckpointData2NV(queue, pCheckpointDataCount, pCheckpointData):
    jvulkanLib.vkGetQueueCheckpointData2NV(queue, pCheckpointDataCount, pCheckpointData)
def vkCmdCopyBuffer2KHR(commandBuffer, pCopyBufferInfo):
    jvulkanLib.vkCmdCopyBuffer2KHR(commandBuffer, pCopyBufferInfo)
def vkCmdCopyImage2KHR(commandBuffer, pCopyImageInfo):
    jvulkanLib.vkCmdCopyImage2KHR(commandBuffer, pCopyImageInfo)
def vkCmdCopyBufferToImage2KHR(commandBuffer, pCopyBufferToImageInfo):
    jvulkanLib.vkCmdCopyBufferToImage2KHR(commandBuffer, pCopyBufferToImageInfo)
def vkCmdCopyImageToBuffer2KHR(commandBuffer, pCopyImageToBufferInfo):
    jvulkanLib.vkCmdCopyImageToBuffer2KHR(commandBuffer, pCopyImageToBufferInfo)
def vkCmdBlitImage2KHR(commandBuffer, pBlitImageInfo):
    jvulkanLib.vkCmdBlitImage2KHR(commandBuffer, pBlitImageInfo)
def vkCmdResolveImage2KHR(commandBuffer, pResolveImageInfo):
    jvulkanLib.vkCmdResolveImage2KHR(commandBuffer, pResolveImageInfo)
def vkGetDeviceBufferMemoryRequirementsKHR(device, pInfo, pMemoryRequirements):
    jvulkanLib.vkGetDeviceBufferMemoryRequirementsKHR(device, pInfo, pMemoryRequirements)
def vkGetDeviceImageMemoryRequirementsKHR(device, pInfo, pMemoryRequirements):
    jvulkanLib.vkGetDeviceImageMemoryRequirementsKHR(device, pInfo, pMemoryRequirements)
def vkGetDeviceImageSparseMemoryRequirementsKHR(device, pInfo, pSparseMemoryRequirementCount, pSparseMemoryRequirements):
    jvulkanLib.vkGetDeviceImageSparseMemoryRequirementsKHR(device, pInfo, pSparseMemoryRequirementCount, pSparseMemoryRequirements)
def vkCreateDebugReportCallbackEXT(instance, pCreateInfo, pAllocator, pCallback):
    jvulkanLib.vkCreateDebugReportCallbackEXT(instance, pCreateInfo, pAllocator, pCallback)
def vkDestroyDebugReportCallbackEXT(instance, callback, pAllocator):
    jvulkanLib.vkDestroyDebugReportCallbackEXT(instance, callback, pAllocator)
def vkDebugReportMessageEXT(instance, flags, objectType, object, location, messageCode, pLayerPrefix, pMessage):
    jvulkanLib.vkDebugReportMessageEXT(instance, flags, objectType, object, location, messageCode, pLayerPrefix, pMessage)
def vkDebugMarkerSetObjectTagEXT(device, pTagInfo):
    jvulkanLib.vkDebugMarkerSetObjectTagEXT(device, pTagInfo)
def vkDebugMarkerSetObjectNameEXT(device, pNameInfo):
    jvulkanLib.vkDebugMarkerSetObjectNameEXT(device, pNameInfo)
def vkCmdDebugMarkerBeginEXT(commandBuffer, pMarkerInfo):
    jvulkanLib.vkCmdDebugMarkerBeginEXT(commandBuffer, pMarkerInfo)
def vkCmdDebugMarkerEndEXT(commandBuffer):
    jvulkanLib.vkCmdDebugMarkerEndEXT(commandBuffer)
def vkCmdDebugMarkerInsertEXT(commandBuffer, pMarkerInfo):
    jvulkanLib.vkCmdDebugMarkerInsertEXT(commandBuffer, pMarkerInfo)
def vkCmdBindTransformFeedbackBuffersEXT(commandBuffer, firstBinding, bindingCount, pBuffers, pOffsets, pSizes):
    jvulkanLib.vkCmdBindTransformFeedbackBuffersEXT(commandBuffer, firstBinding, bindingCount, pBuffers, pOffsets, pSizes)
def vkCmdBeginTransformFeedbackEXT(commandBuffer, firstCounterBuffer, counterBufferCount, pCounterBuffers, pCounterBufferOffsets):
    jvulkanLib.vkCmdBeginTransformFeedbackEXT(commandBuffer, firstCounterBuffer, counterBufferCount, pCounterBuffers, pCounterBufferOffsets)
def vkCmdEndTransformFeedbackEXT(commandBuffer, firstCounterBuffer, counterBufferCount, pCounterBuffers, pCounterBufferOffsets):
    jvulkanLib.vkCmdEndTransformFeedbackEXT(commandBuffer, firstCounterBuffer, counterBufferCount, pCounterBuffers, pCounterBufferOffsets)
def vkCmdBeginQueryIndexedEXT(commandBuffer, queryPool, query, flags, index):
    jvulkanLib.vkCmdBeginQueryIndexedEXT(commandBuffer, queryPool, query, flags, index)
def vkCmdEndQueryIndexedEXT(commandBuffer, queryPool, query, index):
    jvulkanLib.vkCmdEndQueryIndexedEXT(commandBuffer, queryPool, query, index)
def vkCmdDrawIndirectByteCountEXT(commandBuffer, instanceCount, firstInstance, counterBuffer, counterBufferOffset, counterOffset, vertexStride):
    jvulkanLib.vkCmdDrawIndirectByteCountEXT(commandBuffer, instanceCount, firstInstance, counterBuffer, counterBufferOffset, counterOffset, vertexStride)
def vkCreateCuModuleNVX(device, pCreateInfo, pAllocator, pModule):
    jvulkanLib.vkCreateCuModuleNVX(device, pCreateInfo, pAllocator, pModule)
def vkCreateCuFunctionNVX(device, pCreateInfo, pAllocator, pFunction):
    jvulkanLib.vkCreateCuFunctionNVX(device, pCreateInfo, pAllocator, pFunction)
def vkDestroyCuModuleNVX(device, module, pAllocator):
    jvulkanLib.vkDestroyCuModuleNVX(device, module, pAllocator)
def vkDestroyCuFunctionNVX(device, function, pAllocator):
    jvulkanLib.vkDestroyCuFunctionNVX(device, function, pAllocator)
def vkCmdCuLaunchKernelNVX(commandBuffer, pLaunchInfo):
    jvulkanLib.vkCmdCuLaunchKernelNVX(commandBuffer, pLaunchInfo)
def vkGetImageViewHandleNVX(device, pInfo):
    jvulkanLib.vkGetImageViewHandleNVX(device, pInfo)
def vkGetImageViewAddressNVX(device, imageView, pProperties):
    jvulkanLib.vkGetImageViewAddressNVX(device, imageView, pProperties)
def vkCmdDrawIndirectCountAMD(commandBuffer, buffer, offset, countBuffer, countBufferOffset, maxDrawCount, stride):
    jvulkanLib.vkCmdDrawIndirectCountAMD(commandBuffer, buffer, offset, countBuffer, countBufferOffset, maxDrawCount, stride)
def vkCmdDrawIndexedIndirectCountAMD(commandBuffer, buffer, offset, countBuffer, countBufferOffset, maxDrawCount, stride):
    jvulkanLib.vkCmdDrawIndexedIndirectCountAMD(commandBuffer, buffer, offset, countBuffer, countBufferOffset, maxDrawCount, stride)
def vkGetShaderInfoAMD(device, pipeline, shaderStage, infoType, pInfoSize, pInfo):
    jvulkanLib.vkGetShaderInfoAMD(device, pipeline, shaderStage, infoType, pInfoSize, pInfo)
def vkGetPhysicalDeviceExternalImageFormatPropertiesNV(physicalDevice, format, type, tiling, usage, flags, externalHandleType, pExternalImageFormatProperties):
    jvulkanLib.vkGetPhysicalDeviceExternalImageFormatPropertiesNV(physicalDevice, format, type, tiling, usage, flags, externalHandleType, pExternalImageFormatProperties)
def vkCmdBeginConditionalRenderingEXT(commandBuffer, pConditionalRenderingBegin):
    jvulkanLib.vkCmdBeginConditionalRenderingEXT(commandBuffer, pConditionalRenderingBegin)
def vkCmdEndConditionalRenderingEXT(commandBuffer):
    jvulkanLib.vkCmdEndConditionalRenderingEXT(commandBuffer)
def vkCmdSetViewportWScalingNV(commandBuffer, firstViewport, viewportCount, pViewportWScalings):
    jvulkanLib.vkCmdSetViewportWScalingNV(commandBuffer, firstViewport, viewportCount, pViewportWScalings)
def vkReleaseDisplayEXT(physicalDevice, display):
    jvulkanLib.vkReleaseDisplayEXT(physicalDevice, display)
def vkGetPhysicalDeviceSurfaceCapabilities2EXT(physicalDevice, surface, pSurfaceCapabilities):
    jvulkanLib.vkGetPhysicalDeviceSurfaceCapabilities2EXT(physicalDevice, surface, pSurfaceCapabilities)
def vkDisplayPowerControlEXT(device, display, pDisplayPowerInfo):
    jvulkanLib.vkDisplayPowerControlEXT(device, display, pDisplayPowerInfo)
def vkRegisterDeviceEventEXT(device, pDeviceEventInfo, pAllocator, pFence):
    jvulkanLib.vkRegisterDeviceEventEXT(device, pDeviceEventInfo, pAllocator, pFence)
def vkRegisterDisplayEventEXT(device, display, pDisplayEventInfo, pAllocator, pFence):
    jvulkanLib.vkRegisterDisplayEventEXT(device, display, pDisplayEventInfo, pAllocator, pFence)
def vkGetSwapchainCounterEXT(device, swapchain, counter, pCounterValue):
    jvulkanLib.vkGetSwapchainCounterEXT(device, swapchain, counter, pCounterValue)
def vkGetRefreshCycleDurationGOOGLE(device, swapchain, pDisplayTimingProperties):
    jvulkanLib.vkGetRefreshCycleDurationGOOGLE(device, swapchain, pDisplayTimingProperties)
def vkGetPastPresentationTimingGOOGLE(device, swapchain, pPresentationTimingCount, pPresentationTimings):
    jvulkanLib.vkGetPastPresentationTimingGOOGLE(device, swapchain, pPresentationTimingCount, pPresentationTimings)
def vkCmdSetDiscardRectangleEXT(commandBuffer, firstDiscardRectangle, discardRectangleCount, pDiscardRectangles):
    jvulkanLib.vkCmdSetDiscardRectangleEXT(commandBuffer, firstDiscardRectangle, discardRectangleCount, pDiscardRectangles)
def vkSetHdrMetadataEXT(device, swapchainCount, pSwapchains, pMetadata):
    jvulkanLib.vkSetHdrMetadataEXT(device, swapchainCount, pSwapchains, pMetadata)
def vkSetDebugUtilsObjectNameEXT(device, pNameInfo):
    jvulkanLib.vkSetDebugUtilsObjectNameEXT(device, pNameInfo)
def vkSetDebugUtilsObjectTagEXT(device, pTagInfo):
    jvulkanLib.vkSetDebugUtilsObjectTagEXT(device, pTagInfo)
def vkQueueBeginDebugUtilsLabelEXT(queue, pLabelInfo):
    jvulkanLib.vkQueueBeginDebugUtilsLabelEXT(queue, pLabelInfo)
def vkQueueEndDebugUtilsLabelEXT(queue):
    jvulkanLib.vkQueueEndDebugUtilsLabelEXT(queue)
def vkQueueInsertDebugUtilsLabelEXT(queue, pLabelInfo):
    jvulkanLib.vkQueueInsertDebugUtilsLabelEXT(queue, pLabelInfo)
def vkCmdBeginDebugUtilsLabelEXT(commandBuffer, pLabelInfo):
    jvulkanLib.vkCmdBeginDebugUtilsLabelEXT(commandBuffer, pLabelInfo)
def vkCmdEndDebugUtilsLabelEXT(commandBuffer):
    jvulkanLib.vkCmdEndDebugUtilsLabelEXT(commandBuffer)
def vkCmdInsertDebugUtilsLabelEXT(commandBuffer, pLabelInfo):
    jvulkanLib.vkCmdInsertDebugUtilsLabelEXT(commandBuffer, pLabelInfo)
def vkCreateDebugUtilsMessengerEXT(instance, pCreateInfo, pAllocator, pMessenger):
    jvulkanLib.vkCreateDebugUtilsMessengerEXT(instance, pCreateInfo, pAllocator, pMessenger)
def vkDestroyDebugUtilsMessengerEXT(instance, messenger, pAllocator):
    jvulkanLib.vkDestroyDebugUtilsMessengerEXT(instance, messenger, pAllocator)
def vkSubmitDebugUtilsMessageEXT(instance, messageSeverity, messageTypes, pCallbackData):
    jvulkanLib.vkSubmitDebugUtilsMessageEXT(instance, messageSeverity, messageTypes, pCallbackData)
def vkCmdSetSampleLocationsEXT(commandBuffer, pSampleLocationsInfo):
    jvulkanLib.vkCmdSetSampleLocationsEXT(commandBuffer, pSampleLocationsInfo)
def vkGetPhysicalDeviceMultisamplePropertiesEXT(physicalDevice, samples, pMultisampleProperties):
    jvulkanLib.vkGetPhysicalDeviceMultisamplePropertiesEXT(physicalDevice, samples, pMultisampleProperties)
def vkGetImageDrmFormatModifierPropertiesEXT(device, image, pProperties):
    jvulkanLib.vkGetImageDrmFormatModifierPropertiesEXT(device, image, pProperties)
def vkCreateValidationCacheEXT(device, pCreateInfo, pAllocator, pValidationCache):
    jvulkanLib.vkCreateValidationCacheEXT(device, pCreateInfo, pAllocator, pValidationCache)
def vkDestroyValidationCacheEXT(device, validationCache, pAllocator):
    jvulkanLib.vkDestroyValidationCacheEXT(device, validationCache, pAllocator)
def vkMergeValidationCachesEXT(device, dstCache, srcCacheCount, pSrcCaches):
    jvulkanLib.vkMergeValidationCachesEXT(device, dstCache, srcCacheCount, pSrcCaches)
def vkGetValidationCacheDataEXT(device, validationCache, pDataSize, pData):
    jvulkanLib.vkGetValidationCacheDataEXT(device, validationCache, pDataSize, pData)
def vkCmdBindShadingRateImageNV(commandBuffer, imageView, imageLayout):
    jvulkanLib.vkCmdBindShadingRateImageNV(commandBuffer, imageView, imageLayout)
def vkCmdSetViewportShadingRatePaletteNV(commandBuffer, firstViewport, viewportCount, pShadingRatePalettes):
    jvulkanLib.vkCmdSetViewportShadingRatePaletteNV(commandBuffer, firstViewport, viewportCount, pShadingRatePalettes)
def vkCmdSetCoarseSampleOrderNV(commandBuffer, sampleOrderType, customSampleOrderCount, pCustomSampleOrders):
    jvulkanLib.vkCmdSetCoarseSampleOrderNV(commandBuffer, sampleOrderType, customSampleOrderCount, pCustomSampleOrders)
def vkCreateAccelerationStructureNV(device, pCreateInfo, pAllocator, pAccelerationStructure):
    jvulkanLib.vkCreateAccelerationStructureNV(device, pCreateInfo, pAllocator, pAccelerationStructure)
def vkDestroyAccelerationStructureNV(device, accelerationStructure, pAllocator):
    jvulkanLib.vkDestroyAccelerationStructureNV(device, accelerationStructure, pAllocator)
def vkGetAccelerationStructureMemoryRequirementsNV(device, pInfo, pMemoryRequirements):
    jvulkanLib.vkGetAccelerationStructureMemoryRequirementsNV(device, pInfo, pMemoryRequirements)
def vkBindAccelerationStructureMemoryNV(device, bindInfoCount, pBindInfos):
    jvulkanLib.vkBindAccelerationStructureMemoryNV(device, bindInfoCount, pBindInfos)
def vkCmdBuildAccelerationStructureNV(commandBuffer, pInfo, instanceData, instanceOffset, update, dst, src, scratch, scratchOffset):
    jvulkanLib.vkCmdBuildAccelerationStructureNV(commandBuffer, pInfo, instanceData, instanceOffset, update, dst, src, scratch, scratchOffset)
def vkCmdCopyAccelerationStructureNV(commandBuffer, dst, src, mode):
    jvulkanLib.vkCmdCopyAccelerationStructureNV(commandBuffer, dst, src, mode)
def vkCmdTraceRaysNV(commandBuffer, raygenShaderBindingTableBuffer, raygenShaderBindingOffset, missShaderBindingTableBuffer, missShaderBindingOffset, missShaderBindingStride, hitShaderBindingTableBuffer, hitShaderBindingOffset, hitShaderBindingStride, callableShaderBindingTableBuffer, callableShaderBindingOffset, callableShaderBindingStride, width, height, depth):
    jvulkanLib.vkCmdTraceRaysNV(commandBuffer, raygenShaderBindingTableBuffer, raygenShaderBindingOffset, missShaderBindingTableBuffer, missShaderBindingOffset, missShaderBindingStride, hitShaderBindingTableBuffer, hitShaderBindingOffset, hitShaderBindingStride, callableShaderBindingTableBuffer, callableShaderBindingOffset, callableShaderBindingStride, width, height, depth)
def vkCreateRayTracingPipelinesNV(device, pipelineCache, createInfoCount, pCreateInfos, pAllocator, pPipelines):
    jvulkanLib.vkCreateRayTracingPipelinesNV(device, pipelineCache, createInfoCount, pCreateInfos, pAllocator, pPipelines)
def vkGetRayTracingShaderGroupHandlesKHR(device, pipeline, firstGroup, groupCount, dataSize, pData):
    jvulkanLib.vkGetRayTracingShaderGroupHandlesKHR(device, pipeline, firstGroup, groupCount, dataSize, pData)
def vkGetRayTracingShaderGroupHandlesNV(device, pipeline, firstGroup, groupCount, dataSize, pData):
    jvulkanLib.vkGetRayTracingShaderGroupHandlesNV(device, pipeline, firstGroup, groupCount, dataSize, pData)
def vkGetAccelerationStructureHandleNV(device, accelerationStructure, dataSize, pData):
    jvulkanLib.vkGetAccelerationStructureHandleNV(device, accelerationStructure, dataSize, pData)
def vkCmdWriteAccelerationStructuresPropertiesNV(commandBuffer, accelerationStructureCount, pAccelerationStructures, queryType, queryPool, firstQuery):
    jvulkanLib.vkCmdWriteAccelerationStructuresPropertiesNV(commandBuffer, accelerationStructureCount, pAccelerationStructures, queryType, queryPool, firstQuery)
def vkCompileDeferredNV(device, pipeline, shader):
    jvulkanLib.vkCompileDeferredNV(device, pipeline, shader)
def vkGetMemoryHostPointerPropertiesEXT(device, handleType, pHostPointer, pMemoryHostPointerProperties):
    jvulkanLib.vkGetMemoryHostPointerPropertiesEXT(device, handleType, pHostPointer, pMemoryHostPointerProperties)
def vkCmdWriteBufferMarkerAMD(commandBuffer, pipelineStage, dstBuffer, dstOffset, marker):
    jvulkanLib.vkCmdWriteBufferMarkerAMD(commandBuffer, pipelineStage, dstBuffer, dstOffset, marker)
def vkGetPhysicalDeviceCalibrateableTimeDomainsEXT(physicalDevice, pTimeDomainCount, pTimeDomains):
    jvulkanLib.vkGetPhysicalDeviceCalibrateableTimeDomainsEXT(physicalDevice, pTimeDomainCount, pTimeDomains)
def vkGetCalibratedTimestampsEXT(device, timestampCount, pTimestampInfos, pTimestamps, pMaxDeviation):
    jvulkanLib.vkGetCalibratedTimestampsEXT(device, timestampCount, pTimestampInfos, pTimestamps, pMaxDeviation)
def vkCmdDrawMeshTasksNV(commandBuffer, taskCount, firstTask):
    jvulkanLib.vkCmdDrawMeshTasksNV(commandBuffer, taskCount, firstTask)
def vkCmdDrawMeshTasksIndirectNV(commandBuffer, buffer, offset, drawCount, stride):
    jvulkanLib.vkCmdDrawMeshTasksIndirectNV(commandBuffer, buffer, offset, drawCount, stride)
def vkCmdDrawMeshTasksIndirectCountNV(commandBuffer, buffer, offset, countBuffer, countBufferOffset, maxDrawCount, stride):
    jvulkanLib.vkCmdDrawMeshTasksIndirectCountNV(commandBuffer, buffer, offset, countBuffer, countBufferOffset, maxDrawCount, stride)
def vkCmdSetExclusiveScissorNV(commandBuffer, firstExclusiveScissor, exclusiveScissorCount, pExclusiveScissors):
    jvulkanLib.vkCmdSetExclusiveScissorNV(commandBuffer, firstExclusiveScissor, exclusiveScissorCount, pExclusiveScissors)
def vkCmdSetCheckpointNV(commandBuffer, pCheckpointMarker):
    jvulkanLib.vkCmdSetCheckpointNV(commandBuffer, pCheckpointMarker)
def vkGetQueueCheckpointDataNV(queue, pCheckpointDataCount, pCheckpointData):
    jvulkanLib.vkGetQueueCheckpointDataNV(queue, pCheckpointDataCount, pCheckpointData)
def vkInitializePerformanceApiINTEL(device, pInitializeInfo):
    jvulkanLib.vkInitializePerformanceApiINTEL(device, pInitializeInfo)
def vkUninitializePerformanceApiINTEL(device):
    jvulkanLib.vkUninitializePerformanceApiINTEL(device)
def vkCmdSetPerformanceMarkerINTEL(commandBuffer, pMarkerInfo):
    jvulkanLib.vkCmdSetPerformanceMarkerINTEL(commandBuffer, pMarkerInfo)
def vkCmdSetPerformanceStreamMarkerINTEL(commandBuffer, pMarkerInfo):
    jvulkanLib.vkCmdSetPerformanceStreamMarkerINTEL(commandBuffer, pMarkerInfo)
def vkCmdSetPerformanceOverrideINTEL(commandBuffer, pOverrideInfo):
    jvulkanLib.vkCmdSetPerformanceOverrideINTEL(commandBuffer, pOverrideInfo)
def vkAcquirePerformanceConfigurationINTEL(device, pAcquireInfo, pConfiguration):
    jvulkanLib.vkAcquirePerformanceConfigurationINTEL(device, pAcquireInfo, pConfiguration)
def vkReleasePerformanceConfigurationINTEL(device, configuration):
    jvulkanLib.vkReleasePerformanceConfigurationINTEL(device, configuration)
def vkQueueSetPerformanceConfigurationINTEL(queue, configuration):
    jvulkanLib.vkQueueSetPerformanceConfigurationINTEL(queue, configuration)
def vkGetPerformanceParameterINTEL(device, parameter, pValue):
    jvulkanLib.vkGetPerformanceParameterINTEL(device, parameter, pValue)
def vkSetLocalDimmingAMD(device, swapChain, localDimmingEnable):
    jvulkanLib.vkSetLocalDimmingAMD(device, swapChain, localDimmingEnable)
def vkGetBufferDeviceAddressEXT(device, pInfo):
    jvulkanLib.vkGetBufferDeviceAddressEXT(device, pInfo)
def vkGetPhysicalDeviceToolPropertiesEXT(physicalDevice, pToolCount, pToolProperties):
    jvulkanLib.vkGetPhysicalDeviceToolPropertiesEXT(physicalDevice, pToolCount, pToolProperties)
def vkGetPhysicalDeviceCooperativeMatrixPropertiesNV(physicalDevice, pPropertyCount, pProperties):
    jvulkanLib.vkGetPhysicalDeviceCooperativeMatrixPropertiesNV(physicalDevice, pPropertyCount, pProperties)
def vkGetPhysicalDeviceSupportedFramebufferMixedSamplesCombinationsNV(physicalDevice, pCombinationCount, pCombinations):
    jvulkanLib.vkGetPhysicalDeviceSupportedFramebufferMixedSamplesCombinationsNV(physicalDevice, pCombinationCount, pCombinations)
def vkCreateHeadlessSurfaceEXT(instance, pCreateInfo, pAllocator, pSurface):
    jvulkanLib.vkCreateHeadlessSurfaceEXT(instance, pCreateInfo, pAllocator, pSurface)
def vkCmdSetLineStippleEXT(commandBuffer, lineStippleFactor, lineStipplePattern):
    jvulkanLib.vkCmdSetLineStippleEXT(commandBuffer, lineStippleFactor, lineStipplePattern)
def vkResetQueryPoolEXT(device, queryPool, firstQuery, queryCount):
    jvulkanLib.vkResetQueryPoolEXT(device, queryPool, firstQuery, queryCount)
def vkCmdSetCullModeEXT(commandBuffer, cullMode):
    jvulkanLib.vkCmdSetCullModeEXT(commandBuffer, cullMode)
def vkCmdSetFrontFaceEXT(commandBuffer, frontFace):
    jvulkanLib.vkCmdSetFrontFaceEXT(commandBuffer, frontFace)
def vkCmdSetPrimitiveTopologyEXT(commandBuffer, primitiveTopology):
    jvulkanLib.vkCmdSetPrimitiveTopologyEXT(commandBuffer, primitiveTopology)
def vkCmdSetViewportWithCountEXT(commandBuffer, viewportCount, pViewports):
    jvulkanLib.vkCmdSetViewportWithCountEXT(commandBuffer, viewportCount, pViewports)
def vkCmdSetScissorWithCountEXT(commandBuffer, scissorCount, pScissors):
    jvulkanLib.vkCmdSetScissorWithCountEXT(commandBuffer, scissorCount, pScissors)
def vkCmdBindVertexBuffers2EXT(commandBuffer, firstBinding, bindingCount, pBuffers, pOffsets, pSizes, pStrides):
    jvulkanLib.vkCmdBindVertexBuffers2EXT(commandBuffer, firstBinding, bindingCount, pBuffers, pOffsets, pSizes, pStrides)
def vkCmdSetDepthTestEnableEXT(commandBuffer, depthTestEnable):
    jvulkanLib.vkCmdSetDepthTestEnableEXT(commandBuffer, depthTestEnable)
def vkCmdSetDepthWriteEnableEXT(commandBuffer, depthWriteEnable):
    jvulkanLib.vkCmdSetDepthWriteEnableEXT(commandBuffer, depthWriteEnable)
def vkCmdSetDepthCompareOpEXT(commandBuffer, depthCompareOp):
    jvulkanLib.vkCmdSetDepthCompareOpEXT(commandBuffer, depthCompareOp)
def vkCmdSetDepthBoundsTestEnableEXT(commandBuffer, depthBoundsTestEnable):
    jvulkanLib.vkCmdSetDepthBoundsTestEnableEXT(commandBuffer, depthBoundsTestEnable)
def vkCmdSetStencilTestEnableEXT(commandBuffer, stencilTestEnable):
    jvulkanLib.vkCmdSetStencilTestEnableEXT(commandBuffer, stencilTestEnable)
def vkCmdSetStencilOpEXT(commandBuffer, faceMask, failOp, passOp, depthFailOp, compareOp):
    jvulkanLib.vkCmdSetStencilOpEXT(commandBuffer, faceMask, failOp, passOp, depthFailOp, compareOp)
def vkGetGeneratedCommandsMemoryRequirementsNV(device, pInfo, pMemoryRequirements):
    jvulkanLib.vkGetGeneratedCommandsMemoryRequirementsNV(device, pInfo, pMemoryRequirements)
def vkCmdPreprocessGeneratedCommandsNV(commandBuffer, pGeneratedCommandsInfo):
    jvulkanLib.vkCmdPreprocessGeneratedCommandsNV(commandBuffer, pGeneratedCommandsInfo)
def vkCmdExecuteGeneratedCommandsNV(commandBuffer, isPreprocessed, pGeneratedCommandsInfo):
    jvulkanLib.vkCmdExecuteGeneratedCommandsNV(commandBuffer, isPreprocessed, pGeneratedCommandsInfo)
def vkCmdBindPipelineShaderGroupNV(commandBuffer, pipelineBindPoint, pipeline, groupIndex):
    jvulkanLib.vkCmdBindPipelineShaderGroupNV(commandBuffer, pipelineBindPoint, pipeline, groupIndex)
def vkCreateIndirectCommandsLayoutNV(device, pCreateInfo, pAllocator, pIndirectCommandsLayout):
    jvulkanLib.vkCreateIndirectCommandsLayoutNV(device, pCreateInfo, pAllocator, pIndirectCommandsLayout)
def vkDestroyIndirectCommandsLayoutNV(device, indirectCommandsLayout, pAllocator):
    jvulkanLib.vkDestroyIndirectCommandsLayoutNV(device, indirectCommandsLayout, pAllocator)
def vkAcquireDrmDisplayEXT(physicalDevice, drmFd, display):
    jvulkanLib.vkAcquireDrmDisplayEXT(physicalDevice, drmFd, display)
def vkGetDrmDisplayEXT(physicalDevice, drmFd, connectorId, display):
    jvulkanLib.vkGetDrmDisplayEXT(physicalDevice, drmFd, connectorId, display)
def vkCreatePrivateDataSlotEXT(device, pCreateInfo, pAllocator, pPrivateDataSlot):
    jvulkanLib.vkCreatePrivateDataSlotEXT(device, pCreateInfo, pAllocator, pPrivateDataSlot)
def vkDestroyPrivateDataSlotEXT(device, privateDataSlot, pAllocator):
    jvulkanLib.vkDestroyPrivateDataSlotEXT(device, privateDataSlot, pAllocator)
def vkSetPrivateDataEXT(device, objectType, objectHandle, privateDataSlot, data):
    jvulkanLib.vkSetPrivateDataEXT(device, objectType, objectHandle, privateDataSlot, data)
def vkGetPrivateDataEXT(device, objectType, objectHandle, privateDataSlot, pData):
    jvulkanLib.vkGetPrivateDataEXT(device, objectType, objectHandle, privateDataSlot, pData)
def vkCmdSetFragmentShadingRateEnumNV(commandBuffer, shadingRate, combinerOps):
    jvulkanLib.vkCmdSetFragmentShadingRateEnumNV(commandBuffer, shadingRate, combinerOps)
def vkAcquireWinrtDisplayNV(physicalDevice, display):
    jvulkanLib.vkAcquireWinrtDisplayNV(physicalDevice, display)
def vkGetWinrtDisplayNV(physicalDevice, deviceRelativeId, pDisplay):
    jvulkanLib.vkGetWinrtDisplayNV(physicalDevice, deviceRelativeId, pDisplay)
def vkCmdSetVertexInputEXT(commandBuffer, vertexBindingDescriptionCount, pVertexBindingDescriptions, vertexAttributeDescriptionCount, pVertexAttributeDescriptions):
    jvulkanLib.vkCmdSetVertexInputEXT(commandBuffer, vertexBindingDescriptionCount, pVertexBindingDescriptions, vertexAttributeDescriptionCount, pVertexAttributeDescriptions)
def vkGetDeviceSubpassShadingMaxWorkgroupSizeHUAWEI(device, renderpass, pMaxWorkgroupSize):
    jvulkanLib.vkGetDeviceSubpassShadingMaxWorkgroupSizeHUAWEI(device, renderpass, pMaxWorkgroupSize)
def vkCmdSubpassShadingHUAWEI(commandBuffer):
    jvulkanLib.vkCmdSubpassShadingHUAWEI(commandBuffer)
def vkCmdBindInvocationMaskHUAWEI(commandBuffer, imageView, imageLayout):
    jvulkanLib.vkCmdBindInvocationMaskHUAWEI(commandBuffer, imageView, imageLayout)
def vkGetMemoryRemoteAddressNV(device, pMemoryGetRemoteAddressInfo, pAddress):
    jvulkanLib.vkGetMemoryRemoteAddressNV(device, pMemoryGetRemoteAddressInfo, pAddress)
def vkCmdSetPatchControlPointsEXT(commandBuffer, patchControlPoints):
    jvulkanLib.vkCmdSetPatchControlPointsEXT(commandBuffer, patchControlPoints)
def vkCmdSetRasterizerDiscardEnableEXT(commandBuffer, rasterizerDiscardEnable):
    jvulkanLib.vkCmdSetRasterizerDiscardEnableEXT(commandBuffer, rasterizerDiscardEnable)
def vkCmdSetDepthBiasEnableEXT(commandBuffer, depthBiasEnable):
    jvulkanLib.vkCmdSetDepthBiasEnableEXT(commandBuffer, depthBiasEnable)
def vkCmdSetLogicOpEXT(commandBuffer, logicOp):
    jvulkanLib.vkCmdSetLogicOpEXT(commandBuffer, logicOp)
def vkCmdSetPrimitiveRestartEnableEXT(commandBuffer, primitiveRestartEnable):
    jvulkanLib.vkCmdSetPrimitiveRestartEnableEXT(commandBuffer, primitiveRestartEnable)
def vkCmdSetColorWriteEnableEXT(commandBuffer, attachmentCount, pColorWriteEnables):
    jvulkanLib.vkCmdSetColorWriteEnableEXT(commandBuffer, attachmentCount, pColorWriteEnables)
def vkCmdDrawMultiEXT(commandBuffer, drawCount, pVertexInfo, instanceCount, firstInstance, stride):
    jvulkanLib.vkCmdDrawMultiEXT(commandBuffer, drawCount, pVertexInfo, instanceCount, firstInstance, stride)
def vkCmdDrawMultiIndexedEXT(commandBuffer, drawCount, pIndexInfo, instanceCount, firstInstance, stride, pVertexOffset):
    jvulkanLib.vkCmdDrawMultiIndexedEXT(commandBuffer, drawCount, pIndexInfo, instanceCount, firstInstance, stride, pVertexOffset)
def vkSetDeviceMemoryPriorityEXT(device, memory, priority):
    jvulkanLib.vkSetDeviceMemoryPriorityEXT(device, memory, priority)
def vkGetDescriptorSetLayoutHostMappingInfoVALVE(device, pBindingReference, pHostMapping):
    jvulkanLib.vkGetDescriptorSetLayoutHostMappingInfoVALVE(device, pBindingReference, pHostMapping)
def vkGetDescriptorSetHostMappingVALVE(device, descriptorSet, ppData):
    jvulkanLib.vkGetDescriptorSetHostMappingVALVE(device, descriptorSet, ppData)
def vkCreateAccelerationStructureKHR(device, pCreateInfo, pAllocator, pAccelerationStructure):
    jvulkanLib.vkCreateAccelerationStructureKHR(device, pCreateInfo, pAllocator, pAccelerationStructure)
def vkDestroyAccelerationStructureKHR(device, accelerationStructure, pAllocator):
    jvulkanLib.vkDestroyAccelerationStructureKHR(device, accelerationStructure, pAllocator)
def vkCmdBuildAccelerationStructuresKHR(commandBuffer, infoCount, pInfos, ppBuildRangeInfos):
    jvulkanLib.vkCmdBuildAccelerationStructuresKHR(commandBuffer, infoCount, pInfos, ppBuildRangeInfos)
def vkCmdBuildAccelerationStructuresIndirectKHR(commandBuffer, infoCount, pInfos, pIndirectDeviceAddresses, pIndirectStrides, ppMaxPrimitiveCounts):
    jvulkanLib.vkCmdBuildAccelerationStructuresIndirectKHR(commandBuffer, infoCount, pInfos, pIndirectDeviceAddresses, pIndirectStrides, ppMaxPrimitiveCounts)
def vkBuildAccelerationStructuresKHR(device, deferredOperation, infoCount, pInfos, ppBuildRangeInfos):
    jvulkanLib.vkBuildAccelerationStructuresKHR(device, deferredOperation, infoCount, pInfos, ppBuildRangeInfos)
def vkCopyAccelerationStructureKHR(device, deferredOperation, pInfo):
    jvulkanLib.vkCopyAccelerationStructureKHR(device, deferredOperation, pInfo)
def vkCopyAccelerationStructureToMemoryKHR(device, deferredOperation, pInfo):
    jvulkanLib.vkCopyAccelerationStructureToMemoryKHR(device, deferredOperation, pInfo)
def vkCopyMemoryToAccelerationStructureKHR(device, deferredOperation, pInfo):
    jvulkanLib.vkCopyMemoryToAccelerationStructureKHR(device, deferredOperation, pInfo)
def vkWriteAccelerationStructuresPropertiesKHR(device, accelerationStructureCount, pAccelerationStructures, queryType, dataSize, pData, stride):
    jvulkanLib.vkWriteAccelerationStructuresPropertiesKHR(device, accelerationStructureCount, pAccelerationStructures, queryType, dataSize, pData, stride)
def vkCmdCopyAccelerationStructureKHR(commandBuffer, pInfo):
    jvulkanLib.vkCmdCopyAccelerationStructureKHR(commandBuffer, pInfo)
def vkCmdCopyAccelerationStructureToMemoryKHR(commandBuffer, pInfo):
    jvulkanLib.vkCmdCopyAccelerationStructureToMemoryKHR(commandBuffer, pInfo)
def vkCmdCopyMemoryToAccelerationStructureKHR(commandBuffer, pInfo):
    jvulkanLib.vkCmdCopyMemoryToAccelerationStructureKHR(commandBuffer, pInfo)
def vkGetAccelerationStructureDeviceAddressKHR(device, pInfo):
    jvulkanLib.vkGetAccelerationStructureDeviceAddressKHR(device, pInfo)
def vkCmdWriteAccelerationStructuresPropertiesKHR(commandBuffer, accelerationStructureCount, pAccelerationStructures, queryType, queryPool, firstQuery):
    jvulkanLib.vkCmdWriteAccelerationStructuresPropertiesKHR(commandBuffer, accelerationStructureCount, pAccelerationStructures, queryType, queryPool, firstQuery)
def vkGetDeviceAccelerationStructureCompatibilityKHR(device, pVersionInfo, pCompatibility):
    jvulkanLib.vkGetDeviceAccelerationStructureCompatibilityKHR(device, pVersionInfo, pCompatibility)
def vkGetAccelerationStructureBuildSizesKHR(device, buildType, pBuildInfo, pMaxPrimitiveCounts, pSizeInfo):
    jvulkanLib.vkGetAccelerationStructureBuildSizesKHR(device, buildType, pBuildInfo, pMaxPrimitiveCounts, pSizeInfo)
def vkCmdTraceRaysKHR(commandBuffer, pRaygenShaderBindingTable, pMissShaderBindingTable, pHitShaderBindingTable, pCallableShaderBindingTable, width, height, depth):
    jvulkanLib.vkCmdTraceRaysKHR(commandBuffer, pRaygenShaderBindingTable, pMissShaderBindingTable, pHitShaderBindingTable, pCallableShaderBindingTable, width, height, depth)
def vkCreateRayTracingPipelinesKHR(device, deferredOperation, pipelineCache, createInfoCount, pCreateInfos, pAllocator, pPipelines):
    jvulkanLib.vkCreateRayTracingPipelinesKHR(device, deferredOperation, pipelineCache, createInfoCount, pCreateInfos, pAllocator, pPipelines)
def vkGetRayTracingCaptureReplayShaderGroupHandlesKHR(device, pipeline, firstGroup, groupCount, dataSize, pData):
    jvulkanLib.vkGetRayTracingCaptureReplayShaderGroupHandlesKHR(device, pipeline, firstGroup, groupCount, dataSize, pData)
def vkCmdTraceRaysIndirectKHR(commandBuffer, pRaygenShaderBindingTable, pMissShaderBindingTable, pHitShaderBindingTable, pCallableShaderBindingTable, indirectDeviceAddress):
    jvulkanLib.vkCmdTraceRaysIndirectKHR(commandBuffer, pRaygenShaderBindingTable, pMissShaderBindingTable, pHitShaderBindingTable, pCallableShaderBindingTable, indirectDeviceAddress)
def vkGetRayTracingShaderGroupStackSizeKHR(device, pipeline, group, groupShader):
    jvulkanLib.vkGetRayTracingShaderGroupStackSizeKHR(device, pipeline, group, groupShader)
def vkCmdSetRayTracingPipelineStackSizeKHR(commandBuffer, pipelineStackSize):
    jvulkanLib.vkCmdSetRayTracingPipelineStackSizeKHR(commandBuffer, pipelineStackSize)
