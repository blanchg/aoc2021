import os
import collections
import math
import time
start_time = time.time()

(file, _) = os.path.splitext(os.path.basename(__file__))
# f = open(f"{file}sample.txt", "r")
f = open(f"{file}.txt", "r")
lines = []
for rawline in f:
    line = str.strip(rawline)
    lines.append(line)
total = 0

graph = collections.defaultdict(list)


smallcaves = []
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph[start]:
        return []
    paths = []
    for node in graph[start]:
        if node not in smallcaves or node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
    
visitonce = ['start', 'end']
visited = collections.defaultdict(int)
def find_all_paths_v2(graph, start, end, path=[], visited=collections.defaultdict(int), visitedtwice=False):
    path = path + [start]
    visited[start] += 1
    if start == end:
        return [path]
    if not graph[start]:
        return []
    paths = []
    if start in smallcaves and visited[start] == 2:
        visitedtwice = True
    maxsmall = 1 if visitedtwice else 2
    
    for node in graph[start]:
        if (node in visitonce and node not in path) \
            or (node in smallcaves and visited[node] < maxsmall) \
            or (node not in smallcaves and node not in visitonce):
            newpaths = find_all_paths_v2(graph, node, end, path, collections.defaultdict(int, visited), visitedtwice)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

for line in lines:
    a,b = line.split('-')
    if a == str.lower(a):
        smallcaves.append(a)
    if b == str.lower(b):
        smallcaves.append(b)
    graph[a].append(b)
    graph[b].append(a)

paths = find_all_paths(graph, 'start', 'end')

# print(str.join('\n',[str.join(',', path) for path in paths]))
print(len(paths))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

graph = collections.defaultdict(list)
smallcaves = []
for line in lines:
    a,b = line.split('-')
    if a == str.lower(a) and a not in visitonce:
        smallcaves.append(a)
    if b == str.lower(b) and b not in visitonce:
        smallcaves.append(b)
    graph[a].append(b)
    graph[b].append(a)

paths = find_all_paths_v2(graph, 'start', 'end')
# print(str.join('\n',[str.join(',', path) for path in paths]))
print(len(paths))

print("--- %s seconds ---" % (time.time() - start_time))