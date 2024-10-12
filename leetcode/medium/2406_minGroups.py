from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start = []
        end = []

        for s, e in intervals:
            start.append(s)
            end.append(e)

        start = sorted(start)
        end = sorted(end)

        openned = 0
        res = 0
        s, e = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                openned += 1
                s += 1
                res = max(res, openned)
            else:
                e += 1
                openned -= 1

        return res


'''



[2,3],
[1,5],
[6,8],
[5,10],
[1,10]

---

[1,10]
[2,3], [5,10],
[1,5], [6,8],

---


[1,10]
[1,5],
[2,3],
[5,10],
[6,8],



]

'''


def test ():
    params = [
        {
            'input': [[5,10],[6,8],[1,5],[2,3],[1,10]],
            'output': 3,
        },
        {
            'input': [[1,3],[5,6],[8,10],[11,13]],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minGroups(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
