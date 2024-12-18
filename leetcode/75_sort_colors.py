#Loom: https://www.loom.com/share/ce2e6b5bdc4942d5b97c5614732741cc
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]

        for color in nums:
            count[color] +=1

        index = 0
        for i in range(len(count)):
            for _ in range(count[i]):
                nums[index] = i
                index +=1
