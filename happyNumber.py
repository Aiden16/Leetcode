n=input()
sum=0
flag=0
if n=='1' or n=='7':
    print('True')
elif(len(n)<=1):
    print('False')
else:
    while int(n)>9:
        sum=0

        for i in n:
            sum+=int(i)*int(i)
        n=str(sum)
        print('sum==>',sum)
        print(n)
if n=='1' or n=='7':
    print('True')
else:
    print('False')

