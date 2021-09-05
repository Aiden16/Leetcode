class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p=''.join(sorted(p))
        w=len(p)
        ans=[]
        for i in range(len(s)-(len(p)-1)):
            new=''.join(sorted(s[i:w]))
            if new==p:
                ans.append(i)
            w=w+1
        #using &
        print(set('cbad')&set('abc'))
        w=len(p)
        ans=[]
        for i in range(len(s)-(len(p)-1)):
            print('====>',s[i:w])
            new=set(s[i:w]) & set(p)
            print('set new {} || set p {}'.format(new,set(p)))
            print(new)
            if len(new)==len(set(s[i:w])):
                print('----ans----',i)
                ans.append(i)
            w+=1
        print('aaaa'&'aaaa')
        return ans
        
        