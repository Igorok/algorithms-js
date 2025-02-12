from typing import List
from json import dumps
import heapq
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        aCode = ord('a')
        chars = [chr(ord('a') + i) for i in range(26)]
        words = set(wordList)

        wordsQueue = deque()
        wordsQueue.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)

        while wordsQueue:
            oldWord, count = wordsQueue.popleft()

            for i in range(n):
                for char in chars:
                    newWord = oldWord[:i] + char + oldWord[i+1:]

                    if newWord in visited or not newWord in words:
                        continue
                    if newWord == endWord:
                        return count + 1
                    visited.add(newWord)

                    wordsQueue.append((newWord, count + 1))

        return 0

def test ():
    params = [
        {
            'input': ["hit", "cog", ["hot","dot","dog","lot","log","cog"]],
            'output': 5,
        },
        {
            'input': ["hit", "cog", ["hot","dot","dog","lot","log"]],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        beginWord, endWord, wordList = param['input']
        result = solution.ladderLength(beginWord, endWord, wordList)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
