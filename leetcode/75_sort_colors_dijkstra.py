#Loom: https://www.loom.com/share/ce2e6b5bdc4942d5b97c5614732741cc
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Using Dijkstra's algorithm (Dutch National Flag Problem)
        #I'll initialize both a left and right pointer
        l,r = 0, len(nums) -1
        i = 0

        #We will have to perform swapping alongisde our problem
        #So we will use an helper function to perform it
        def swap(i,j):
            # nums[i], nums[j] = nums[j], nums[i]
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        #We will now be using our pointers
        #To correctly sort our colors array
        #Time Complexity O(n)
        #Space Complexity O(1)
        while i <= r:
            if nums[i] == 0:
                swap(l,i)
                l+=1
                i+=1
            elif nums[i] == 2:
                swap(i,r)
                r -= 1
            else:
            #We will assume that the other number will be in
            #In their right position   
                i+=1

