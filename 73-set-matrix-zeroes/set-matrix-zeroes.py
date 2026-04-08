class Solution(object):
    def setZeroes(self, matrix):
        '''
        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0
        '''
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

