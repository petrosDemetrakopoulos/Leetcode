class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        list_a = list(a)
        list_b = list(b)
        la = len(a) - 1
        lb = len(b) - 1
        total = 0
        i = 0
        while la >= 0:
            if list_a[la] == '1':
                total += 2 ** i
            i += 1
            la -= 1
        i = 0
        while lb >= 0:
            if list_b[lb] == '1':
                total += 2 ** i
            i += 1
            lb -= 1
        return bin(total).replace('0b','')