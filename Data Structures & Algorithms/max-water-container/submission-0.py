class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        left = 0
        right = len(heights) - 1

        for height in heights: #1 
            bottom = right - left  #
            max_height_container = min(heights[left], heights[right])

            area = bottom * max_height_container

            if max_area < area:
                max_area = area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area



