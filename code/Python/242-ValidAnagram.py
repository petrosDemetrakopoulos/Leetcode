class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}
        for i in t:
            if i not in s:
                return False
            if i not in t_dict:
                t_dict[i] = 0
            else:
                t_dict[i] = t_dict[i] + 1
        for i in s:
            if i not in t:
                return False
            if i not in s_dict:
                s_dict[i] = 0
            else:
                s_dict[i] = s_dict[i] + 1
        
        for i in s_dict.keys():
            if s_dict[i] != t_dict[i]:
                return False
        
        return True