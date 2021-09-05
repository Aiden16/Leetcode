
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        dic={}
        for i in strs:
            s=''.join(sorted(i))
            if s in dic:
                dic[s].append(i)
            else:
                dic[s]=[i]
        for i in dic:
            ans.append(dic[i])
        return ans


# def ana(w,a):
#     if w==a:
#         return True
#     whash={}
#     ahash={}
#     for i in w:
#         if i in whash:
#             whash[i]+=1
#         else:
#             whash[i]=1
#     for i in a:
#         if i in ahash:
#             ahash[i]+=1
#         else:
#             ahash[i]=1
#     print(whash)
#     print(ahash)
#     if not whash and not ahash:
#         return True
#     if not whash or not ahash:return False
#     if len(whash)!=len(ahash):return False
#     for i in ahash.keys():
#         if i in whash:
#             if ahash[i]!=whash[i]:
#                 return False
#         else:
#             return False
#     return True
# strs = ["ac","c"]
# ans=[]
# evaluated=[]
# print('%%%%%%%%%%%%%%%%%%%%',ana("ac","c"))
# for i in range(len(strs)):
#     print('======>',strs[i])
#     if strs[i] not in evaluated:
#         temp=[strs[i]]
#         evaluated.append(strs[i])
#         for j in range(i+1,len(strs)):
#             if ana(strs[i],strs[j]):
#                 print('--------------------------{} {} {}'.format(ana(strs[i],strs[j]),strs[i],strs[j]))
#                 print(strs[i],strs[j])
#                 temp.append(strs[j])
#                 evaluated.append(strs[j])
#         print(temp)
#         ans.append(temp)
# print(ans)