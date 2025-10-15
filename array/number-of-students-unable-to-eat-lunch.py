from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        for _ in range(len(students)*5):
            if len(sandwiches) == 0:
                return len(students)
            student = students.popleft()
            if sandwiches and sandwiches[0] == student:
                sandwiches.popleft()
            else:
                students.append(student)
        return len(students)