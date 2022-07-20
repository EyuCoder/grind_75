# https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        if r == 0:
            return mat
        visited = set()

        q = deque()
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dir[0], y + dir[1]
                if new_x >= 0 and new_x <= r-1 and new_y >= 0 and new_y <= c-1 and (new_x, new_y) not in visited:
                    mat[new_x][new_y] = mat[x][y] + 1
                    visited.add((new_x, new_y))
                    q.append((new_x, new_y))
        return mat
