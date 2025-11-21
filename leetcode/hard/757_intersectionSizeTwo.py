from typing import List
import json
from collections import deque

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1], -x[0]))

        res = 2
        p2 = intervals[0][-1]
        p1 = p2-1

        for left, right in intervals:
            if left > p2:
                res += 2
                p1 = right-1
                p2 = right
            elif left == p2:
                res += 1
                p1 = p2
                p2 = right
            elif left < p2 and left > p1:
                res += 1
                p1 = p2
                p2 = right


        return res

'''

[[1,3],[3,7],[8,9]]
0 1 2 3 4 5 6 7 8 9 10
- 1 - 3; 2
- - - 3 - - - 7; 1
- - - - - - - - 8 9; 2


[[1,3],[1,4],[2,5],[3,5]]

0 1 2 3 4 5 6
- 1 - 3; 2
- 1 - - 4; 0
- - 2 - - 5; 0
- - - 3 - 5; 1

[[1,2],[2,3],[2,4],[4,5]]

0 1 2 3 4 5 6
- 1 2; 2
- - 2 3; 1
- - 2 - 4; 0
- - - - 4 5; 2

[1,2], [2,8], [3,5], [4,9], [5,6]

0 1 2 3 4 5 6 7 8 9 10
- 1 2; 1,2
- - - 3 - 5; 4,5
- - - - - 5 6; 6
- - 2 - - - - - 8;
- - - - 4 - - - - 9;


0 1 2 3 4 5 6 7 8 9 10
- 1 2;
- - - 3 - 5;
- - - - - 5 6;
- - 2 - - - - - 8;
- - - - 4 - - - - 9;



[[18, 24], [24, 33], [24, 33], [7, 34], [29, 37], [13, 37], [42, 43], [33, 44], [10, 47], [25, 48]]

23, 24, 33, 42, 43


24, 33
29, 37




[[2, 8], [5, 10], [3, 13]]
7, 8,

[[0, 3], [1, 4], [0, 4], [0, 4], [3, 7], [0, 7], [6, 8], [8, 9], [0, 9], [6, 10]]

2, 3, 7, 8,



'''


def test ():
    params = [
        {
            'input': [[1,3],[3,7],[8,9]],
            'output': 5,
        },
        {
            'input': [[1,3],[1,4],[2,5],[3,5]],
            'output': 3,
        },
        {
            'input': [[1,2],[2,3],[2,4],[4,5]],
            'output': 5,
        },
        {
            'input': [[1,2], [2,8], [3,5], [4,9], [5,6]],
            'output': 5,
        },
        {
            'input': [[33,44],[42,43],[13,37],[24,33],[24,33],[25,48],[10,47],[18,24],[29,37],[7,34]],
            'output': 6,
        },
        {
            'input': [[3,13],[2,8],[5,10]],
            'output': 2,
        },
        {
            'input': [[0,3],[0,4],[0,9],[8,9],[0,7],[1,4],[6,10],[0,4],[3,7],[6,8]],
            'output': 5,
        },
    ]
    solution = Solution()

    for param in params:
        intervals = param['input']
        result = solution.intersectionSizeTwo(intervals)
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
