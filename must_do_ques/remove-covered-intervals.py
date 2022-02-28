class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda k:k[0])
        p1,p2 = intervals[0][0],intervals[0][1]
        c = 0
        for i in range(1,len(intervals)):
            if p1<=intervals[i][0] and p2>=intervals[i][1]:
                c+=1
                continue
            elif p1==intervals[i][0] and p2<=intervals[i][1]:
                c+=1
                p2=intervals[i][1]
                continue
            p1 = intervals[i][0]
            p2 = intervals[i][1]
        return len(intervals)-c