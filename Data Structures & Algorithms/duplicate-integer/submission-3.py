class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #I -> Integer arr `nums`
        #O -> Boolean
        #P -> frequency counter and check if we have any two occurences in the hash map.

        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        for x in list(d.values()):
            if x > 1:
                return True
        return False
        