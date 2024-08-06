from collections import defaultdict
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = defaultdict(int)
        for s in arr:
            count[s] += 1

        i = 0
        for s, n in count.items():
            if n == 1:
                i += 1
                if k == i:
                    return s

        return ''



def test ():
    params = [
        {
            'input': [["d","b","c","b","c","a"], 2],
            'output': 'a',
        },
        {
            'input': [["aaa","aa","a"], 1],
            'output': 'aaa',
        },
        {
            'input': [["a","b","a"], 3],
            'output': '',
        },
    ]
    solution = Solution()

    for param in params:
        arr, k = param['input']
        result = solution.kthDistinct(arr, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
