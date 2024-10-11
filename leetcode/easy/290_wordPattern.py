from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def getWordsPattern(words):
            print('words', words)

            i = 0
            wordsMap = {}
            wordsMap[words[0]] = i
            sentense = ''

            for w in words:
                if w in wordsMap:
                    num = wordsMap[w]
                    sentense += str(num)
                else:
                    i += 1
                    wordsMap[w] = i
                    sentense += str(i)

            print('sentense', sentense)

            return sentense

        p1 = getWordsPattern(list(pattern))
        p2 = getWordsPattern(s.split(' '))

        return p1 == p2


def test ():
    params = [
        {
            'input': ["abba", "dog cat cat dog"],
            'output': True,
        },
        {
            'input': ["abba", "dog cat cat fish"],
            'output': False,
        },
        {
            'input': ["abba", "dog cat cat fish"],
            'output': False,
        },
        {
            'input': ["e", "eukera"],
            'output': True,
        },
        {
            'input': ["deadbeef", "d e a d b e e f"],
            'output': True,
        },
    ]
    solution = Solution()

    for param in params:
        pattern, s = param['input']
        result = solution.wordPattern(pattern, s)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
