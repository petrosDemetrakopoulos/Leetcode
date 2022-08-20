from datetime import datetime
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year = date.split('-')[0]
        d1 = datetime.strptime(year+'-01-01', "%Y-%m-%d")
        d2 = datetime.strptime(date, "%Y-%m-%d")
        return abs((d2 - d1).days) + 1