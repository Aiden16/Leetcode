class Solution:
    def reverseWords(self, s: str) -> str:
        strlis=s.split(' ')
        lis=[]
        for i in strlis:
            if i!='' and i!=' ':
                lis.append(i)
        new=''
        for i in range(len(lis)-1,-1,-1):
            if i==0:
                new+=lis[i]
            else:
                new+=lis[i]+' '
        return new
        