from collections import deque

def levelTrav(root):
    if not root:
        return
    que = deque()
    que.append(root)
    while(len(que)>0):
        n = que.popleft()
        print(n.val, end=' ')
        if n.left:
            que.append(n.left)
        if n.right:
            que.append(n.right)
            
def preTrav(root):
    if not root:
        return
    print(root.val, end=' ')
    preTrav(root.left)
    preTrav(root.right)
    
def inTrav(root):
    if not root:
        return
    inTrav(root.left)
    print(root.val)
    inTrav(root.right)
    
def postTrav(root):
    if not root:
        return 
    postTrav(root.left)
    postTrav(root.right)
    print(root.val)
    
# iterative
def preTrav(root):
    if not root:
        return
    stack = [root]
    while (len(stack)>0):
        node = stack.pop()
        while (node.left):
            print (node.val, end = ' ')
            if node.right:
                stack.append(node.right)
            node = node.left
            
def inTrav(root):
    if not root:
        return
    stack = [root]
    while (len(stack)>0):
        node = stack.pop()
        if node.marked:
            print(node.val, end=' ')
        else:
            node.marked = True
            if node.right:
                stack.append(node.right)
            stack.append(node)
            if node.left:
                stack.append(node.left)
                
def postTrav(root):
    if not root:
        return
    stack = [root]
    while (len(stack)>0):
        node = stack.pop()
        if node.marked:
            print(node.val, end=' ')
        else:
            node.marked = True
            stack.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

def isMirror(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree2 or not tree1:
        return False
    return (tree1.val == tree2.val) and isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)

def isSymmetric(root):
    if not root:
        return True
    return isMirror(root.left, root.right)

def hasPathSum(root, sum):
    if not root:
        return sum==0
    return root.val==sum or hasPathSum(root.left, sum) or hasPathSum(root.left, sum-root.val)\
                         or hasPathSum(root.right, sum) or hasPathSum(root.right, sum-root.val)
                         
class Node():
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.val = 0
        
def insert(root, val):
    if not root:
        return Node(val)
    if val<root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
                         
def bstFromPost(arr):
    if len(arr)==0:
        return None
    root = Node(arr[-1])
    for i in range(len(arr)-2, -1, -1):
        root = insert(root, arr[i])
    return root

def findPath(root, target, path):
    if not root or not target:
        return False
    if target.val == root.val:
        path = root
        return True
    if(findPath(root.left, target, path)):
        path += root
        return True
    if(findPath(root.right, target, path)):
        path += root
        return True
    return False

def lowestCommonAncestor(root, n1, n2):
    if not root or not n1 or not n2:
        return None
    if root.val==n1.val or root.val==n2.val:
        return root
    left = lowestCommonAncestor(root.left, n1, n2)
    right = lowestCommonAncestor(root.right, n1, n2)
    if left and right:
        return root
    if left:
        return left
    return right
    