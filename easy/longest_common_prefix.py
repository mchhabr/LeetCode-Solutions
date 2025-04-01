#https://leetcode.com/problems/longest-common-prefix/description/

# Time Complexity: O(m x n)
# Space Complexity: O(n)


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
