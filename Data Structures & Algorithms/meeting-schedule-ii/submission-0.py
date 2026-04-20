"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        abs_intervals = []
        for each in intervals:
            abs_intervals.append(each.start)
            abs_intervals.append(-1 * each.end)

        abs_intervals.sort(key=lambda x: abs(x))

        current_count = 0
        max_count = 0
        for each in abs_intervals:
            if each >= 0:
                current_count += 1
            else:
                current_count -= 1
            max_count = max(max_count, current_count)

        print(abs_intervals)
        return max_count