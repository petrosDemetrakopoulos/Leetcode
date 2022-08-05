class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxVal = 0
        sums_per_customer = []
        for customer in xrange(len(accounts)):
            customer_wealth = 0
            for acc in xrange(len(accounts[customer])):
                customer_wealth += accounts[customer][acc]
            sums_per_customer.append(customer_wealth)
        maxVal = max(sums_per_customer)
        return maxVal