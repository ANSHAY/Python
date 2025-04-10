# /**
#  * Given a binary tree, determine if it is height-balanced.
#  * For this problem, a height-balanced binary tree is defined as:

#  *  a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

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

def Node():
    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0

def balancedBT(root):
    if not root:
        return True, 0
    lb, lh = balancedBT(root.left)
    rb, rh = balancedBT(root.right)
    
    return (lb and rb and abs(lh-rh)<=1, max(lh, rh)+1)