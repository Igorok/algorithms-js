from typing import List
import math

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = ''
        queue = [
            [a, 'a'], [b, 'b'], [c, 'c']
        ]
        queue = sorted(queue, key=lambda x: -x[0])


        print(
            'queue', queue,
        )

        groupCount = math.ceil(queue[0][0] / 2)

        while groupCount != 0:
            if len(s) and s[-1] == queue[0][1]:
                break

            if queue[0][0] == 1:
                queue[0][0] = 0
                s += queue[0][1]
            else:
                s += (queue[0][1] * 2)
                queue[0][0] -= 2

            if queue[1][0] + queue[2][0] >= groupCount:
                if queue[1][0] > 0:
                    if queue[1][0] == 1:
                        queue[1][0] -= 1
                        s += queue[1][1]
                    else:
                        s += (queue[1][1] * 2)
                        queue[1][0] -= 2
                if queue[1][0] + queue[2][0] >= groupCount and queue[2][0] > 0:
                    if queue[2][0] == 1:
                        queue[2][0] -= 1
                        s += queue[2][1]
                    else:
                        s += (queue[2][1] * 2)
                        queue[2][0] -= 2
            else:
                if queue[1][0] != 0:
                    queue[1][0] -= 1
                    s += queue[1][1]
                elif queue[2][0] != 0:
                    queue[2][0] -= 1
                    s += queue[2][1]

            groupCount -= 1

        return s


def test ():
    params = [
        {
            'input': [1, 1, 7],
            'output': 'ccaccbcc',
        },
        {
            'input': [7, 1, 0],
            'output': 'aabaa',
        },
        {
            'input': [8, 3, 0],
            'output': 'aabaabaabaa',
        },
        {
            'input': [8, 8, 0],
            'output': 'aabbaabbaabbaabb',
        },
        {
            'input': [4, 4, 3],
            'output': 'aabbccaabbc',
        },


    ]
    solution = Solution()

    for param in params:
        a, b, c = param['input']
        result = solution.longestDiverseString(a, b, c)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
