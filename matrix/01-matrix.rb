def oob(mat, row, col)
    return true if row < 0 || col < 0
    return true if row >= mat.size || col >= mat[0].size
    return false
end

def bfs(mat, row, col, count=0)
    return Float::INFINITY if oob(mat, row, col) || mat[row][col] == -1
    return count if mat[row][col].zero?
    cell = mat[row][col]
    mat[row][col] = -1
    res = [bfs(mat, row+1, col, count+1),
    bfs(mat, row-1, col, count+1),
    bfs(mat, row, col+1, count+1),
    bfs(mat, row, col-1, count+1)].min
    mat[row][col] = cell
    res
end

# @param {Integer[][]} mat
# @return {Integer[][]}
def update_matrix(mat)
    0.upto(mat.size-1) do |row|
        0.upto(mat[0].size-1) do |col|
            next if mat[row][col].zero?
            mat[row][col] = bfs(mat, row, col)
        end
    end
    mat
end