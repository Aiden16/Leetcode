

from cv2 import merge
count = 0
def merge(a,b):
    global count
    i,j=0,0
    while i<len(a) and j<len(b):
        if a[i]>2*b[j]:
            print(a[i],b[j])
            count+=len(a)-i
            j+=1
        else:
            i+=1
    ap,bp=0,0
    new = []
    while ap<len(a) and bp<len(b):
        if a[ap]>b[bp]:
            # if a[ap]>2*b[bp]:
                # print(a[ap],b[ap])
                # count+=len(a)-ap
            new.append(b[bp])
            bp+=1
        else:
            new.append(a[ap])
            ap+=1
    if ap<len(a):
        for i in range(ap,len(a)):
            new.append(a[i])
    if bp<len(b):
        for i in range(bp,len(b)):
            new.append(b[i])
    print(a,b,new)
    # print(a,b,count)
    return new

def merge_sort(arr,l,r):
    if l==r:
        return [arr[l]]
    mid = (l+r)//2
    left = merge_sort(arr,l,mid)
    right = merge_sort(arr,mid+1,r)
    ans = merge(left,right)
    return ans
count = 0
arr=list(map(int,input().split(' ')))
print(merge_sort(arr,0,len(arr)-1))
print(count)