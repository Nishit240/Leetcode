class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        result = [[1]]
        for i in range(numRows - 1):
            temp = [0] + result[-1] + [0]
            current = []
            for j in range(len(result[-1]) + 1):
                current.append(temp[j] + temp[j + 1])
            result.append(current)
        return result         
        """

        res = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = res[i-1][j-1] + res[i-1][j]

            res.append(row)

        return res