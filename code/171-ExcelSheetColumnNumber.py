class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        list_str = list(columnTitle)
        hash_table = {'A': 1,'B': 2,'C': 3,'D': 4,
                     'E': 5,'F': 6,'G': 7,'H':8,
                     'I':9,'J':10,'K':11,'L':12,
                     'M': 13,'N':14,'O':15,'P':16,
                     'Q': 17,'R': 18,'S': 19,'T':20,
                     'U':21,'V': 22,'W': 23,'X': 24,
                      'Y': 25,'Z': 26}
        num = 0
        l = len(columnTitle) - 1
        i = 1
        j = 1
        while l >= 0:
            num += hash_table[list_str[l]] * i
            l = l-1
            i = 26 ** j
            j += 1
        return num