class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        rec(image, sr, sc, visited, color_from=image[sr][sc], color_to=color)
        return image

def rec(image, row, col, visited, color_from, color_to):
    if oob(image, row, col) or image[row][col] != color_from or (row, col) in visited:
        return
    image[row][col] = color_to
    visited.add((row, col))
    rec(image, row+1, col, visited, color_from, color_to)
    rec(image, row-1, col, visited, color_from, color_to)
    rec(image, row, col+1, visited, color_from, color_to)
    rec(image, row, col-1, visited, color_from, color_to)

def oob(arr, i, j):
    if i < 0 or j < 0:
        return True
    if i >= len(arr) or j >= len(arr[0]):
        return True
    return False