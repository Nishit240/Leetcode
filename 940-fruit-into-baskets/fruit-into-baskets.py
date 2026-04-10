class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l = 0
        my_dict = {}
        for r in range(len(fruits)):
            my_dict[fruits[r]] = my_dict.get(fruits[r],0)+1
            if len(my_dict) > 2:
                my_dict[fruits[l]] -= 1
                if my_dict[fruits[l]] == 0:
                    del my_dict[fruits[l]]
                l += 1
            r += 1
        return len(fruits)-l

        






        