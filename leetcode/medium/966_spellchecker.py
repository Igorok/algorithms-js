from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        allWords = set()
        capitalized = {}
        errored = {}

        def getChar(char):
            char = char.lower()
            return '_' if char in vowels else char

        for word in wordlist:
            allWords.add(word)

            w = word.lower()
            if not w in capitalized:
                capitalized[w] = word

            key = [getChar(char) for char in word]
            key = ''.join(key)
            if not key in errored:
                errored[key] = word

        res = []
        for query in queries:
            if query in allWords:
                res.append(query)
                continue

            q = query.lower()
            if q in capitalized:
                res.append(capitalized[q])
                continue


            key = [getChar(char) for char in query]
            key = ''.join(key)
            if key in errored:
                res.append(errored[key])
                continue

            res.append('')

        return res

'''



Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)


'''

def test ():
    params = [
        {
            'input': [
                ["KiTe","kite","hare","Hare"],
                ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
            ],
            'output': ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"],
        },
        {
            'input': [
                ["yellow"], ["YellOw"]
            ],
            'output': ["yellow"],
        },
    ]
    solution = Solution()

    for param in params:
        wordlist, queries = param['input']
        result = solution.spellchecker(wordlist, queries)
        correct = result == param['output']

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
