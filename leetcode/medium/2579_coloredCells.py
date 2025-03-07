from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def coloredCells(self, n: int) -> int:
        count = 1
        for i in range(2, n+1):
            count += i*4 - 4

        return count

'''
1

1
1 1
prev + 2*4-4 = 1+8-4 = 5

1
1 1
1 1 1
prev + 3*4-4 = 5+12-4=13

1
1 1
1 1 1
1 1 1 1
prev + 4*4-4 = 13+12=25



1, 5, 13, 25, 41

1

      1
    1 1 1
      1

      1
    1 1 1
  1 1 1 1 1
    1 1 1
      1

          1
        1 1 1
      1 1 1 1 1
    1 1 1 1 1 1 1
      1 1 1 1 1
        1 1 1
          1


            1
          1 1 1
        1 1 1 1 1
      1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1
      1 1 1 1 1 1 1
        1 1 1 1 1
          1 1 1
            1


'''


def test ():
    params = [
        {
            'input': 1,
            'output': 1,
        },
        {
            'input': 2,
            'output': 5,
        },
        {
            'input': 3,
            'output': 13,
        },
        {
            'input': 4,
            'output': 25,
        },
        {
            'input': 5,
            'output': 41,
        },
    ]
    solution = Solution()

    for param in params:
        n = param['input']
        result = solution.coloredCells(n)
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
