class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # c1=trust[0]
        #O(n) soln
        if not trust and n==1:
            return 1
        track=[0]*(n+1)
        for trusting,trusted in trust:
            track[trusting]-=1
            track[trusted]+=1
        for ind,val in enumerate(track):
            if val==n-1:
                return ind
        return -1
    
    
        #soln using dictionary
        if n==1:
            return 1
        trusting = set()
        hash={}
        for i in range(len(trust)):
            trusting.add(trust[i][0])
            if trust[i][1] not in trusting:
                hash[trust[i][1]] = hash.get(trust[i][1],0)+1
            if trust[i][0] in hash:
                del hash[trust[i][0]]
        for i in hash.keys():
            if hash[i]==n-1:
                return i
        return -1
        