class Solution:
    def makeGood(self, s: str) -> str:
        stck = []
        for i in range(len(s)):
            if not stck:
                stck.append(s[i])
                continue
            else:
                if stck[-1].lower() == s[i].lower():
                    if stck[-1].isupper() == s[i].islower() or stck[-1].islower == s[i].isupper():
                        stck.pop()
                    else:
                        stck.append(s[i])
                else:
                    stck.append(s[i])
        return ''.join(stck)