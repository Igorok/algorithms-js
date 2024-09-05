from typing import List
import json
import math

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        cols = math.ceil(len(original) / n)
        if cols != m:
            return []

        result = []
        tmp = []
        for i in range(len(original)):
            if len(tmp) == n:
                result.append(tmp)
                tmp = []
            tmp.append(original[i])

        if len(tmp) != 0:
            result.append(tmp)
            tmp = []

        return result



def test ():
    params = [
        {
            'input': [[1,2,3,4], 2, 2],
            'output': [[1,2],[3,4]],
        },
        {
            'input': [[1,2,3], 1, 3],
            'output': [[1,2,3]],
        },
        {
            'input': [[1,2], 1, 1],
            'output': [],
        },
    ]
    solution = Solution()

    for param in params:
        original, m, n = param['input']
        result = solution.construct2DArray(original, m, n)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
