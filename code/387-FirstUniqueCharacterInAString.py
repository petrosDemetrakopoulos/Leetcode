class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_str = list(s)
        hm = {}
        index = -1
        for i in range(len(list_str)):
            if list_str[i] not in hm:
                hm[list_str[i]] = [i,0]
            else:
                hm[list_str[i]] = [i, hm[list_str[i]][1] + 1]
        ind = 0
        
        vals = filter(lambda x: x[1] == 0, hm.values())
        while ind <= len(list_str):
            for i in range(len(vals)):
                if vals[i][0] == ind and vals[i][1] == 0:
                    return ind
            ind += 1
        return -1
        