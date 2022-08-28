class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        bucket = capacity
        res = 0
        i = 0
        crn_plant = plants[0]
        while crn_plant > 0:
            if bucket >= crn_plant:
                bucket = bucket - crn_plant
                res += 1
                plants[i] = 0
                i += 1
                if i < len(plants):
                    crn_plant = plants[i]
                else:
                    return res
            else:
                res += 2*i + 1
                bucket = capacity - crn_plant
                plants[i] = 0
                i+= 1
                if i < len(plants):
                    crn_plant = plants[i]
                else:
                    return res