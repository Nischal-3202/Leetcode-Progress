class Solution(object):
    def trap(self, height):
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        total = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] < leftMax:
                    total += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if height[right] < rightMax:
                    total += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1
        return total