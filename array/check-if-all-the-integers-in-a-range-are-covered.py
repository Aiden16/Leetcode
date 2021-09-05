class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        arr=[i for i in range(left,right+1)]
        p=0
        for i in ranges:
            for r in range(i[0],i[-1]+1):
                if p==len(arr):
                    break
                else:
                    if r == arr[p]:
                        p+=1
        if p==len(arr):
            return True
        return False