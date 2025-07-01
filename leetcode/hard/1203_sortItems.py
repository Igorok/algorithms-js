import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        res = []

        myGroups = defaultdict(list)
        childrenForGroups = defaultdict(set)
        parentsForGroups = defaultdict(set)
        childrenForNodes = [0]*n
        parentsForNodes = [[] for i in range(n)]

        for pr in range(n):
            prKey = str(group[pr]) if group[pr] != -1 else 's_' + str(pr)
            myGroups[prKey].append(pr)

            for ch in beforeItems[pr]:
                chKey = str(group[ch]) if group[ch] != -1 else 's_' + str(ch)
                if chKey != prKey:
                    parentsForGroups[chKey].add(prKey)
                    childrenForGroups[prKey].add(chKey)
                else:
                    parentsForNodes[ch].append(pr)
                    childrenForNodes[pr] += 1


        groupsQueu = deque()

        for gr in myGroups:
            if not gr in childrenForGroups or len(childrenForGroups[gr]) == 0:
                groupsQueu.append(gr)

        while groupsQueu:
            gr = groupsQueu.popleft()

            items = []
            itemsQueue = deque()
            for node in myGroups[gr]:
                if childrenForNodes[node] == 0:
                    itemsQueue.append(node)

            while itemsQueue:
                item = itemsQueue.popleft()
                items.append(item)
                for pr in parentsForNodes[item]:
                    childrenForNodes[pr] -= 1
                    if childrenForNodes[pr] == 0:
                        itemsQueue.append(pr)

            if len(items) != len(myGroups[gr]):
                return []
            else:
                res += items

            for prGr in parentsForGroups[gr]:
                childrenForGroups[prGr].remove(gr)
                if len(childrenForGroups[prGr]) == 0:
                    groupsQueu.append(prGr)


        return res if len(res) == n else []


'''
-1:
0, 1: 5-1 6-0, 7

0:
3 6-0, 4 3-0, 6-0,6

1: 0
2 5-1, 5 3-0,


'''


def test ():
    params = [
        {
            'input': [
                8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3,6],[],[],[]],
            ],
            'output': [6,3,4,1,5,2,0,7],
        },
        {
            'input': [
                8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3],[],[4],[]],
            ],
            'output': [],
        },
        #
        {
            'input': [
                8, 2, [-1,-1,1,0,0,1,0,-1], [[],[5, 6],[5],[6],[3,6],[3],[],[]],
            ],
            'output': [6,3,4,5,2,1,0,7],
        },
    ]
    solution = Solution()

    for param in params:
        n, m, group, beforeItems = param['input']
        result = solution.sortItems(n, m, group, beforeItems)

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
