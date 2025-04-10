# // Given a 2d grid map of '1's (land) and '0's (water),
# // count the number of islands. An island is surrounded
# // by water and is formed by connecting adjacent lands
# // horizontally or vertically. You may assume all four
# // edges of the grid are all surrounded by water.

from collections import deque

def dfs(grid, r, c, visited):
    if r<0 or r>=len(grid):
        return
    if c<0 or c>=len(grid[0]):
        return
    if grid[r][c] == 0:
        return
    visited[r][c] = True
    dfs(grid, r+1, c)
    dfs(grid, r-1, c)
    dfs(grid, r, c+1)
    dfs(grid, r, c-1)
    
def bfs(grid, row, col, visited):
    que = deque()
    que.append((row,col))
    
    while(len(que)>0):
        r, c = que.popleft()
        visited[r][c] = True
        for i in [1, -1, 0, 0]:
            for j in [0, 0, 1, -1]:
                if grid[r+i][c+j] == 1 and not visited[r+i][c+j]:
                    que.append((r+i, c+j))
    
def countIslands(grid):
    if len(grid) == 0 or len(grid[0])==0:
        return 0
    count = 0
    visited = [[False for _ in range(len(grid))] for _ in range(len(grid[0]))]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]==1 and not visited[r][c]:
                # bfs(grid, r, c, visited)
                dfs(grid, r, c, visited)
                count += 1
    return count