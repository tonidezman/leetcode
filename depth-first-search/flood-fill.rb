def oob(image, row, col)
    return true if row < 0 || col < 0
    return true if row >= image.size || col >= image[0].size
    return false
end

def rec(image, row, col, color_from, color_to)
    return if oob(image, row, col) || image[row][col] != color_from || image[row][col] == color_to
    image[row][col] = color_to
    rec(image, row+1, col, color_from, color_to)
    rec(image, row-1, col, color_from, color_to)
    rec(image, row, col+1, color_from, color_to)
    rec(image, row, col-1, color_from, color_to)

end

# @param {Integer[][]} image
# @param {Integer} sr
# @param {Integer} sc
# @param {Integer} color
# @return {Integer[][]}
def flood_fill(image, sr, sc, color)
    rec(image, sr, sc, image[sr][sc], color)
    image
end