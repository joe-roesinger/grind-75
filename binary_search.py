# Solution to the Binary Search Problem
# https://leetcode.com/problems/binary-search/description/
#
# Approach
# 
# Odd that the name of the problem is the the solution....
#
# - Items are sorted
# - Allows for middle-point jumps based on if the value is < or >
# - Will allow for O(logn) runtime

class Solution:
    # Recursive, unneeded but fun
    def search_rec(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, nums: List[int], target: int, start: int, end: int) -> int:
        index = (end + start) // 2


        if start > end:
            return index if nums[index] == target else -1

        if nums[index] < target:
            return self.binary_search(nums, target, index + 1, end)
        elif nums[index] > target:
            return self.binary_search(nums, target, start, index - 1)
        else: 
            return index
        

    # Iterative
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            index = (end + start) // 2
            
            if nums[index] < target:
                start = index + 1
            elif nums[index] > target:
                end = index - 1
            else:
                return index

        return -1
