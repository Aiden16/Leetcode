class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        #leetcode array modification soln
        count = 0
        for ind,val in enumerate(flowerbed):
            if ind == 0 and ind == len(flowerbed)-1:
                if flowerbed[ind] == 0:
                    count+=1
            elif ind==0:
                if val == 0 and flowerbed[ind+1] == 0:
                    count+=1
                    flowerbed[ind] = 1
            elif ind == len(flowerbed)-1:
                if val == 0 and flowerbed[ind-1]==0:
                    count+=1
                    flowerbed[ind] = 1
            else:
                if val == 0 and flowerbed[ind+1] == 0 and flowerbed[ind-1]==0:
                    count+=1
                    flowerbed[ind] = 1
        return count>=n
    
        #my own shitty soln
        if len(flowerbed) == 1:
            if flowerbed[0] == 1 and n==0:
                return True
            elif flowerbed[0] == 0 and (n==0 or n==1):
                return True
            else: return False
        count = 0
        prev = None
        zero = 0
        for ind,val in enumerate(flowerbed):
            if val == 0 and prev==None:
                zero+=1
                if zero%2==1:
                    count = (zero//2)+1
                else:
                    count = zero//2
            elif prev==None and val == 1:
                count = zero//2
                prev = ind
            elif prev!=None and val == 1:
                if ((ind-prev)-1)%2==1:
                    count += ((ind-prev-1)//2)
                else:
                    count+=((ind-prev-1)//2-1)
                prev = ind
                
            elif prev!=None and ind == len(flowerbed)-1:
                # print('==4')
                count+=(ind-prev)//2
        if count==n or count>n:
            return True
        