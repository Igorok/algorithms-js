from typing import List
from collections import defaultdict


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        consonantsCount = defaultdict(int)
        vowelsCount = defaultdict(int)

        maxVow = 0
        maxCons = 0
        for char in s:
            if char in vowels:
                vowelsCount[char] += 1
                maxVow = max(maxVow, vowelsCount[char])
            else:
                consonantsCount[char] += 1
                maxCons = max(maxCons, consonantsCount[char])

        return maxVow + maxCons


def test ():
    params = [
        {
            'input': 'successes',
            'output': 6,
        },
        {
            'input': 'aeiaeia',
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maxFreqSum(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
