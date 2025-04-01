# https://leetcode.com/problems/roman-to-integer/

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {"I":1, "V":5, "X":10,"L":50,"C":100,"D":500, "M":1000,}
        total = 0
       
        for i in range(len(s)):
            if i + 1 < len(s) and hash_map[s[i]] < hash_map[s[i + 1]]:
                total -= int(hash_map[s[i]])
            else:
                total += int(hash_map[s[i]])
        return total