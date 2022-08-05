class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = bin(num).replace("0b","")
        sup = ""
        for i in binary:
            if i == '1':
                sup = sup + '0'
            else:
                sup = sup + '1'
        return int(sup,2)