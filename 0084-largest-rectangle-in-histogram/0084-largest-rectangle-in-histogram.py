class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans=0
        n=len(heights)
        left_stack=[]
        right_stack=[]
        nextSmallerright=[n]*n
        nextSmallerleft=[-1]*n

        for i in range(n):
            while right_stack and heights[i] < heights[right_stack[-1]]:
                rem = right_stack.pop()
                nextSmallerright[rem] = i

            right_stack.append(i)

        for i in range(n-1,-1,-1):
            while left_stack and heights[i] < heights[left_stack[-1]]:
                rem = left_stack.pop()
                nextSmallerleft[rem] = i

            left_stack.append(i)
        
        for i in range(n):
            width = nextSmallerright[i] - nextSmallerleft[i] - 1
            temp = heights[i] * width
            ans = max(ans, temp)
        return ans


