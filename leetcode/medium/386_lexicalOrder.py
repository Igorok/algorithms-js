from typing import List
from json import dumps

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        def rec(start):
            if start > n:
                return

            result.append(start)
            s = start * 10
            e = (start + 1) * 10
            for i in range(s, e):
                if i > n:
                    break
                rec(i)

        for i in range(1, 10):
            rec(i)

        return result


'''

                0
        1                                                           2       3       ...         9
10      11      12      13      ..      19
100
1000

'''


def test ():
    params = [
        {
            'input': 13,
            'output': [1,10,11,12,13,2,3,4,5,6,7,8,9],
        },
        {
            'input': 2,
            'output': [1,2],
        },
        {
            'input': 100,
            'output': [1,10,100,11,12,13,14,15,16,17,18,19,2,20,21,22,23,24,25,26,27,28,29,3,30,31,32,33,34,35,36,37,38,39,4,40,41,42,43,44,45,46,47,48,49,5,50,51,52,53,54,55,56,57,58,59,6,60,61,62,63,64,65,66,67,68,69,7,70,71,72,73,74,75,76,77,78,79,8,80,81,82,83,84,85,86,87,88,89,9,90,91,92,93,94,95,96,97,98,99],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.lexicalOrder(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
