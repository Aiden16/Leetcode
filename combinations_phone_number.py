class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        if digits == '':
            return []
        elif len(digits)==1:
            return mapping[digits]
        result = ['']
        for digit in digits:
            temp=[]
            letters = mapping[digit]
            for letter in letters:
                for comb in result:
                    temp.append(comb+letter)
            result = temp
        return result
                    
#         print(mapping['2'])
#         self.dict = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz","10":" "}
#         result = [""]
#         for digit in digits:
#             lst = self.dict[digit]
#             newresult = []
#             for char in lst:
#                 print('chr+++>,',char)

#                 for str in result:

#                     print('str==>',str)
#                     newresult.append(str+char)
#                     print(newresult)
#                 print('for loop ends')

#             result = newresult
#             print('=====result======',result)
#         return result
        