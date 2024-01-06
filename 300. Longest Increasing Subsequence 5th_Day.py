'''
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''


# Solution ----------------------------------------------------------------------------------------------------------------------------------

# Solution 1: Dynamic Programming
# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# Solution 2: Dynamic Programming with Binary Search
# Time Complexity: O(n log(n))
# Space Complexity: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                index = self.binarySearch(dp, nums[i])
                dp[index] = nums[i]
        return len(dp)
    def binarySearch(self, dp, target):
        low = 0
        high = len(dp) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if dp[mid] == target:
                return mid
            elif dp[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low