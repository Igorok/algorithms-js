from typing import List
from functools import cmp_to_key

'''
def cmp_items(a, b):
    a = (int(i) for i in a.split(':'))
    b = (int(i) for i in b.split(':'))

    print(
        'a', a,
        'b', b,
    )

    if a[0] > b.foo:
        return 1
    elif a.foo == b.foo:
        return 0
    else:
        return -1

cmp_items_py3 = cmp_to_key(cmp_items)

alist.sort(key = cmp_items_py3)
'''

class Solution:
    def convert(self, strTime):
        return [int(s) for s in strTime.split(':')]

    def cmp_items(self, a, b):
        if a[0] > b[0]:
            return 1
        elif a[0] == b[0]:
            return a[1] - b[1]
        else:
            return -1

    def diff_today(self, a, b):
        at = a[0] * 60 + a[1]
        bt = b[0] * 60 + b[1]
        return bt - at

    def diff_tomorrow(self, a, b):
        at = a[0] * 60 + a[1] + 24*60
        bt = b[0] * 60 + b[1]
        return at - bt

    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = [self.convert(s) for s in timePoints]
        arr.sort(key = cmp_to_key(self.cmp_items))

        minDiff = self.diff_tomorrow(arr[0], arr[-1])
        if minDiff == 0:
            return 0

        for i in range(1, len(arr)):
            diff = self.diff_today(arr[i - 1], arr[i])
            minDiff = min(minDiff, diff)
            if minDiff == 0:
                return 0

        print('arr', arr)
        print('diff_today', self.diff_today(arr[0], arr[1]))
        print('diff_tomorrow', self.diff_tomorrow(arr[0], arr[1]))

        return minDiff



def test ():
    params = [
        {
            'input': ["23:59","00:00"],
            'output': 1,
        },
        {
            'input': ["00:00","23:59","00:00"],
            'output': 0,
        },
        {
            'input': ["23:59","00:00", '00:10', '11:00'],
            'output': 1,
        },
        {

            'input': ["00:00","23:00","18:00","17:59"],
            'output': 1,
        }
    ]
    solution = Solution()

    for param in params:
        result = solution.findMinDifference(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
