# Solution to the Two Sum problem
# https://leetcode.com/problems/two-sum

# Approach 1
# - Store num and index into hash map
# - When iterating nums, take the target - current use the result as a key to the map
# - Dupe keys dont matter since only single solution guarenteed
# - Give O(n) complexity, but larger space complexity
#
# Approach 2
# If space  omplexity if more important that runtime...
# - use nested loops and check if value at index i + value as index J = target
# - O(n^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index_map = {}
        for i, num in enumerate(nums):
            key = target - num

            if key in value_index_map:
                return [value_index_map[key], i]

            value_index_map[num] = i

    def twoSumSpace(self, nums: List[int], target: int) -> List[int]:
        array_len = len(nums)
        for i in range(array_len):
            for j in range(i+1, array_len):
                if nums[i] + nums[j] == target:
                    return [i, j]


