class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #hash
        ransom={}
        for i in ransomNote:
            ransom[i]=ransom.get(i,0)+1
        counter=len(ransom)
        for i in magazine:
            if i in ransom:
                ransom[i]-=1
                if ransom[i]==0:
                    counter-=1
        if counter==0:
            return True
        return False
        # for i in ransom.values():
        #     if i >0:
        #         return False
        # return True
        #2 pointer approach
#         ransomeNote=''.join(sorted(ransomNote))
#         magazine = ''.join(sorted(magazine))
#         print(ransomeNote)
#         print(magazine)
#         if len(ransomNote)==1:
#             return ransomNote in magazine
#         p1=0
#         p2=0
#         print('===========',ransomeNote[p1])
#         while True:
#             # print(ransomeNote)
#             print(p1,p2)
#             print(ransomNote[p1],magazine[p2])
#             if ransomNote[p1]==magazine[p2]:
#                 print(ransomeNote[p1])
#                 p1+=1
#                 p2+=1
#             else:
#                 p2+=1
            
#             if p1>=len(ransomNote) or p2>=len(magazine):
#                 break
#         if p1==len(ransomNote):
#             return True
#         return False