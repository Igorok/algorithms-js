from typing import List
import json

'''
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        allPref = {}

        for w in words:
            for i in range(1, len(w) + 1):
                if not w[:i] in allPref:
                    allPref[w[:i]] = 0
                allPref[w[:i]] += 1

        res = []
        for w in words:
            s = 0
            for i in range(1, len(w) + 1):
                s += allPref[w[:i]]
            res.append(s)

        return res
'''

class Node:
    def __init__(self, char):
        self.char = char
        self.count = 0
        self.nodes = [None]*26

    def insert(self, char):
        num = ord(char) - ord('a')
        if self.nodes[num] != None:
            node = self.nodes[num]
        else:
            node = Node(char)
            self.nodes[num] = node
        node.count += 1
        return node

class Tree:
    def __init__(self):
        self.nodes = [None]*26

    def insert(self, char):
        num = ord(char) - ord('a')
        if self.nodes[num] != None:
            node = self.nodes[num]
        else:
            node = Node(char)
            self.nodes[num] = node
        node.count += 1
        return node



class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        tree = Tree()

        for word in words:
            node = tree.insert(word[0])
            for i in range(1, len(word)):
                node = node.insert(word[i])

        res = []
        for word in words:
            num = ord(word[0]) - ord('a')
            node = tree.nodes[num]
            s = node.count
            for i in range(1, len(word)):
                num = ord(word[i]) - ord('a')
                node = node.nodes[num]
                s += node.count
            res.append(s)

        return res

def test ():
    params = [
        {
            'input': ["abc","ab","bc","b"],
            'output': [5,4,3,2],
        },
        {
            'input': ["abcd"],
            'output': [4],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.sumPrefixScores(param['input'])
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
