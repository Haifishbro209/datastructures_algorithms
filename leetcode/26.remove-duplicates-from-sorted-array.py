#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        try:
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if nums[i] == nums[j]:
                        nums.remove(nums[j])
                        j -= 1
        except IndexError as e:
            return len(nums)

        return len(nums)
        
        
# @lc code=end

