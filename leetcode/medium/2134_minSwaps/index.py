from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        partsLength = 0
        parts = []
        part = []
        for i in range(len(nums)):
            if nums[i] == 1:
                if len(part) == 0:
                    part.append(i)
            if nums[i] == 0:
                if len(part) == 1:
                    part.append(i - 1)
                    parts.append(part)
                    partsLength += (part[1] - part[0] + 1)
                    part = []

        if len(part) == 1:
            part.append(len(nums) - 1)
            parts.append(part)
            partsLength += (part[1] - part[0] + 1)
            part = []

        print(
            'parts', parts,
            'partsLength', partsLength
        )

        if len(parts) < 2:
            return 0

        outsideWhole = (parts[0][0] - 0) + (len(nums) - 1 - parts[-1][1])

        print(
            'outsideWhole', outsideWhole
        )

        if len(parts) == 2 and outsideWhole == 0:
            return 0

        wholes = []
        insideWhole = 0
        for i in range(1, len(parts)):
            whole = parts[i][0] - parts[i - 1][1] - 1
            wholes.append(whole)
            insideWhole += whole

        print(
            'wholes', wholes,
            'insideWhole', insideWhole,
        )


        return 0


'''

[0,1,0,1,1,0,0]

startWhole: [
    [start: 0, end: 1],
    [start: 5 end: 7]
]
size = (7 - 5) + (1 - 0) = 3

wholes: [
    [start: 2, end: 3, size: 1],
]

parts = 2

---

parts = [
[1,1],
[3,4]
]

startWhole = (1 - 0) + (7 - 4)





parts [[1, 1], [3, 4]] partsLength 3
outsideWhole 3
wholes [1] insideWhole 1
ERROR input [0, 1, 0, 1, 1, 0, 0] output 1 result 0

parts [[1, 3], [6, 7]] partsLength 5
outsideWhole 2
wholes [2] insideWhole 2
ERROR input [0, 1, 1, 1, 0, 0, 1, 1, 0] output 2 result 0

parts [[0, 1], [4, 4]] partsLength 3
outsideWhole 0
SUCCESS input [1, 1, 0, 0, 1] output 0 result 0

parts [[2, 2], [4, 4]] partsLength 2
outsideWhole 4
wholes [1] insideWhole 1
ERROR input [0, 0, 1, 0, 1, 0, 0] output 1 result 0

parts [[1, 1], [6, 6]] partsLength 2
outsideWhole 2
wholes [4] insideWhole 4
ERROR input [0, 1, 0, 0, 0, 0, 1, 0] output 1 result 0

parts [[1, 3], [6, 7], [11, 12]] partsLength 7
outsideWhole 1
wholes [2, 3] insideWhole 5
ERROR input [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1] output 3 result 0

parts [[1, 3], [6, 7], [10, 11], [13, 13], [16, 17]] partsLength 10
outsideWhole 1
wholes [2, 2, 1, 2] insideWhole 7
ERROR input [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1] output 5 result 0

[0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1]
10
l - 3, r -2
m = 10 - 5 = 5
w - 1, 5 -1

w1 p3 w2 p2 w2 p2 w1 p1 w2 p2
p1 p3 w2 p2 w2 p2 w1 w1 w2 p2
p1 p3 p2 p2 w2 w2 w1 w1 w2 p2

'''




def test ():
    params = [
        {
            'input': [0,1,0,1,1,0,0],
            'output': 1,
        },
        {
            'input': [0,1,1,1,0,0,1,1,0],
            'output': 2,
        },
        {
            'input': [1,1,0,0,1],
            'output': 0,
        },
        {
            'input': [0,0,1,0,1,0,0],
            'output': 1,
        },
        {
            'input': [0,1,0,0,0,0,1,0],
            'output': 1,
        },
        {
            'input': [0,1,1,1,0,0,1,1,0,0,0,1,1],
            'output': 2,
        },
        {
            'input': [0,1,1,1,0,0,1,1,0,0,1,1,0,1,0,0,1,1],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minSwaps(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
