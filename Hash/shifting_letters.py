class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        dic={}
        s=list(s)
        total=sum(shifts)
        p1=0
        for i in range(97,123):
            dic[i-97]=chr(i)
        for i in range(len(s)):
            val=ord(s[i])-97
            key=val+total
            if key<=25:
                s[i]=dic[key]
            else:
                s[i]=dic[key%26]
            total-=shifts[i]
        return "".join(s)