def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = [*s]
        vowels = 'aeiouAEIOU'
        i, j = 0, len(arr)-1
        while i < j:
            while i < j and arr[i] not in vowels:
                i += 1
            while i < j and arr[j] not in vowels:
                j -= 1
            swap(arr, i, j)
            i += 1
            j -= 1
        return "".join(arr)