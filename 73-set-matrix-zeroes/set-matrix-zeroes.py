class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        rows = [0 for _ in range(r)]
        cols = [0 for _ in range(c)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rows[i] = -1
                    cols[j] = -1
        
        for i in range(r):
            for j in range(c):
                if rows[i] == -1 or cols[j] == -1:
                    matrix[i][j] = 0

