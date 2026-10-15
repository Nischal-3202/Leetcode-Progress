from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue=deque()
        fresh=0
        minutes=0
        r=len(grid)
        c=len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    queue.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1
        opr=[-1,1,0,0]
        opc=[0,0,-1,1]
        while queue and fresh>0:
            level_size=len(queue)
            rotted_this_minute=False
            for i in range(level_size):
                r,c=queue.popleft()
                for j in range(4):
                    nr=r+opr[j]
                    nc=c+opc[j]
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                        if grid[nr][nc]==1:
                            grid[nr][nc]=2
                            queue.append([nr,nc])
                            fresh-=1
                            rotted_this_minute=True
            if rotted_this_minute:
                minutes+=1
        if fresh!=0:
            return -1
        else:
            return minutes
