"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 1. Sort intervals by their start time using interval attributes
        intervals.sort(key=lambda i: i.start)

        # 2. Iterate through and compare adjacent intervals
        for i in range(1, len(intervals)):
            previous_interval = intervals[i - 1]
            current_interval = intervals[i]

            # 3. If the current meeting starts before the previous one ends, there is a conflict
            if current_interval.start < previous_interval.end:
                return False
            
        return True
