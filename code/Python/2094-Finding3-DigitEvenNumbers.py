class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        for i in xrange(100,1000,2):
            str_i = list(str(i))
            all_in = True
            crn_digits = list(digits)
            for j in str_i:
                if int(j) not in crn_digits:
                    all_in = False
                else:
                    del crn_digits[crn_digits.index(int(j))]
            if all_in:
                res.append(int("".join(str_i)))
        return res