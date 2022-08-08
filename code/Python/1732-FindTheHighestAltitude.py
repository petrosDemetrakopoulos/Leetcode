class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alts = [0]
        crn_alt = 0
        for i in gain:
            alts.append(crn_alt + i)
            crn_alt = crn_alt + i
        return max(alts)