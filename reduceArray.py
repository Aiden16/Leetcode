arr = list(map(int,input().split(' ')))
ans=[]
newLis = sorted(arr,key=lambda k : arr.count(k),reverse=True)
arr=[]
arr=[i for i in newLis if i not in arr]
print(arr)
print(newLis)
print(set(newLis))
# print(set(arr))
# for i in set(arr):
#     print(i)

def reduce(arr):
    arrLen = len(arr)
    print(arrLen//2)
    # print(newLis)
    is_half = 0
    for i in (arr):
        print('i==>',i)
        if arr.count(i)>=arrLen//2 and i not in ans:
            return i
        else:
            if is_half<arrLen//2 and i not in ans:
                is_half+=newLis.count(i)
                print('{} isHalf and count {}'.format(is_half,newLis.count(i)))
                ans.append(i)
            elif is_half>arrLen//2:
                break


print(reduce(newLis))
print(ans)


# class Solution:
#     def minSetSize(self, arr: List[int]) -> int:
#         unique = list(dict.fromkeys(arr))
#         # print(arr.count(22))
#         newLis = sorted(unique,key=lambda k : arr.count(k),reverse=True)
#         # newUnique = list(dict.fromkeys(newLis))
#         # print(unique)
#         # print(newLis)
#         arrLen = len(arr)
#         is_half = 0
#         count=0
#         # print('arr',arr)
#         for i in newLis:
#             # print('i+++>',i)
#             if arr.count(i)>=arrLen//2:
#                 return 1
#             else:
#                 if is_half<arrLen//2:
#                     is_half+=arr.count(i)
#                     # print('{} isHalf and count {}'.format(is_half,arr.count(i)))

#                     count+=1
#                 elif is_half>arrLen//2:
#                     break
#         return count


#actual soln

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        unique = list(dict.fromkeys(arr))
        a=list(Counter(arr).values())
        a.sort(reverse=True)
        half, cnt = len(arr)>>1, 0  #len(arr)>>1 will return half of len(arr)
        for i in a:
            half-=i
            cnt+=1
			
            if 0>=half:
                return cnt