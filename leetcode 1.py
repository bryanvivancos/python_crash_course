List = 3,4,5,7,9
target = 9
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=0
        for i in range(len(nums)):
            p = target-nums[i]
            if p in nums:
                a=nums.index(p)
                if a==i:
                    continue
                break
        return i,a