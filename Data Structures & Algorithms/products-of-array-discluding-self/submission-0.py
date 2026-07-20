class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            product = 1
            for o_index in range(len(nums)):
                if o_index!= i:
                    product *= nums[o_index] 
            output.append(product)
        return output




