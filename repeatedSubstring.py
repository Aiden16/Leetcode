s=input()
def checkStr(s):
    sub=''
    for i in s:
        sub+=i
        if s.count(sub)*len(sub) == len(s) and sub!=s:
            return sub
    return False
print(checkStr(s))