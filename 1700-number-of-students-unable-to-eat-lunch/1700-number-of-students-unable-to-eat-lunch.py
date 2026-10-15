from collections import deque
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        queue=deque(students)
        rotations=0
        i=0
        while queue and rotations < len(queue):
            student=queue.popleft()
            if student==sandwiches[i]:
                i+=1
                rotations=0
            else:
                rotations+=1
                queue.append(student)

        return len(queue)