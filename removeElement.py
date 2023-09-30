def removeEle(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.remove(val)
            continue
        i += 1
    return len(nums)
nums = [3,2,2,3]
print(removeEle(nums, 3))
print(nums)
