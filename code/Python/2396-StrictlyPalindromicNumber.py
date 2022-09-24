class Solution(object):
    DIGITS = '0123456789abcdef'

    def convert_to_base(self, decimal_number, base):
        remainder_stack = []

        while decimal_number > 0:
            remainder = decimal_number % base
            remainder_stack.append(remainder)
            decimal_number = decimal_number // base

        new_digits = []
        while remainder_stack:
            new_digits.append(self.DIGITS[remainder_stack.pop()])
        return ''.join(new_digits)
    
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for base in xrange(2,n-1):
            converted = self.convert_to_base(n,base)
            if converted != converted[::-1]:
                return False
        return True