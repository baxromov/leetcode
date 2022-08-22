from typing import List

nums = [4, 1, 2, 1, 2]


def singleNumber(nums: List[int]) -> int:
    return 2 * sum(set(nums)) - sum(nums)


print(singleNumber(nums))
