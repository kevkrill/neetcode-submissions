class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp_product = 1
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i: 
                    continue
                temp_product *= nums[j]
            
            res.append(temp_product)
            temp_product = 1
        return res