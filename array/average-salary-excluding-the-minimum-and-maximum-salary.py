class Solution:
    def average(self, salary: List[int]) -> float:
        mini=float('Infinity')
        maxi=float('-Infinity')
        s=0
        for i in salary:
            if i<mini:
                mini=i
            if maxi<i:
                maxi=i
            s+=i
        return (s-(mini+maxi))/(len(salary)-2)