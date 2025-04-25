class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        # find the part that is overlapping
        # for each balloons in points
        # --> if the last digit is >= next start
        # ---> yes then update the last digit
        # ---> max(last digit end, next digit end)
        # --> if not --> append
        if not points:
            return 0

        points.sort(key=lambda x: x[0])
        merged = []

        prev_start, prev_end = points[0]

        for start, end in points[1:]:
            if prev_end >= start:
                prev_end = min(prev_end, end)
            else:
                merged.append([prev_start, prev_end])
                prev_start, prev_end = start, end

        merged.append([prev_start, prev_end])
        return len(merged)