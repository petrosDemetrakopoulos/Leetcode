class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        bin_str = str(bin(n)).replace('0b','')
        str_list = list(bin_str)
        for i in str_list:
            if i == '1':
                cnt +=1
        return cnt