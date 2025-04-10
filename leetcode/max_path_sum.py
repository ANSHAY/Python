# find max sum of paths of binary tree
# 
import sys
res = -sys.maxsize-1

def maxSum(root):
    if not root:
        return 0
    res = max(max(root.val + maxSum(root.left), root.val + maxSum(root.right)), root.val)
    return res