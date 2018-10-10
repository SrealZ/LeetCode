"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.


Example:

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    """
    Time:O(n)
    Space:O(n)
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # most readable
        # for i in range(len(nums)):
        #     if (target - nums[i]) in nums:
        #         if i != nums.index(target - nums[i]):
        #             return [i, nums.index(target - nums[i])]
        # return "no two sum solution"

        # fastest
        temp = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in temp:
                if nums.index(complement) == i:
                    continue
                else:
                    return [nums.index(complement), i]
            else:
                temp.append(nums[i])
        return "no two sum solution"


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(nums, target)
    print(result)
