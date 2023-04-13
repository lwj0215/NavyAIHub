#1260
from collections import deque
import copy


def dfs(edg, start):
    edge = copy.deepcopy(edg)
    for i in edge.keys():
        edge[i].reverse()
    result = []
    discovered = set([])
    result.append(start)
    discovered.add(start)
    stk = deque()
    for i in edge[start]:
        stk.append(i)
    while len(stk) != 0:
        t = stk.pop()
        if discovered.isdisjoint(([t])):
            result.append(t)
            discovered.add(t)
            for i in edge[t]:
                if discovered.isdisjoint(([i])):
                    stk.append(i)
    return result


def bfs(edge, start):
    result = []
    discovered = set([])
    que = deque()
    result.append(start)
    discovered.add(start)
    que.append(start)
    for i in edge[start]:
        que.append(i)
    while len(que):
        t = que.popleft()
        if discovered.isdisjoint(([t])):
            result.append(t)
            discovered.add(t)
            for i in edge[t]:
                if discovered.isdisjoint(([i])):
                    que.append(i)
    return result


nodes = {}
v, a, b = map(int, input().split())
for i in range(a):
    c, d = map(int, input().split())
    if c in nodes:
        nodes[c].append(d)
    else:
        nodes[c] = [d]
    if d in nodes :
        nodes[d].append(c)
    else:
        nodes[d] = [c]
if b not in nodes:
    print(b, b)
else:
    for i in nodes.keys():
        s = set(nodes[i])
        nodes[i] = list(s)
        nodes[i].sort()
    else:
        print(*dfs(nodes,b), sep=' ')
        print(*bfs(nodes,b), sep=' ')
