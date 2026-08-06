# Solution to the Valid Anagram Problem
# https://leetcode.com/problems/valid-anagram/description/
#
# Approach
#
# The "bonus" mentions including all unicode characters
# so well focus on that.
#
# Logically, a falid anagram means every character is seen
# the same number of times between each word.
#
# Since we have to validate each character, min RT would be
# O(n)
# The following "shortcuts" can save unneeded runtime:
# - s or t is None
# - len of s != len of t
#
# Storing each char as a key and count as the value in a dict
# Allows us to validate the other string without a runtime hit
# 
# An array would probably be more space efficient if just using 
# alphabetic characters, but I am unaware off the top of my head
# the number of valid unicode characters there are.
#
# For fun the array version will be tacked on
# but the approach is basically identical

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_dict = {}
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        for char in t:
            if char not in char_dict:
                return False
            elif char_dict[char] > 1:
                char_dict[char] -= 1
            else:
                char_dict.pop(char)

        return len(char_dict) == 0

    def isAnagramAlphabeticOnly(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_array = [0] * 26
        for char in s:
            char_array[ord(char) - ord('a')] += 1

        for char in t:
            char_array[ord(char) - ord('a')] -= 1

        return all(count == 0 for count in char_array)
