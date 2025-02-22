from typing import List
import json
from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder_0(self, traversal: str):

        if not traversal:
            return None

        def getNumbers(text):
            levels = []
            level = 0
            val = ''
            start = 0
            for i in range(len(text)):
                if len(levels) == level:
                    levels.append([])

                if text[i].isnumeric():
                    val += text[i]
                    if i == len(text) - 1:
                        levels[level].append(int(val))
                        val = ''
                        level = 0
                elif text[i-1].isnumeric():
                    levels[level].append(int(val))
                    val = ''
                    level = 1
                else:
                    level += 1

            return levels



        l = getNumbers(traversal)


        return []

    def recoverFromPreorder(self, traversal: str):

        if not traversal:
            return None

        def getNumbers(text):
            levels = []
            level = 0
            val = ''
            start = 0

            def addNode():
                node = TreeNode(int(val))
                levels[level].append(node)

                if level != 0:
                    ancestor = levels[level-1][-1]
                    if not ancestor.left:
                        ancestor.left = node
                    else:
                        ancestor.right = node

            for i in range(len(text)):
                if len(levels) == level:
                    levels.append([])

                if text[i].isnumeric():
                    val += text[i]
                    if i == len(text) - 1:
                        addNode()
                        val = ''
                        level = 0
                elif text[i-1].isnumeric():
                    addNode()
                    val = ''
                    level = 1
                else:
                    level += 1

            return levels



        l = getNumbers(traversal)

        print(l[0][0])

        return []


'''
1-2--3--4-5--6--7

[1]
[2,5]
[3,4,6,7]


1-2--3---4-5--6---7
[1]
[2,5]
[3,6]
[4,7]

1-401--349---90--88
[1]
[401,]
[349,88]
[90]


'''



def test ():
    params = [
        {
            'input': '1-2--3--4-5--6--7',
            'output': [1,2,5,3,4,6,7],
        },
        {
            'input': '1-2--3---4-5--6---7',
            'output': [1,2,5,3,None,6,None,4,None,7],
        },
        {
            'input': '1-401--349---90--88',
            'output': [1,401,None,349,88,90],
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.recoverFromPreorder(nums)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
