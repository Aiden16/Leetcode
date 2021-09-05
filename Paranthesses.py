st =  input()
openPara = '{[('
closePara = '}])'
stack = [st[0]]
indO = 0
indC = 0
for i in range(1,len(st)):
    if(len(stack)!=0):
        print(stack)
        if stack[-1] in openPara and st[i] in closePara :
            indO = openPara.index(stack[-1])
            indC = closePara.index(st[i])
            
            print(indO)
            print(indC)
            
            if indO==indC:
                print('lala')
                stack.pop()
            else:
                stack.append(st[i])
        else:
            stack.append(st[i])




    else:
        stack.append(st[i])
print(stack)