class Solution(object):
    alphabet_string = string.ascii_lowercase
    def firstCharAvailable(self,char1,char2):
        if char2 == None:
            for i in self.alphabet_string:
                if i != char1:
                    return i
        else:
            for i in self.alphabet_string:
                if i != char1 and i != char2:
                    return i
            
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return 'a' if s == '?' else s
        list_s = list(s)
        for i in xrange(len(list_s)):
            if list_s[i] == '?':
                if i == 0:
                    list_s[i] = self.firstCharAvailable(list_s[i+1],None)
                elif i == len(list_s)-1:
                    list_s[i] = self.firstCharAvailable(list_s[i-1],None)
                else:
                    list_s[i] = self.firstCharAvailable(list_s[i-1],list_s[i+1])
        return "".join(list_s)