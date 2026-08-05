# Solution to the Valid Palindrome Problem
# https://leetcode.com/problems/valid-palindrome/description/
#
# Approach
# !!!! BAD !!!!
# - Reads like a stack problem
# - push until mid point, then popand compare
# - Each character needs compare so O(n) min
# - If the char leng is odd, ignore the mid character
# - The tricky part is handling the non alpha chars without impacting runtime
#   - Sanitizing itself would take O(n), then the compare worst case would be O(n)
#   - O(2n) can probably be improved... but well start there
# 
# !!!! BETTER !!!!
# iterating the whole list twice is dumb, we have the starting and ending points
# treat it like an array and utilize starting/ending index
# - Check if valid character, if not, update index and continue
# - If BOTH are alpha numeric then compare with lower(), != return False, == continue

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start].isalnum() and s[end].isalnum():
                if s[start].lower() != s[end].lower():
                    return False

                start += 1
                end -= 1
            else:
                if not s[start].isalnum():
                    start += 1

                if not s[end].isalnum():
                    end -= 1

        return True
