#!/usr/bin/python

''' author: cgautam
    description: run dfs on a given graph
    graph is given in the following format:
    first line of input = N = total number of nodes in the graph
    next N lines = adjacency list of node i on line i
    nodes indices start from 0
'''

# get inputs and create adjacency list
N = input()
adj_list = {}
for i in range (0, N):
    adj_list[i] = map(int, raw_input().split(' '))

print adj_list  #debug statement

def dfs(root):
    parent = [-1] * N
    visited = ['N'] * N
    stack = list()
    stack.append(root)

    visited[root] = 'Y'
    while stack:
        el = stack.pop()
        visited[el] = 'Y'
        for i,c in enumerate(adj_list[el]):
            if visited[c] == 'N':
                stack.insert(0,c)
                parent[c] = el
    print parent
    print visited

dfs(0)

