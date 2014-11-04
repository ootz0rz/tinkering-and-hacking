# Basically, defined as:
# {
#     'NODE A': set(['CONNECTING NODE 1', 'CONNECTING NODE 2', ...]),
#     'NODE B': set(['CONNECTING NODE 1', 'CONNECTING NODE 2', ...]),
#     ...
# }
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start, goal, path=None):
    if path is None:
        path = [start]

    if start == goal:
        yield path

    for node in (graph[start] - set(path)):
        for res in dfs(graph, node, goal, path + [node]):
            yield res

def bfs(graph, start, goal):
    Q = [(start, [start])]

    while Q:
        v, path = Q.pop(0)

        for node in (graph[v] - set(path)):
            if node == goal:
                yield path + [node]
            else:
                Q.append((node, path + [node]))