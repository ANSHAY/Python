# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins. Given n, find the total number of full staircase rows that can be formed1.

# Here are some examples:

# Example 1: Input: n = 5 Output: 2 Explanation: We can build the first two rows of the staircase completely since 1 + 2 < 5. The last row will be incomplete since the last row requires 3 coins and we have 5 coins in total1.

# Example 2: Input: n = 8 Output: 3 Explanation: We can build the first three rows of the staircase completely since 1 + 2 + 3 < 8. The last row will be incomplete since the last row requires 4 coins and we have 8 coins in total1.

# The constraints for the problem are:

# n is a non-negative integer and fits within the range of a 32-bit signed integer

# k2 + k -2n = 0
import math

def arrCoins(n):
    return (math.sqrt(1+8*n) - 1)//2

print(arrCoins(5))
print(arrCoins(8))
print(arrCoins(77))
print(arrCoins(0))
