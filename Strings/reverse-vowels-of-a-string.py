#2 pointer approach
class Solution:
    def reverseVowels(self, s: str) -> str:
        lis=[]
        lis[0:]=s
        vowels='aeiouAEIOU'
        f=0
        l=len(s)-1
        while f<=l:
            if lis[f] in vowels and lis[l] in vowels:
                tmp=lis[f]
                lis[f]=lis[l]
                lis[l]=tmp
                l-=1
                f+=1
            elif lis[f] in vowels:
                l-=1
            elif lis[l] in vowels:
                f+=1
            else:
                f+=1
                l-=1
        return ''.join(lis)

        