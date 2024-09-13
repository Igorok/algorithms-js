from typing import List
from json import dumps

class Solution:
    def _xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []

        binArr = [bin(v)[2:] for v in arr]

        prefixArr = [0]*len(arr)
        prefixArr[0] = arr[0]
        for i in range(1, len(prefixArr)):
            prefixArr[i] = prefixArr[i - 1] ^ arr[i]
        prefixArr = [bin(v)[2:] for v in prefixArr]

        print(
            'arr', arr,
            'binArr', binArr,
            'prefixArr', prefixArr,
        )


        for q in queries:
            s, e = q
            v = arr[s]
            for i in range(s+1, e + 1):
                v = v ^ arr[i]
            res.append(v)

        return res

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []

        binArr = [bin(v)[2:] for v in arr]

        prefixArr = [0]*len(arr)
        prefixArr[0] = arr[0]
        for i in range(1, len(prefixArr)):
            prefixArr[i] = prefixArr[i - 1] ^ arr[i]
        # prefixArr = [bin(v)[2:] for v in prefixArr]

        print(
            'arr', arr,
            'binArr', binArr,
            'prefixArr', prefixArr,
        )


        for q in queries:
            s, e = q
            v = prefixArr[e]
            if s > 0:
                v = v ^ prefixArr[s-1]
            res.append(v)

        return res

'''

arr [1, 3, 4, 8]
binArr ['1', '11', '100', '1000']
prefixArr ['1', '10', '110', '1110']

1-2
011^100 = 111 = 1+2+4=7

110

SUCCESS input [[1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]] output [2, 7, 14, 8] result [2, 7, 14, 8]

arr [4, 8, 2, 10]
binArr ['100', '1000', '10', '1010']
prefixArr ['100', '1100', '1110', '100']

SUCCESS input [[4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]] output [8, 0, 4, 4] result [8, 0, 4, 4]

'''

def test ():
    params = [
        {
            'input': [[1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]],
            'output': [2,7,14,8],
        },
        {

            'input': [[4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]],
            'output': [8,0,4,4],
        },
    ]
    solution = Solution()

    for param in params:
        arr, queries = param['input']
        result = solution.xorQueries(arr, queries)
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
