# @param {Integer[][]} points
# @param {Integer} k
# @return {Integer[][]}
def k_closest(points, k)
   res = []
   points.each do |point|
        x, y = point
        res << [x**2.abs + y**2.abs, point]
   end
   res.sort_by! { |arr| arr[0] }
   res.take(k).map { |arr| arr[1] }
end