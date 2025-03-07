from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = Counter(students)
        for sandwich in sandwiches:
            if counter[sandwich] > 0:
                counter[sandwich] -= 1
            else:
                return sum(counter.values())
        return sum(counter.values())
        