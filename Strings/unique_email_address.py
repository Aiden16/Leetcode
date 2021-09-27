class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans=set()
        valid_email=''
        for email in emails:
            for char in email:
                if char=="+" or char=='@':
                    break
                elif char!='.':
                    valid_email+=char
            ind=email.index('@')
            valid_email+=email[ind:]
            ans.add(valid_email)
            valid_email=''
        return len(ans)