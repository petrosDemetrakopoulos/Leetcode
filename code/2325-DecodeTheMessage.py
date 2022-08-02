class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        list_key = list(key.replace(' ',''))
        stop_list = []
        for i in xrange(len(list_key)):
            if list_key[i] not in stop_list:
                stop_list.append(list_key[i])
            else:
                list_key[i] = '-'
        list_key = filter(lambda x: x != '-',list_key)
        list_key = map(lambda x: str(x), list_key)
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        message = map(lambda x: str(x), message)
        for i in xrange(len(message)):
            if message[i] != ' ':
                message[i] = alphabet[list_key.index(message[i])]
        return "".join(message)