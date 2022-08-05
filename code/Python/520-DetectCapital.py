class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        all_caps = True
        all_lower = True
        first_caps = True
        for i in word:
            if not i.isupper():
                all_caps = False
                break
        for i in word:
            if not i.islower():
                all_lower = False
                break
        if word[0].isupper():
            for i in word[1:]:
                if not i.islower():
                    first_caps = False
                    break
        else:
            first_caps = False
        return all_caps or all_lower or first_caps