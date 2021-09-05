a=input()
b=input()
def repeatedMatch(a,b):
    cun=1
    c=a
    flag=1
    counter=1
    if b in a:
        return 1
    elif b[0] in a:
        for i in b:
            if i not in a:
                flag=0
        if flag==0:
            print('flag')
            return -1
        else:
            while(b not in a and ((len(b)*len(c))+10)>len(a)):
                print('cun==>',cun)
                cun+=1
                a+=c
                # print(a)
            if b in a:
                return a.count(c)
            else:
                print('b in a')
                return -1
    else:
        return -1
print(repeatedMatch(a,b))


