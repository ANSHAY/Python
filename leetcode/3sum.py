# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets1.

# Here are some examples:

# Example 1: Input: nums = [-1,0,1,2,-1,-4] Output: [[-1,-1,2], [-1,0,1]] Explanation: nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0. nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0. nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0. The distinct triplets are [-1,0,1] and [-1,-1,2]. Notice that the order of the output and the order of the triplets does not matter2.

# Example 2: Input: nums = [0,1,1] Output: [] Explanation: The only possible triplet does not sum up to 02.

# Example 3: Input: nums = [0,0,0] Output: [[0,0,0]] Explanation: The only possible triplet sums up to 02.

# The constraints for the problem are:

# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

def doubles(result, nums, i, sum):
    l=i+1
    r=len(nums)-1
    while(r>l):
        if nums[r]+nums[l] == sum:
            result.append([nums[i], nums[l], nums[r]])
            return
        if nums[r]+nums[l] > sum:
            r-=1
        else:
            l+=1
    
def triplets(result, nums, sum):
    for i in range(len(nums)-2):
        doubles(result, nums, i, sum-nums[i])

def main(nums, sum):
    nums.sort()
    result = []
    triplets(result, nums, sum)
    return result

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    nums = [0,1,1]
    # nums = [0,0,0]
    sum = 0
    result = main(nums, sum)
    print(result)