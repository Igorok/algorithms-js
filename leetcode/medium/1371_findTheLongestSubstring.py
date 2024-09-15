from typing import List

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        chars = {
            'a': 1, # 00001
            'e': 2, # 00010
            'i': 4, # 00100
            'o': 8, # 01000
            'u': 16, # 10000
        }
        # all possible combinations
        combinations = [-1] * (1 + 2**5)
        comb = 0
        maxLength = 0
        for i, char in enumerate(s):
            num = chars[char] if char in chars else 0
            comb ^= num

            # we meet one vowel, like 'a' and have combination '00001'
            if comb != 0 and combinations[comb] == -1:
                combinations[comb] = i
            maxLength = max(maxLength, i - combinations[comb])

        return maxLength


def test ():
    params = [
        {
            'input': 'eleetminicoworoep',
            'output': 13,
        },
        {
            'input': 'leetcodeisgreat',
            'output': 5,
        },
        {
            'input': 'bcbcbc',
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.findTheLongestSubstring(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
