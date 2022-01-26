class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        #smaller and concise
        i=0
        while i+1 < len(arr) and arr[i]<arr[i+1]:
            i = i+1
        if i == 0 or i == len(arr)-1:
            return False
        while i+1 < len(arr) and arr[i]>arr[i+1]:
            i = i+1
        return i ==  len(arr)-1
    
    
        #peak valley approach
        peak,valley=0,0
        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]: #found peak
                peak = 1
            if arr[i-1]>= arr[i] <= arr[i+1]:
                valley = 1
        return peak == 1 and valley ==0
    
    
        #bit lenghty
        if len(arr)<3:
            return False
        is_increasing = False
        is_decreasing = False
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            if is_decreasing and not is_increasing:
                return False
            if is_decreasing and arr[i+1]>arr[i]:
                return False
            if arr[i+1]>arr[i]:
                is_increasing = True
            elif arr[i+1]<arr[i]:
                is_decreasing = True
        return is_increasing and is_decreasing
            
        