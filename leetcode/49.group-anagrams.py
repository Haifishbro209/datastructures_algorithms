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
        for i in range(len(strs)):
            string = ''.join(sorted(strs[i]))
            hashmap[string].append(i)
        
        output = []

        for anagram in hashmap:
            indices=hashmap[anagram]
            anagrams = []
            for i in indices:
                anagrams.append(strs[i])
            output.append(anagrams)
        
        return output
# @lc code=end

