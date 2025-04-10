# Given an integer array nums of 2n integers, pair these integers into n pairs (a1, b1), (a2, b2),..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum1.

# Here are some examples:

# Example 1: Input: nums = [1,4,3,2] Output: 4 Explanation: The pairs (1,2),(3,4) make the sum of their minimums 1 + 3 = 4, which is the maximum possible1.

# Example 2: Input: nums = [6,2,6,5,1,2] Output: 9 Explanation: The pairs (1,2),(2,5),(6,6) make the sum of their minimums 1 + 2 + 6 = 9, which is the maximum possible1.

# The constraints for the problem are:

# 1 <= n <= 10^4
# nums.length == 2 * n
# -10^4 <= nums[i] <= 10^4

def part(nums):
    nums.sort()
    parts = []
    for i in range(0, len(nums), 2):
        parts.append((nums[i], nums[i+1]))
    return parts

nums = [1,4,3,2]
print(part(nums))
nums = [6,2,6,5,1,2]
print(part(nums))
