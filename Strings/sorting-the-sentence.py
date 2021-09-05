class Solution:
    def sortSentence(self, s: str) -> str:
        dic={}
        lis=s.split(' ')
        for i in range(len(lis)):
            # print(lis[i])
            dic[lis[i][-1]]=lis[i][:len(lis[i])-1]
        # print(dic)
        ans=''
        for i in range(1,len(lis)+1):
            if i!=len(lis):
                ans+=dic[str(i)]+' '
            else:
                ans+=dic[str(i)]
        # print(ans)
        return ans
            
        