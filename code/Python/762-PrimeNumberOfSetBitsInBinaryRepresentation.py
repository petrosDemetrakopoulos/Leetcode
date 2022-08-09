class Solution(object):
    def isprime(self,num):
        if num==2 or num==3:
            return True
        if num%2==0 or num<2:
            return False
        for n in range(3,int(num**0.5)+1,2):   
            if num%n==0:
                return False   
        return True

    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        prime_cnt = 0
        for i in xrange(left, right + 1):
            crn_bits = str(bin(i))[2:]
            crn_cnt = 0
            for char in crn_bits:
                if char == '1':
                    crn_cnt += 1
            if self.isprime(crn_cnt):
                prime_cnt += 1
        return prime_cnt