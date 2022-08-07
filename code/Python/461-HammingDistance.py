class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bits_x = str(bin(x))[2:]
        bits_y = str(bin(y))[2:]
        len_y = len(bits_y)
        len_x = len(bits_x)
        new_bits_x = ''
        new_bits_y = ''
        if len_x < len_y:
            for i in xrange(len_y - len_x):
                new_bits_x += "0"
            new_bits_x += bits_x
        else:
            new_bits_x = bits_x
        if len_y < len_x:
            for i in xrange(len_x - len_y):
                new_bits_y += "0"
            new_bits_y += bits_y
        else:
            new_bits_y = bits_y
        dist = 0

        for i in xrange(len(new_bits_x)):
            if new_bits_x[i] != new_bits_y[i]:
                dist += 1
        return dist