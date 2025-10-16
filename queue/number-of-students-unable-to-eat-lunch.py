from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        n = len(students)
        res = n
        for sandwich in sandwiches:
            count = 0
            while count < n and students[0] != sandwich:
                count += 1
                students.append(students.popleft())

            if students[0] == sandwich:
                students.popleft()
                res -= 1
            else:
                break
        return res