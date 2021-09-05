lis = []
n=int(input())
lis = list(input().split(' '))
pre = []
s1=lis[0]
s2=lis[1]
flag=1
for i in range(min(len(s1),len(s2))):
    if s1[0] != s2[0]:
        flag=0
        break

    elif s1[i] == s2[i]:
        pre.append(s1[i])
    else:
        break
for i in lis[2:]:
    for j in range(min(len(pre),len(i))):
        if pre[j] != i[j]:
            pre[j] =0
longest_prefix = ''
if (len(pre)>0):
    for i in pre:
        if i !=0:
            longest_prefix+=i
else:
    print('""')            
print(pre)
print(longest_prefix)