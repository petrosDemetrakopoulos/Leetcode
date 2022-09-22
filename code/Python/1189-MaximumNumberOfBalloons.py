from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        freq = Counter(text).most_common()
        filtered = [x for x in freq if x[0] in 'balon']
        if len(filtered) < 5:
            return 0
        filtered_dict = {}
        for ch in filtered:
            if ch[0] not in filtered_dict:
                filtered_dict[ch[0]] = ch[1]
        if filtered_dict['l'] < 2 or filtered_dict['o'] < 2:
            return 0
        return min([filtered_dict['b'], filtered_dict['a'], filtered_dict['l']/2,filtered_dict['o']/2, filtered_dict['n']])