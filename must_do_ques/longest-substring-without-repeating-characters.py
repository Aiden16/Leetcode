class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        #set solution
        charSet=set()
        left=0
        res=0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            res=max(res,right-left+1)
        return res
                
        
        
        # start=0
        # hash={}
        # maxLen=0
        # for ind,char in enumerate(s):
        #     if char in hash and start<=hash[char]:
        #         start=hash[char]+1
        #     else:
        #         maxLen=max(maxLen,ind-start+1)
        #     hash[char]=ind
        # return maxLen
#         start = maxLength = 0
#         usedChar = {}
        
#         for i in range(len(s)):
#             if s[i] in usedChar and start <= usedChar[s[i]]:
#                 start = usedChar[s[i]] + 1
#             else:
#                 maxLength = max(maxLength, i - start + 1)

#             usedChar[s[i]] = i

#         return maxLength