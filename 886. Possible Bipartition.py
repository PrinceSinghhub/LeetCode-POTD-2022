class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Create an adjacency list representation of the graph
        adj_list = [[] for _ in range(n)]
        for a, b in dislikes:
            adj_list[a - 1].append(b - 1)
            adj_list[b - 1].append(a - 1)

        # Initialize a colors array to store the colors of the vertices
        # 0 = not visited, 1 = set A, 2 = set B
        colors = [0] * n

        # Perform BFS starting from each vertex
        for start in range(n):
            # If the vertex has not been visited, perform BFS
            if colors[start] == 0:
                # Initialize the queue with the starting vertex
                queue = deque([start])
                colors[start] = 1

                # Perform BFS
                while queue:
                    vertex = queue.popleft()
                    for neighbor in adj_list[vertex]:
                        # If the neighbor has not been visited, assign it to the other set and add it to the queue
                        if colors[neighbor] == 0:
                            colors[neighbor] = 3 - colors[vertex]
                            queue.append(neighbor)
                        # If the neighbor is in the same set as the current vertex, return False (not bipartite)
                        elif colors[neighbor] == colors[vertex]:
                            return False
        # If BFS was successful for all vertices, return True (bipartite)
        return True
