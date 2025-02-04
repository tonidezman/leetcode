# @param {Integer[][]} intervals
# @param {Integer[]} new_interval
# @return {Integer[][]}
def insert(intervals, new_interval)
    res = []
    intervals.each.with_index do |interval, i|
        if interval[0] > new_interval[1]
            res.append(new_interval)
            return res + intervals[i..-1]
        end

        if interval[1] >= new_interval[0]
            new_interval = [[interval[0], new_interval[0]].min, [interval[1], new_interval[1]].max]
        else
            res.append(interval)
        end
    end
    res.append(new_interval)
    res
end