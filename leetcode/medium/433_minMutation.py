from typing import List
import json
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        chars = ('A','C','G','T')
        bankOfGene = set(bank)
        if startGene == endGene:
            return 0
        if endGene not in bankOfGene:
            return -1

        n = len(startGene)
        visited = set()
        geneQueue = deque()
        geneQueue.append((startGene, 0))

        while geneQueue:
            oldGene, step = geneQueue.popleft()
            if oldGene in visited:
                continue
            visited.add(oldGene)

            for i in range(n):
                for char in chars:
                    newGene = oldGene[:i] + char + oldGene[i+1:]
                    if (not newGene in bankOfGene) or (newGene in visited):
                        continue
                    if newGene == endGene:
                        return step + 1
                    geneQueue.append((newGene, step + 1))

        return -1


def test ():
    params = [
        {
            'input': ["AACCGGTT", "AACCGGTA", ["AACCGGTA"]],
            'output': 1,
        },
        {
            'input': ["AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]],
            'output': 2,
        },
        {
            'input': ["AACCGGTT", "AAACGGTA", ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]],
            'output': 4,
        },
        {
            'input': ["AACCTTGG", "AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        startGene, endGene, bank = param['input']
        result = solution.minMutation(startGene, endGene, bank)
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
