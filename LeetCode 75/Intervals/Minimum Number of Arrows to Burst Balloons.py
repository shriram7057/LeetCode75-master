class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        # Sort balloons by their ending position
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        for x_start, x_end in points:
            # If the balloon starts after the last arrow's position,
            # we need a new arrow
            if x_start > end:
                arrows += 1
                end = x_end  # update arrow position

        return arrows
