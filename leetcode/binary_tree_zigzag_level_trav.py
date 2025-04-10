# /*
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
# */

from collections import deque

def zigZagLevel(root):
    que = deque()
    
    que.append(root)
    ltr = True
    while (len(que)>0):
        n = len(que)
        for i in range(n):
            if ltr:
                node = que.popleft()
            else:
                node = que.pop()
            print(node.val, end=' ')
            if ltr:
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            else:
                if node.right:
                    que.appendleft(node.right)
                if node.left:
                    que.appendleft(node.left)
        ltr = not ltr
                
        