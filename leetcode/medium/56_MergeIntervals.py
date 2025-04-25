class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

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

