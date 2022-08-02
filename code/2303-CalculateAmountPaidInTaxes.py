class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        tax = 0
        already_taxed = 0
        i = 0
        while already_taxed < income:
            crn_bracket = brackets[i]
            diff = crn_bracket[0] - brackets[i-1][0] if i > 0 else crn_bracket[0]
            tax += (float(crn_bracket[1]) / 100) * min(diff,(income - already_taxed))
            i += 1
            already_taxed += diff
        return tax