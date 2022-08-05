class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent_cnt = 0
        consec_days_of_abs = 0
        consec_days_of_abs_over_3 = False
        for i in xrange(len(s)):
            if s[i] == 'L':
                consec_days_of_abs += 1
                if consec_days_of_abs >= 3:
                    consec_days_of_abs_over_3 = True
            if s[i] == 'A':
                absent_cnt += 1
            if s[i] == 'A' or s[i] == 'P' and not consec_days_of_abs_over_3:
                consec_days_of_abs = 0
        return absent_cnt < 2 and not consec_days_of_abs_over_3