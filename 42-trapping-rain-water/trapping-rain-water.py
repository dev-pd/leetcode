class Solution:
    def trap(self, height: List[int]) -> int:
        # Using two pointer approach
        n = len(height)
        l = 0
        r = n-1
        lefMax = 0
        rigMax = 0
        totalWater = 0
        while l <= r:
            # when the left pointer has more height than left max 
            # assign the left max to height at left
            if height[l] <= height[r]:
                if height[l] >= lefMax:
                    lefMax = height[l]
                # if the height is less than left max 
                # it means it can entrap water so adding this to total water
                else:
                    totalWater += lefMax - height[l]
                l += 1
            
            else:
                if height[r] >= rigMax:
                    rigMax = height[r]
                else:
                    totalWater += rigMax - height[r]
                r -= 1
        return totalWater

        