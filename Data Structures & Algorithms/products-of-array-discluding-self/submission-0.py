class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1 for _ in range(0, len(nums))]
        post = [1 for _ in range(0, len(nums))]
        products = [1 for _ in range(0, len(nums))]


        if len(nums) == 1:
            return [1]
        
        product = 1
        for i in range(1,len(nums)):
            product *= nums[i-1]
            pre[i] = product

        product = 1
        for i in range(len(nums)-2, -1, -1):
            product *= nums[i+1]
            post[i] = product
        for i in range(0,len(nums)):
            products[i] = pre[i] * post[i]

        return products

