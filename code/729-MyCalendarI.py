class MyCalendar(object):

    def __init__(self):
        self.cal = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if len(self.cal) == 0:
            self.cal.append([start,end])
            return True
        else:
            for book in self.cal:
                x = book[0]
                y = book[1]
                if (start >= x and start <  y) or (end > x and end <=y):
                    return False
                if x > start and y < end:
                    return False
            self.cal.append([start,end])
            return True
                
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)