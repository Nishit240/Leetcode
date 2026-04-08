class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(matrix)
        c = len(matrix[0])
        result = [[0]*r for _ in range(c)]

        for i in range(r):
            for j in range(c):
                result[j][i] = matrix[i][j]
        return result
                
        