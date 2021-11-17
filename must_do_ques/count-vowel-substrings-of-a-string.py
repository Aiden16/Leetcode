class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        '''
        optimized, idk how this one works
        '''
        last_seen_vowels={i:-1 for i in 'aeiou'}
        last_seen_consonant=-1
        ans=0
        for ind,char in enumerate(word):
            if char in last_seen_vowels:
                last_seen_vowels[char]=ind
                ans+=max(min(last_seen_vowels.values())-last_seen_consonant,0)
            else:
                last_seen_consonant=ind
        return ans
        
        '''
        brute force
        '''
        win=set()
        vowels='aeiou'
        count=0
        #brute force
        for i in range(len(word)):
            win=set()
            if word[i] in vowels:
                win.add(word[i])
                for j in range(i+1,len(word)):
                    if word[j] in vowels:
                        win.add(word[j])
                    else:
                        break
                    if len(win)==5:
                        count+=1
                        # break
        # print(count)
        return  count

        # p1,p2=0
        # count=0
        # for i in range(len(word)):
        #     if word[i] in vowels:
        #         win.add(word[i])
        #         if not p1:
        #             p1=i
        #     if len(win)==5:
        #         p2=i
        #         break
        # while some condn:
        #     while word[p2] in vowels and len(win)==5:
        #         win.add(word[p2])
        #         count+=1
        #         p2+=1
                
        
        #wtf i hv done so far on leetcode
        
        vowels='aeiou'
        # p1=0
        # p2=1
        # win=set()
        # count=0
        # for i in range(len(word)):
        #     if word[i] in vowels:
        #         win.add(word[i])
        #         if not p1:
        #             p1=i
        #     if len(win)==5:
        #         count+=1
        #         p2=i
        #         break
        # print(p1,i)
        # p2+=1
        # if p2>=len(word):
        #     return count
        # while p2!=len(word):
        #     if word[p2] in vowels and len(win)==5:
        #         count+=1
        #     else:
        #         print(p2)
        #         win=set()
        #         while word[p2] not in vowels and p2<=len(word)-1:
        #             print(p2)
        #             p2+=1
        #             if p2>len(word)-1:
        #                 break
        #         if p2>len(word)-1:
        #             break
        #         p1=p2
        #         print(p1)
        #         win.add(word[p1])
        #     p2+=1
        # print('count',count)
        # while p
        