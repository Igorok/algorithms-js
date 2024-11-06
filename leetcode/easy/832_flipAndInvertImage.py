from typing import List
from json import dumps
import heapq

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def invert(num):
            return 0 if num == 1 else 1

        for i in range(len(image)):
            start = 0
            end = len(image[i]) - 1
            while start < end:
                image[i][start], image[i][end] = invert(image[i][end]), invert(image[i][start])
                start +=1
                end -= 1
            if start == end:
                image[i][start] = invert(image[i][start])

        return image

def test ():
    params = [
        {
            'input': [[1,1,0],[1,0,1],[0,0,0]],
            'output': [[1,0,0],[0,1,0],[1,1,1]],
        },
        {
            'input': [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]],
            'output': [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.flipAndInvertImage(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
