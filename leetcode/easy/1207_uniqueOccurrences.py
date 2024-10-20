from typing import List
from json import dumps


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}
        for v in arr:
            c = occ.get(v, 0) + 1
            occ[v] = c

        uniq = set()
        for k in occ:
            v = occ[k]
            if not v in uniq:
                uniq.add(v)
            else:
                return False

        return True


def test ():
    params = [
        {
            'input': [1,2,2,1,1,3],
            'output': True,
        },
        {
            'input': [1,2],
            'output': False,
        },
        {
            'input': [-3,0,1,-3,1,1,1,-3,10,0],
            'output': True,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.uniqueOccurrences(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
