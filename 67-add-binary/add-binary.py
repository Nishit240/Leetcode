class Solution(object):
    def addBinary(self, a, b):
        """
        sum_int = int(a, 2) + int(b, 2)
        return bin(sum_int)[2:]
        """
        result = bin(int(a, 2) + int(b, 2))[2:]
        return result
