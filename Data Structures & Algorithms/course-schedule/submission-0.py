
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # STEP 1: Create an empty graph
        # Each course gets its own list.
        # This list will store the courses that depend on it.

        graph = []

        for i in range(numCourses):
            graph.append([])


        # STEP 2: Create the indegree list
        # Indegree = number of prerequisites each course has.
        # Initially, we assume every course has 0 prerequisites.

        indegree = []

        for i in range(numCourses):
            indegree.append(0)


        # STEP 3: Build the graph using the prerequisites

        for pair in prerequisites:

            # Example: pair = [1, 0]
            # We must complete Course 0 before Course 1.

            course = pair[0]         # 1
            prerequisite = pair[1]   # 0

            # Store Course 1 inside graph[0].
            # This means completing Course 0 helps unlock Course 1.

            graph[prerequisite].append(course)

            # Course 1 now has one additional prerequisite.
            # Increase its indegree by 1.

            indegree[course] = indegree[course] + 1


        # STEP 4: Find all courses with no prerequisites

        queue = deque()

        for course in range(numCourses):

            # Indegree 0 means this course is ready to take.

            if indegree[course] == 0:
                queue.append(course)

        # Count how many courses we successfully complete.

        completed = 0


        # STEP 5: BFS - Take courses one by one

        # Keep running while there are courses ready to take.

        while len(queue) > 0:

            # Remove the first course from the queue.
            # We are now taking and completing this course.

            currentCourse = queue.popleft()

            # Increase the number of completed courses.

            completed = completed + 1

            # Find every course that depends on currentCourse.
            #
            # Example:
            # graph[0] = [1, 2]
            #
            # If currentCourse = 0,
            # nextCourse will first be 1 and then 2.

            for nextCourse in graph[currentCourse]:

                # We just completed one prerequisite
                # required by nextCourse.
                #
                # Reduce its remaining prerequisite count.

                indegree[nextCourse] = indegree[nextCourse] - 1

                # If the indegree becomes 0,
                # ALL prerequisites for this course are completed.
                #
                # It is now ready to take.

                if indegree[nextCourse] == 0:

                    # Add it to the queue.
                    # BFS will complete this course later.

                    queue.append(nextCourse)


        # STEP 6: Check whether all courses were completed

        # If completed equals numCourses,
        # every course was successfully taken.

        if completed == numCourses:
            return True

        # Otherwise, some courses could not be completed.
        # This happens when there is a dependency cycle.

        else:
            return False




        