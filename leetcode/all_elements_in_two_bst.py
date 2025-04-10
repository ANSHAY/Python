# /*
# Given two binary search trees root1 and root2.

# Return a list containing all the integers from both trees sorted in ascending order.
# */
# /**
#  * Definition for a binary tree node.
#  * struct TreeNode {
#  *     int val;
#  *     TreeNode *left;
#  *     TreeNode *right;
#  *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
#  *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
#  *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
#  * };
#  */

class TreeNode():
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        
def iot(result, root):
    if not root:
        return
    if root.left:
        iot(result, root.left)
    result.append(result, root.val)
    if root.right:
        iot(result, root.right)
        
def merge(result, res1, res2):
    i=0
    j=0
    while (i<len(res1) and j<len(res2)):
        if (res1[i] < res2[j]):
            result.append(res1[i])
            i += 1
        else:
            result.append(res2[j])
            j+=1
    while (i < len(res1)):
        result.append(res1[i])
        i+=1
    while(j<len(res2)):
        result.append(res2[j])
        j+=1
        
def listElements(result, root1, root2):
    res1 = []
    res2 = []
    iot(res2, root2)
    iot(res1, root1)
    merge(result, res1, res2)
    print(result)
    
        