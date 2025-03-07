from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        for _ in range(len(sandwiches)*5):
            if len(students) == 0:
                return 0
            student = students.popleft()
            if student == sandwiches[0]:
                sandwiches.popleft()
                continue
            students.append(student)
        return len(students)