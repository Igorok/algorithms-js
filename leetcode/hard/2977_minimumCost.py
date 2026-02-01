from typing import List
import json
import heapq


class TrieNode:
    def __init__(self):
        self.children = {}
        self.string_id = -1

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        m = len(original)

        string_to_id = {}
        curr_id = 0

        root = TrieNode()

        def get_id(s):
            nonlocal curr_id
            if s not in string_to_id:
                string_to_id[s] = curr_id
                node = root
                for char in s:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.string_id = curr_id
                curr_id += 1
            return string_to_id[s]

        # fill trie
        for i in range(m):
            get_id(original[i])
            get_id(changed[i])

        num_nodes = curr_id
        # distance between strings
        dist = [[float('inf')] * num_nodes for i in range(num_nodes)]
        # distance to it self = 0
        for i in range(num_nodes):
            dist[i][i] = 0

        # looking a min distance for duplicates
        for i in range(m):
            s1, s2, c = original[i], changed[i], cost[i]
            u, v = string_to_id[s1], string_to_id[s2]
            dist[u][v] = min(dist[u][v], c)

        # floyd marshal, shortest path between every of nodes
        # middle node
        for k in range(num_nodes):
            # start node
            for i in range(num_nodes):
                # no direct path between nodes
                if dist[i][k] == float('inf'):
                    continue
                # end node
                for j in range(num_nodes):
                    if dist[k][j] < float('inf'):
                        # if path from i,j > i,k + k,j
                        # use a path though the middle node
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


        # dp
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == float('inf'):
                continue

            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])

            node_s = root
            node_t = root

            for j in range(i, n):
                char_s = source[j]
                char_t = target[j]

                if char_s not in node_s.children or char_t not in node_t.children:
                    break

                node_s = node_s.children[char_s]
                node_t = node_t.children[char_t]

                if node_s.string_id != -1 and node_t.string_id != -1:
                    u, v = node_s.string_id, node_t.string_id
                    if dist[u][v] != float('inf'):
                        dp[j+1] = min(dp[j+1], dp[i] + dist[u][v])

        return dp[n] if dp[n] != float('inf') else -1


def test ():
    params = [
        {
            'input': ["abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]],
            'output': 28,
        },
        {
            'input': ["abcdefgh", "acdeeghh", ["bcd","fgh","thh"], ["cde","thh","ghh"], [1,3,5]],
            'output': 9,
        },
        {
            'input': ["abcdefgh", "addddddd", ["bcd","defgh"], ["ddd","ddddd"], [100,1578]],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        source, target, original, changed, cost = param['input']
        result = solution.minimumCost(source, target, original, changed, cost)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
