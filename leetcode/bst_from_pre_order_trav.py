class Node():
    def __init__(self, val=0):
        self.right = None
        self.left = None
        self.val = val
        
# recursive
def bstFromPre(arr, start):
    root = Node(arr[start])
    if start == len(arr):
        return root
    if arr[start] > arr[start+1]:
        root.left = bstFromPre(arr, start+1)
    else:
        root.right = bstFromPre(arr, start+1)
    return root

    
def insert(val, node=None):
    if not node:
        node = Node(val)
        return node
    if val < node.val:
        node.left = insert(val, node.left)
    else:
        node.right = insert(val, node.right)
    return node

# iterative
def bstFromPre(arr):
    root = Node(arr[0])
    for i in range(1, len(arr)):
        insert(arr[i], root)
    return root