#https://leetcode.com/problems/valid-parentheses/

# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution(object):
    def isValid(self, s):
        stack = []
        paranthesis_map = {')': '(', ']': '[', '}': '{'} 

        for char in s:
            if char in paranthesis_map: 
                top_element = stack.pop() if stack else '#'  
                if paranthesis_map[char] != top_element:  
                    return False
            else:  
                stack.append(char)

        return not stack  
            
        