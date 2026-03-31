class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        difference= {}
        for i in range(len(nums)):
            second = target - nums[i]
            if second in difference:
                return [difference[second], i]
            difference[nums[i]] = i
        return []