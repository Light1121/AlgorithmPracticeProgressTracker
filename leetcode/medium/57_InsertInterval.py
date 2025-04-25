class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        merged = []

        prev_start, prev_end = intervals[0]

        for start, end in intervals[1:]:
            if prev_end >= start:
                prev_end = max(prev_end, end)
            else:
                merged.append([prev_start, prev_end])
                prev_start, prev_end = start, end

        merged.append([prev_start, prev_end])
        return merged