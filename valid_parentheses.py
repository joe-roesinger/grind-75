# Solution to the Valid Parentheses problem
# https://leetcode.com/problems/valid-parentheses/
#
# Solution
# - Reads like a stack problem
# - Push character that represents an open parentheses
# - When closing parentheses is hit, if its a type match POP
# - Otherwise the combo is invalid and return false
# - Once all characters are processed, if stack is empty, its valid,
#   if its non empty, invalid
# - Use dict for easy of checking matches

class Solution:
    char_pair_dict = {
        ']': '[',
        '}': '{',
        ')': '('
    }
    
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            # If the character is not a key its an open bracket
            if char not in self.char_pair_dict:
                stack.append(char)
            # If its a closed bracket, ensure theres something to match
            # then check that it is a match
            elif len(stack) == 0 or stack.pop() != self.char_pair_dict[char]:
                return False

        return len(stack) == 0
