from typing import List
from json import dumps
from collections import deque, defaultdict


class Solution_0:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = defaultdict(int)
        for arr in responses:
            for word in set(arr):
                count[word] += 1

        arr = [(count[key], key) for key in count]
        arr.sort(key=lambda x: (-x[0], x[1]))
        return arr[0][1]

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        res = ''
        count = defaultdict(int)
        for arr in responses:
            for word in set(arr):
                count[word] += 1

                if count[word] > count[res] or (count[word] == count[res] and res > word):
                    res = word
        return res

def test ():
    params = [
        {
            'input': [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]],
            'output': 'good',
        },
        {
            'input': [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]],
            'output': 'bad',
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.findCommonResponse(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
