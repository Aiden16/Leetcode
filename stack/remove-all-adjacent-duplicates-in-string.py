class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        for i in s:
            if not st:
                st.append(i)
            else:
                if st[-1]==i:
                    st.pop(-1)
                else:
                    st.append(i)
        return ''.join(st)

           #2 pointers
        s=list(s)
        i=0
        for j in range(len(s)):
            s[i] = s[j]
            if i>0 and s[i-1]==s[i]:
                i-=2
            i+=1
        return ''.join(s[0:i])