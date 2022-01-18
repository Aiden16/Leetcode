class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        #O(n)
        winner=arr[0]
        won=0
        for i in range(1,len(arr)):
            if arr[i]>winner:
                winner=arr[i]
                won=0
            won+=1
            if won==k:
                return winner
        return winner


        #slow
        h={}
        if k>len(arr):
            return max(arr)
        count=0
        while True:
            if arr[0]>arr[1]:
                tmp=arr.pop(1)
                arr.append(tmp)
                won=arr[0]
            else:
                tmp=arr.pop(0)
                arr.append(tmp)
                won=arr[0]
            h[won]=h.get(won,0)+1
            if h[won]==k:
                return won
                break
