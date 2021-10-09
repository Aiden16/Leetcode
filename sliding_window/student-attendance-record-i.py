class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #use sliding window
        if len(s)<3:
            return False if s.count('A')>=2 else True
        a=0
        win=''
        for i in range(3):
            win+=s[i]
            if s[i]=='A':
                a+=1
        if win.count('L')==3:return False
        left=0
        for j in range(0,len(s)-3):
            win+=s[j+3]
            if s[j+3]=='A':
                a+=1
            left+=1
            if a>=2 or win[left:j+4].count('L')==3:
                return False
        return True
            
        