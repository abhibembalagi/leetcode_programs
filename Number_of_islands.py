class Solution:
    def isSafe(self, row, col, grid, visited):
        return(0<= row < len(grid) and
         0 <= col < len(grid[0]) and
         grid[row][col] == "1" and visited[row][col] == False)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = []
        visited = [[False for col in range(len(grid[0]))]for row in range(len(grid))]
        if not grid:
            return 0
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and visited[row][col] == False:
                    count += 1
                    queue.append((row, col))
                    visited[row][col] = True
                    while queue:
                        x, y = queue.pop(0)
                        if(self.isSafe(x-1, y, grid, visited)):
                            queue.append((x-1,y))
                            visited[x-1][y] = True
                        if(self.isSafe(x, y-1, grid, visited)):
                            queue.append((x,y-1))
                            visited[x][y-1] = True
                        
                        if(self.isSafe(x+1, y, grid, visited)):   
                            queue.append((x+1,y))
                            visited[x+1][y] = True
                        
                        if(self.isSafe(x, y+1, grid, visited)):
                            queue.append((x,y+1))
                            visited[x][y+1] = True
        return count
