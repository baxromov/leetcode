nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums: list, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)
print(removeElement(nums, val))