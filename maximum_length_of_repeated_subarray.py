nums1 = list(map(int,input().split(' ')))
nums2 = list(map(int,input().split(' ')))

def subArray(nums1,nums2):
    sub_array1 = []
    sub_array2 = []
    temp=''
    for i in range(len(nums1)):
        temp=str(nums1[i])
        sub_array1.append(temp)

        for j in range(i+1,len(nums1)):

            temp+='->'+str(nums1[j])
            sub_array1.append(temp)

            # print(temp)
            # print('===>',sub_array1)
        temp=''
    
    for i in range(len(nums2)):
        temp=str(nums2[i])
        sub_array2.append(temp)

        for j in range(i+1,len(nums2)):

            temp+='->'+str(nums2[j])
            sub_array2.append(temp)

            # print(temp)
            # print('===>',sub_array2)
        temp=''
    print(sub_array1)
    print(sub_array2)
    ans=[]
    for i in sub_array1:
        if i in sub_array2:
            ans.append(i)
    newLis=sorted(ans,key=lambda k : len(k),reverse=True)
    print(newLis)

    actualAns = list(map(int,(newLis[0].split('->'))))
    print(actualAns)
        

    return len(actualAns)



subArray(nums1,nums2)
print(subArray(nums1,nums2))


# class Solution(object):
#     def findLength(self, nums1, nums2):
#         longest = 0
#         shortest_empty = 1+min(len(nums1),len(nums2))
        
#         def sublists(lis,length):
#             lists = [[]]
#             for i in range(0, len(lis) - length + 1):
#                 lists.append(lis[i:i+length])
#             return lists[1:]
        
#         def checkMatching(length):
#             sub = sublists(nums2,length)
#             for i in range(0, len(nums1) - length + 1):
#                 if nums1[i:i+length] in sub:
#                     return True
#             return False
        
#         while shortest_empty - longest > 1:
#             check = (shortest_empty+longest)//2
#             if checkMatching(check):
#                 longest = check
#             else:
#                 shortest_empty = check
        
#         return longest