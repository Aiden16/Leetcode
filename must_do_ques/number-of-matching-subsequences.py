class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        dic=defaultdict(list)
        for i in range(len(words)):
            dic[words[i][0]].append(words[i])
        # print(dic)
        count=0
        for i in s:
            var =  dic[i]
            dic[i]=[]
            for char in var:
                if len(char)==1:
                    count+=1
                else:
                    dic[char[1]].append(char[1:])
        return count
        #gave me tle
        # h={char:ind for ind,char in enumerate(s)}
        # print(h)
        # seen=set()
        # def is_sub(word):
        #     c=0
        #     p1=0
        #     p2=0
        #     while p1<=len(s)-1 and p2<=len(word)-1:
        #         if word[p2]==s[p1]:
        #             c+=1
        #             p2+=1
        #             p1+=1
        #         else:
        #             p1+=1
        #         if c==len(word):
        #             return True
        #     return  c==len(word)
        # ans=0
        # for word in words:
        #     if word in seen:
        #         ans+=1
        #     elif is_sub(word):
        #         # print(word)
        #         seen.add(word)
        #         ans+=1
        # return ans