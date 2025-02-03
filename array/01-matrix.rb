require 'thread'

def oob(mat, r, c)
    return true if r < 0 || c < 0
    return true if r >= mat.size || c >= mat[0].size
    return false
end

# @param {Integer[][]} mat
# @return {Integer[][]}
def update_matrix(mat)
    queue = Queue.new
    directions = [[1,0], [-1,0], [0,1], [0,-1]]

    mat.each.with_index do |row, r|
        row.each.with_index do |col, c|
            if mat[r][c] == 0
                queue << [r, c, 0]
            else
                mat[r][c] = Float::INFINITY
            end
        end
    end

    until queue.empty?
        r, c, dist = queue.pop
        if mat[r][c] > dist
            mat[r][c] = dist
        end
        directions.each do |d|
            dir_r, dir_c = d
            next_r, next_c, next_dist = dir_r+r, dir_c+c, dist+1
            next if oob(mat, next_r, next_c)
            if mat[next_r][next_c] == Float::INFINITY
                queue << [next_r, next_c, next_dist]
            end
        end
    end
    mat
end
