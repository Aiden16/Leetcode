def func(a,k):
    # s=sum(a)
    h={}
    s=0
    for i in range(len(a)):
        s+=a[i]
        h[i]=s
    count=0
    flag=1
    print(s)
    for dig in range(len(a)):
        newF=(h[dig]-a[dig])+k
        newL=(h[len(a)-1]-a[dig])+k
        if newF==newL and flag:
            print('--')
            count+=1
        print(h[dig],s-h[dig])
        if h[dig]==s-h[dig]:
            print('//')
            count+=1
    return count
print(func([22,4,-33,-20,-15,15,-16,7,19,-10,0,-13,-14],-33))
        