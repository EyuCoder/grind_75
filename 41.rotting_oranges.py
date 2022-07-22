# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited, curr, time = set(), deque(), 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited.add((i, j))
                elif grid[i][j] == 2:
                    curr.append((i, j))

        while visited and curr:
            # BFS iteration
            for _ in range(len(curr)):
                i, j = curr.popleft()

                for dir in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if dir in visited:
                        visited.remove(dir)
                        curr.append(dir)
            time += 1

        return -1 if visited else time
