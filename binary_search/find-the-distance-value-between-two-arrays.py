class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        #brute force
        # count=0
        # for i in arr1:
        #     flag=True
        #     for j in range(len(arr2)):
        #         if abs(i-arr2[j])<=d:
        #             flag=False
        #             break
        #     if flag:
        #         count+=1
        # return count
                    
        arr2.sort()
        def binary(arr,val,d):
            f=0
            l=len(arr)
            while f<l:
                mid=f+(l-f)//2
                if abs(arr[mid]-val)<=d:
                    print('for',val)
                    print(arr[mid])
                    return False
                elif arr[mid]>val:
                    l=mid
                else:
                    f=mid+1
            return True
        count=0
        for i in arr1:
            flag=binary(arr2,i,d)
            if flag:
                # print(i)
                count+=1
        return count
        