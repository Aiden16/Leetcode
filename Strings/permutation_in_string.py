class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #optimal soln
        if len(s1)>len(s2):
            return False
        hash1={}
        for char in s1:
            hash1[char]=hash1.get(char,0)+1
        hash2={}
        for char in range(len(s1)):
            hash2[s2[char]]=hash2.get(s2[char],0)+1
        if hash1==hash2:
            return True
        for char in range(len(s1),len(s2)):
            left=char-len(s1)
            if hash2[s2[left]]==1:
                del hash2[s2[left]]
            else:
                hash2[s2[left]]-=1
            hash2[s2[char]]=hash2.get(s2[char],0)+1
            if hash1==hash2:
                return True
        return False
            
        #sliding window , 
        # hash={}
        # for i in s1:
        #     hash[i]=hash.get(i,0)+1
        # def ana(s1,s2):
        #     new={}
        #     for char in s2:
        #         if char in hash:
        #             new[char]=new.get(char,0)+1
        #         else:
        #             return False
        #     return new==hash
        # p1=0
        # p2=len(s1)-1
        # if len(s1)>len(s2):
        #     return False
        # while p2!=len(s2):
        #     win=s2[p1:p2+1]
        #     flag=ana(s1,win)
        #     if flag:
        #         return True
        #     p1+=1
        #     p2+=1
        # return False