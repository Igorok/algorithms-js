from typing import List
import json
from collections import deque, defaultdict

class Solution_0:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        frByUser = [[] for i in range(m)]
        learnByUser = [[0]*(n+1) for i in range(m)]

        langByUser = []
        for i in range(m):
            langs = [0]*(n+1)
            for l in languages[i]:
                langs[l] += 1
            langByUser.append(langs)

        for f1, f2 in friendships:
            f1 -= 1
            f2 -= 1

            canSpeak = False
            for l in range(n+1):
                if langByUser[f1][l] == 1 and langByUser[f2][l] == 1:
                    canSpeak = True
                    break

            if not canSpeak:
                for l in range(n+1):
                    if langByUser[f1][l] == 1:
                        learnByUser[f2][l] += 1
                    if langByUser[f2][l] == 1:
                        learnByUser[f1][l] += 1

            frByUser[f1].append(f2)
            frByUser[f2].append(f1)

        res = 0
        for u in range(m):
            for f in frByUser[u]:
                canSpeak = False

                for l in range(n+1):
                    if langByUser[u][l] == 1 and langByUser[f][l] == 1:
                        canSpeak = True
                        break

                if canSpeak:
                    continue

                learnU = -1
                learnF = -1

                for l in range(n+1):
                    if learnByUser[u][l] != 0 and (learnU == -1 or learnByUser[u][l] > learnByUser[u][learnU]):
                        learnU = l
                    if learnByUser[f][l] != 0 and (learnF == -1 or learnByUser[f][l] > learnByUser[f][learnF]):
                        learnF = l

                if learnByUser[u][learnU] > learnByUser[f][learnF]:
                    langByUser[u][learnU] = 1
                    learnByUser[u][learnU] = 0
                else:
                    langByUser[f][learnF] = 1
                    learnByUser[f][learnF] = 0

                res += 1


        return res



class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)

        langsByUser = []
        for u in range(m):
            langs = [0]*(n+1)
            for l in languages[u]:
                langs[l] = 1
            langsByUser.append(langs)


        canNotSpeak = set()
        for f1, f2 in friendships:
            f1 -= 1
            f2 -= 1
            canSpeak = False

            for l in range(n+1):
                if langsByUser[f1][l] == 1 and langsByUser[f2][l] == 1:
                    canSpeak = True
                    break

            if canSpeak:
                continue

            canNotSpeak.add(f1)
            canNotSpeak.add(f2)


        frequency = [0]*(n+1)
        commonLang = 0
        for u in canNotSpeak:
            for l in range(n+1):
                if langsByUser[u][l] == 1:
                    frequency[l] += 1

                    if frequency[commonLang] < frequency[l]:
                        commonLang = l


        return len(canNotSpeak) - frequency[commonLang]




'''
f
1: 2,3;
2: 1,3;
3: 1,2;
l
1: 1; +2
2: 2;
3: 1,2;

---

n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]

f
1: 4,2;
2: 1,3;
3: 4,2;
4: 1,3;
l
1: 2; +3
2: 1,3;
3: 1,2; +3
4: 3;

---
f
1: 2,3;
2: 1,3;
3: 1,2;
l:
1: 1;
2: 2; +1;
3: 1;

require:
1: {2: 1};
2: {1: 2};
3: {2: 1};

'''

def test ():
    params = [
        {
            'input': [2, [[1],[2],[1]], [[1,2],[1,3],[2,3]]],
            'output': 1,
        },
        {
            'input': [2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]]],
            'output': 1,
        },
        {
            'input': [3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]]],
            'output': 2,
        },
        {
            'input': [17, [[4,7,2,14,6],[15,13,6,3,2,7,10,8,12,4,9],[16],[10],[10,3],[4,12,8,1,16,5,15,17,13],[4,13,15,8,17,3,6,14,5,10],[11,4,13,8,3,14,5,7,15,6,9,17,2,16,12],[4,14,6],[16,17,9,3,11,14,10,12,1,8,13,4,5,6],[14],[7,14],[17,15,10,3,2,12,16,14,1,7,9,6,4]], [[4,11],[3,5],[7,10],[10,12],[5,7],[4,5],[3,8],[1,5],[1,6],[7,8],[4,12],[2,4],[8,9],[3,10],[4,7],[5,12],[4,9],[1,4],[2,8],[1,2],[3,4],[5,10],[2,7],[1,7],[1,8],[8,10],[1,9],[1,10],[6,7],[3,7],[8,12],[7,9],[9,11],[2,5],[2,3]]],
            'output': 4,
        },
        {
            'input': [
                2,
                [[2],[1],[2,1],[1],[1,2],[1],[2],[1],[1],[2],[1,2],[1,2],[1,2],[2,1],[1],[2],[1,2]],
                [[15,16],[4,13],[3,16],[5,14],[1,7],[2,11],[3,15],[4,16],[7,9],[6,13],[6,16],[4,10],[6,9],[5,6],[7,12],[6,12],[3,7],[4,7],[8,10]]
            ],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        n, languages, friendships = param['input']
        result = solution.minimumTeachings(n, languages, friendships)
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
