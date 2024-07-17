class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        # Lower Space Complexity
        output = []
        output.append(1)
        for i in range(1, len(nums)):
            output.append(nums[i-1]*output[i-1])

        postfix = 1
        for i in range(len(nums)-2,-1,-1):
            postfix *= nums[i+1]
            output[i] *= postfix
        return output

        
        #NOTE: SLOWEST SOLUTION with BIGGEST MEMORY SPACE
        # # Get the prefix multiple
        # prefix = [0] * (len(nums)+1)
        # prefix[0] = 1
        # for i in range(1, len(nums)+1, 1):
        #     prefix[i] = prefix[i-1] * nums[i-1]
        
        # # Get the postfix multiple
        # postfix = [0] * (len(nums)+1)
        # last = len(nums)
        # postfix[last] = 1 
        # for i in range(last-1, -1, -1):
        #     postfix[i] = postfix[i+1] * nums[i]
        
        # # the output would be: (prefix at i-1) X (postfix at i+1)
        # # NOTE: Because the length of the prefix is increased at index 0, we just use i instead of i-1 
        # output = [0] * len(nums)
        # for i in range(len(nums)):
        #     output[i] = prefix[i] * postfix[i+1]
        
        # return output