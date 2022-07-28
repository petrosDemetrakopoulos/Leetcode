class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        edited = s.replace(' ','').lower()
        edited = str(edited)
        edited = ''.join(filter(str.isalnum, edited))
        str_list = list(edited)
        if len(str_list) % 2 == 0:
            middle_index = int(len(str_list) / 2)
            first = str_list[:middle_index]
            second = str_list[middle_index:]
            second.reverse()
            return first == second
        else:
            middle_index = int(len(str_list) / 2)
            middle_char = int(len(str_list) / 2)
            first = str_list[:middle_index]
            second = str_list[middle_index + 1:]
            second.reverse()
            first.append(str_list[middle_char])
            second.append(str_list[middle_char])
            return first == second