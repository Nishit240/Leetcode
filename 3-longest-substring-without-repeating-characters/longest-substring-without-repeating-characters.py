class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # n = len(s)
        # length = 0

        # for i in range(0, n):
        #     my_set = set()
        #     for j in range (i,n):
        #         if s[j] in my_set:
        #             break
        #         length = max(length, j-i+1)
        #         my_set.add(s[j])
        # return length 

        my_dict = {}
        left, right, length = 0,0,0

        while right < len(s):
            if s[right] in  my_dict:
                left = max(left, my_dict[s[right]]+1)
            length = max(length , right-left+1)
            my_dict[s[right]] = right 
            right +=1 
        return length












        