def bs(arr: List[int], target: int) -> bool:
    l,r = 0,len(arr)-1
    while l <= r:
        mid = l + ((r-l)//2)
        if arr[mid] == target:
            return True
        elif target > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up,down=0,len(matrix)-1

        while up <= down:
            mid = up + ((down-up)//2)
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                return bs(matrix[mid], target)
            elif target < matrix[mid][0]:
                down = mid - 1
            else:
                up = mid + 1