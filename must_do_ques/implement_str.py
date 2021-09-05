class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        countNeedle={}
        for c in needle:
            print(c)
            countNeedle[c]=1+countNeedle.get(c,0)
        print(countNeedle)
        need=len(countNeedle)
        have=0
        win={}
        for ind,i in enumerate(haystack):
            if i in countNeedle:
                if not win:
                    index=ind
                win[i]=1+win.get(i,0)

            else:
                win={}
                have=0
            if i in countNeedle:
                if win[i]==countNeedle[i]:
                    have+=1
                elif win[i]>countNeedle[i]:
                    win={}
                    have=0
            if need==have:
                return index
                break
        return -1
                


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #2 pointer approach
        if not needle:
            return 0
        p1=0
        p2=0
        startChar=needle[0]
        update=0
        ind=0
        flag=0
        while p2!=len(haystack):
            if needle[p1]==haystack[p2]:
                # print(needle[p1])
                if not p1:
                    ind=p2
                    flag=1
                p1+=1
                p2+=1
            else:
                p1=0
                if flag:
                    p2=ind+1
                else:
                    p2+=1
                flag=0
            if p1==len(needle):
                print('hogya')
                return ind
                break
            if p2==len(haystack):
                break
            if haystack[p2]==startChar:
                update=p2

        return -1
