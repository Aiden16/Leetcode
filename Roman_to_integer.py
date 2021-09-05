def romanToInt(s):

    dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    placedBefore = ['I','X','C']
    sum=0
   
    # for i in range(len(s)-1):
    #     print(s[i])
    #     if s[i]=='I':
    #         if s[i+1] == 'V' or s[i+1] == 'X':
    #             sum-=1
    #             print('was here')
    #         else:
    #             sum+=1
    #     elif s[i] == 'X':
    #         if s[i+1] == 'L' or s[i+1] == 'C':
    #             sum-=10
    #         else:
    #             sum+=10
    #     elif s[i] == 'C':
    #         if s[i+1] == 'D' or s[i+1] == 'M':
    #             sum-=100
    #         else:
    #             sum+=100
    #     else:
    #         sum+=dic[s[i]]
    #         print('lalal')
    if len(s)==1:
        return dic[s]
    else:
        
        lis=[]
        lis.append(s[1])
        for i in range(len(s)):
            print(s[i])
            if(len(s)-1>i):
                # print('m herreee')
                lis[0]=s[i+1]
            else:
                lis[0]=''
            print('lis===>',lis[-1])
            if s[i]=='I':
                if lis[-1] == 'V' or lis[-1] == 'X':
                    sum-=1
                    print('was here')
                else:
                    sum+=1
            elif s[i] == 'X':
                if lis[-1] == 'L' or lis[-1] == 'C':
                    sum-=10
                else:
                    sum+=10
            elif s[i] == 'C':
                if lis[-1] == 'D' or lis[-1] == 'M':
                    sum-=100
                else:
                    sum+=100
            else:
                sum+=dic[s[i]]
                # print('lalal')

        return sum

s=input()
print(romanToInt(s))