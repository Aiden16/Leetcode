class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hash={}
        ans=0
        for i in time:
            ans+=hash.get(-i%60,0)
            hash[i%60]=hash.get(i%60,0)+1
        return ans
    
    
    
        #long version
        h={}
        for i in time:
            print(i,i%60)
        # for i in time:
            # h[i]=h.get(i,0)+1
        print(-20%60)
        pairs=0
        for i in range(len(time)):
            if time[i]<=60:
                rem=60-time[i]
                if rem in h:
                    pairs+=h[rem]
            elif time[i]>60:
                req=(-time[i]%60)
                if req in h:
                    pairs+=h[req]
      
            h[time[i]%60]=h.get(time[i]%60,0)+1
        # print(pairs)
        print(h)
        return pairs
        