nums = [0, 0, 1, 1, 1, 2, 2 ,3 ,3, 4]


def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

print(removeDuplicates(nums))

"""

[0, 0, 1, 1, 1, 2, 2 ,3 ,3, 4]
i = 0 , j = 2
i = 1, j = 3
num[i] = 1


"""