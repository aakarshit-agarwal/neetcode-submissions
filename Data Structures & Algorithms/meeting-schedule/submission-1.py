"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)

        last_start = -1
        last_end = -1
        for each in intervals:
            if last_start == -1:
                last_start = each.start
                last_end = each.end
            elif last_end > each.start :
                return False
            else:
                last_start = each.start
                last_end = each.end
        return True

    def print_intervals(self, intervals):
        for each in intervals:
            print("(", each.start, each.end, ")")