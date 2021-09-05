class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        #group by character
        arr=[]
        pivot=s[0]
        count=1
        for i in range(1,len(s)):
            if s[i]==pivot:
                count+=1
            else:
                arr.append(count)
                pivot=s[i]
                count=1
        arr.append(count)
        ans=0
        for i in range(len(arr)-1):
            ans+=min(arr[i],arr[i+1])
        print(arr)
        return ans