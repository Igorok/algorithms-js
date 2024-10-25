from typing import List
from json import dumps
from queue import Queue

class Solution:
    def predictPartyVictory_1(self, senate: str) -> str:
        desc = {
            'R': 'Radiant',
            'D': 'Dire',
        }

        senators = Queue()
        for char in senate:
            senators.put(char)

        while not senators.empty():
            f = senators.get()
            if senators.empty():
                return desc[f]
            s = senators.get()
            if f == s:
                return desc[f]
            senators.put(f)

        return ''

    def predictPartyVictory(self, senate: str) -> str:
        desc = {
            'R': 'Radiant',
            'D': 'Dire',
        }

        def round(senators):
            if len(senators) == 0:
                return ''
            if len(senators) == 1:
                return desc[senators[0]]

            nextRound = []
            stack = []
            ban = False
            for char in senators:
                if len(stack) == 0 or stack[-1] == char:
                    stack.append(char)
                    continue

                first = stack.pop()
                nextRound.append(first)
                ban = True

            if not ban:
                return desc[stack[0]]

            return round(stack + nextRound)

        return round(senate)

def test ():
    params = [
        {
            'input': 'RD',
            'output': 'Radiant',
        },
        {
            'input': 'RDD',
            'output': 'Dire',
        },
        {
            'input': 'DDRRRR',
            'output': 'Radiant',
        }
    ]
    solution = Solution()

    for param in params:
        result = solution.predictPartyVictory(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
