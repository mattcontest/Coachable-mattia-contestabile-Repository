#Loom: https://www.loom.com/share/3ad998725e1c474cb0f5f0be9323139f

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Time Complexity: O(n)
        #Space Complexity: O(1)

        #We will declare our target which we will use to check
        #how many steps behind we can go past our original target
        target = len(nums) -1

        #We will be iterating with a for loop in range of len(nums) and
        # we will be moving backward and check whether depending how many steps
        # behind we can go if we can reach our final target which happens the first element
        # of our array nums[0]

        for i in range(len(nums)-1, -1,-1):
            if nums[i] + i >= target:
                target = i
        # We are looking for if the final target we reach is the first targer of our array

        return True if target == 0 else False
