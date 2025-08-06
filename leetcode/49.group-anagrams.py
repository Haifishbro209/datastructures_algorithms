#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            hashmap[sorted_str].append(string)
        
        output = []

        for anagram in hashmap:
            indices=hashmap[anagram]
            
            output.append(indices)
        
        return output
# @lc code=end

