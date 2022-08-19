import datetime
import calendar
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        date = datetime.datetime.strptime(str(day) + ' ' + str(month) + ' ' + str(year), '%d %m %Y').weekday()
        return calendar.day_name[date]