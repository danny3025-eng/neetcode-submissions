class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        def dfs(i):
            if states[i] == VISITING:
                return False
            elif states[i] == VISITED:
                return True
            states[i] = VISITING

            for nei in g[i]:
                if not dfs(nei):
                    return False
            
            states[i] = VISITED
            order.append(i)
            return True
    
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order


# from collections import defaultdict  # Import defaultdict from collections module to create a dictionary with default values (lists)

# numCourses = 4  # Total number of courses to take (labeled 0 to 3)

# prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]  # List of pairs [a, b], meaning course b is a prerequisite for course a


# def findorder(numCourses, prerequisites):
#   order = []  # List that will store the valid topological order of courses
#   g = defaultdict(list)  # Adjacency list mapping each course to its dependent courses

#   for a, b in prerequisites:  # Loop through each prerequisite pair [a, b]
#     g[a].append(
#         b
#     )  # Add b as a dependency for course a (or depending on convention, edge from a to b)

#   UNVISITED, VISITING, VISITED = (
#       0,
#       1,
#       2,
#   )  # Define constants for node states: 0 = unvisited, 1 = currently visiting (in recursion stack / cycle check), 2 = completely visited

#   states = [
#       UNVISITED
#   ] * numCourses  # Initialize the state of every course as UNVISITED (0)

#   def dfs(i):  # Define Depth-First Search function for course index i
#     if (
#         states[i] == VISITING
#     ):  # If the current course is already in the VISITING state, a cycle is detected
#       return False  # Return False because a valid ordering is impossible with a cycle
#     elif (
#         states[i] == VISITED
#     ):  # If the current course has already been completely processed
#       return True  # Return True as it's already safely ordered

#     states[i] = VISITING  # Mark the current course as currently VISITING (1)

#     for nei in (
#         g[i]
#     ):  # Iterate through all neighbors/prerequisites of the current course
#       if not dfs(nei):  # Recursively run DFS on the neighbor
#         return False  # If a cycle is found down the chain, propagate False up

#     states[i] = VISITED  # Mark the current course as completely VISITED (2)
#     order.append(
#         i
#     )  # Append the course to the order list after its dependencies are resolved
#     return True  # Return True indicating successful traversal of this path

#   for i in range(numCourses):  # Iterate through all courses from 0 to numCourses-1
#     if not dfs(i):  # Run DFS for course i; if a cycle is detected
#       return []  # Return an empty list since no valid schedule exists

#   return (
#       order  # Return the final computed list of courses in valid topological order
#   )


# print(
#     findorder(numCourses, prerequisites)
# )  # Call findorder function and print the resulting course order
# # Output : [0,2,1,3]