class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        date_list = date.split()
        months = {"Jan": '01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', 
                  "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', 
                  "Nov":'11', "Dec":'12'}
        day = ''
        if len(date_list[0]) == 3:
            day = '0' + date_list[0][0]
        elif len(date_list[0]) == 4:
            day = date_list[0][:2]
        return date_list[2]+'-'+months[date_list[1]]+'-'+day