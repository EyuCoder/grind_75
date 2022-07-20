# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        map = {}

        def dfs(node):
            if node in map:
                return map[node]
            copy = Node(node.val)
            map[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        return dfs(node) if node else None
