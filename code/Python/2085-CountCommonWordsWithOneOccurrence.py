class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        seen1 = set()
        seen2 = set()
        hm1 = set()
        hm2 = set()
        for el in words1:
            if el not in seen1:
                seen1.add(el)
                hm1.add(el)
            else:
                hm1.discard(el)
        for el in words2:
            if el not in seen2:
                seen2.add(el)
                hm2.add(el)
            else:
                hm2.discard(el)
    
        return len([value for value in hm1 if value in hm2])
        
        