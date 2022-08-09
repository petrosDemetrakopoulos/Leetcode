class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary_str = str(bin(n))[2:]
        binary_str = binary_str[::-1]
        binary_str += '0' * (32-len(binary_str))
        return int(binary_str,2)