class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.split()
        n = len(s)
        return (len(s[n-1]))
        