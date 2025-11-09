from typing import List
import json
from collections import deque, defaultdict
import math

class Solution_0:
    def originalDigits(self, s: str) -> str:
        numByWord = {
            'zero': '0',
            'two': '2',
            'four': '4',
            'six': '6',
            'eight': '8',

            'three': '3',
            'nine': '9',
            'seven': '7',
            'five': '5',
            'one': '1',
        }

        charsInWord = {}
        for word in numByWord:
            memo = {}
            for char in word:
                memo[char] = memo.get(char, 0) + 1
            charsInWord[word] = memo

        acc = {}
        for char in s:
            acc[char] = acc.get(char, 0) + 1

        def checkWord(word, acc):
            nonlocal charsInWord

            countOfChars = charsInWord[word]
            for char in countOfChars:
                if (not char in acc) or (countOfChars[char] > acc[char]):
                    return False

            return True

        def getWord(word, acc):
            for char in word:
                if acc[char] == 1:
                    del acc[char]
                else:
                    acc[char] -= 1

        res = ''
        cache = {}
        def dfs(acc, numbers):
            nonlocal res, numByWord, numByWord
            key = ''
            for k in acc:
                key += f"_{k}_{acc[k]}_"

            if key in cache:
                return cache[key]

            if len(acc) == 0:
                numbers.sort()
                res = ''.join(numbers)
                return True

            for word in numByWord:
                if not checkWord(word, acc):
                    continue
                numbers.append(numByWord[word])
                _acc = acc.copy()
                getWord(word, _acc)
                r = dfs(_acc, numbers)
                if r:
                    return r

                numbers.pop()

            cache[key] = False
            return False

        dfs(acc, [])

        return res


class Solution:
    def originalDigits(self, s: str) -> str:
        numByWord = {
            'zero': '0',
            'two': '2',
            'four': '4',
            'six': '6',
            'eight': '8',

            'three': '3',
            'seven': '7',

            'five': '5',

            'nine': '9',
            'one': '1',
        }

        charsInWord = {}
        for word in numByWord:
            memo = {}
            for char in word:
                memo[char] = memo.get(char, 0) + 1
            charsInWord[word] = memo

        def getWord(word, acc, cnt = 1):
            for char in word:
                if acc[char] == cnt:
                    del acc[char]
                else:
                    acc[char] -= cnt

        acc = {}
        for char in s:
            acc[char] = acc.get(char, 0) + 1

        numbers = []

        if 'z' in acc:
            numbers += ['0'] * acc['z']
            getWord('zero', acc, acc['z'])

        if 'w' in acc:
            numbers += ['2'] * acc['w']
            getWord('two', acc, acc['w'])

        if 'u' in acc:
            numbers += ['4'] * acc['u']
            getWord('four', acc, acc['u'])

        if 'x' in acc:
            numbers += ['6'] * acc['x']
            getWord('six', acc, acc['x'])

        if 'g' in acc:
            numbers += ['8'] * acc['g']
            getWord('eight', acc, acc['g'])

        if 'r' in acc:
            numbers += ['3'] * acc['r']
            getWord('three', acc, acc['r'])

        if 's' in acc:
            numbers += ['7'] * acc['s']
            getWord('seven', acc, acc['s'])

        if 'f' in acc:
            numbers += ['5'] * acc['f']
            getWord('five', acc, acc['f'])

        if 'i' in acc:
            numbers += ['9'] * acc['i']
            getWord('nine', acc, acc['i'])

        if 'o' in acc:
            numbers += ['1'] * acc['o']
            getWord('one', acc, acc['o'])


        numbers.sort()

        return ''.join(numbers)

'''
zero
one
two
three
four
five
six
seven
eight
nine


z - zero
w - two
u - four
x - six
g - eight



'''

def test ():
    params = [
        {
            'input': 'owoztneoer',
            'output': '012',
        },
        {
            'input': 'fviefuro',
            'output': '45',
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.originalDigits(s)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
