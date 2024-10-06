from typing import List

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True

        if len(sentence1) == len(sentence2):
            return False

        big, small = '', ''
        if len(sentence1) > len(sentence2):
            big = sentence1
            small = sentence2
        else:
            big = sentence2
            small = sentence1

        if big[0:len(small)] == small and big[len(small)] == ' ':
            return True

        if big[(len(big) - len(small)):] == small and big[(len(big) - len(small) - 1)] == ' ':
            return True

        start = 0
        end = len(small) - 1

        while start < len(small):
            if small[start] == big[start] and start + 1 < len(small) and small[start + 1] == big[start + 1]:
                start += 1
            else:
                break

        print(
            'small', small,
            'big', big,
            'start', start,
            'end', end,
            'small[start]', small[start],
            'big[start]', big[start],
        )


        if start != 0 and small[start] != ' ' and big[start] != ' ':
            return False

        endBig = len(big) - 1
        while end > start:
            if small[end] == big[endBig] and end > -1 and small[end - 1] == big[endBig - 1]:
                end -= 1
                endBig -= 1
            else:
                break

        if start != end:
            return False

        if big[endBig] != ' ':
            return False


        print(
            'start', start,
            'end', end,
            'small[end]', small[end],
            'big[endBig]', big[endBig],
        )

        return True


def test ():
    params = [
        {
            'input': ["My name is Haley", "My Haley"],
            'output': True,
        },
        {
            'input': ["of", "A lot of words"],
            'output': False,
        },
        {
            'input': ["Eating right now", "Eating"],
            'output': True,
        },
        {
            'input': ["B", "ByI BMyQIqce b bARkkMaABi vlR RLHhqjNzCN oXvyK zRXR q ff B yHS OD KkvJA P JdWksnH"],
            'output': False,
        },
        {
            'input': ["f", "a C"],
            'output': False,
        },
        {
            'input': ["A", "a b c A"],
            'output': True,
        },
        {
            'input': ["aa", "a Aa"],
            'output': False,
        },
        {
            'input': ["xD iP tqchblXgqvNVdi", "FmtdCzv Gp YZf UYJ xD iP tqchblXgqvNVdi"],
            'output': True,
        },
        {
            'input': ["aaa", "aa bbb ccc aaa"],
            'output': True,
        },
        {
            'input': ["A a a", "Aa a"],
            'output': False,
        },



    ]
    solution = Solution()

    for param in params:
        sentence1, sentence2 = param['input']
        result = solution.areSentencesSimilar(sentence1, sentence2)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
