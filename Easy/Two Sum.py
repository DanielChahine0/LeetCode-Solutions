class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        container = dict()

        for index in range(len(nums)):
            num = nums[index]
            wanted = target - num
            if wanted in container:
                return [index,container[wanted]]
            container[num] = index
            