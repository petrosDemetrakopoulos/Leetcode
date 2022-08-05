class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n).replace("0b","")
        sup = ""
        for i in binary:
            if i == '1':
                sup = sup + '0'
            else:
                sup = sup + '1'
        return int(sup,2)