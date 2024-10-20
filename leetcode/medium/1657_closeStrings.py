from typing import List
from json import dumps


class Solution:
    def closeStrings_wrong(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        s1 = ''.join(sorted(list(set(word1))))
        s2 = ''.join(sorted(list(set(word2))))

        return s1 == s2

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        def getData(word):
            chars = {}
            for char in word:
                count = chars.get(char, 0)
                chars[char] = count + 1
            allChars = []
            allCount = []
            for char, count in chars.items():
                allChars.append(char)
                allCount.append(str(count))

            return [
                ''.join(sorted(allChars)),
                ''.join(sorted(allCount)),
            ]

        data1 = getData(word1)
        data2 = getData(word2)

        print(
            'data1', data1,
            'data2', data2,
        )

        return data1[0] == data2[0] and data1[1] == data2[1]

'''

abbzzca
babzzcz

abbzzca
abbzzcz


cabbba
abbccc

aabbbc
abbccc


'''


def test ():
    params = [
        {
            'input': ["abc", "bca"],
            'output': True,
        },
        {
            'input': ["a", "aa"],
            'output': False,
        },
        {
            'input': ["cabbba", "abbccc"],
            'output': True,
        },
        {
            'input': ["abbzzca", "babzzcz"],
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        word1, word2 = param['input']
        result = solution.closeStrings(word1, word2)
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
