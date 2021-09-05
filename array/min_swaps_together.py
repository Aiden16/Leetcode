#using sliding window
def minswap(arr,k):
    good=0
    for i in arr:
        if i<=k:
            good+=1
    win=arr[:good]
    bad=0
    for i in win:
        if i>k:
            bad+=1
    left=0
    right=good+1
    ans=bad
    for left in range(1,len(arr)-good+1):
        if arr[left-1]>k:
            bad-=1
        if arr[right-1]>k:
            bad+=1
        ans=min(ans,bad)
        right+=1
    return ans
        

#using 2 pointer , verdict -> failed 
# def minswap(arr,k):
#     p1=0
#     p2=len(arr)-1
#     swap=0
#     while p1<p2:
#         if arr[p1]<=k:
#             p1+=1
#         else:
#             while arr[p1]>k:
#                 print(arr)
#                 if arr[p2]<=k:
#                     arr[p1],arr[p2]=arr[p2],arr[p1]
#                     swap+=1
#                     p1+=1
#                     p2-=1
#                     break
#                 else:
#                     p2-=1
#     print(swap)
#     return arr
print(minswap([2,7,9,5,8,7,4],6))
