from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        memo = [0] * (len(books) + 1)
        memo[1] = books[0][1]

        for i in range(2, len(memo)):
            book = books[i - 1]
            memo[i] = book[1] + memo[i - 1]
            unitedHeight = book[1]

            width = shelfWidth - book[0]

            j = i - 1
            prevBook = books[j - 1]

            while width - prevBook[0]>= 0 and j > 0:
                unitedHeight = max(unitedHeight, prevBook[1])
                memo[i] = min(memo[j - 1] + unitedHeight, memo[i])

                width -= prevBook[0]
                j -= 1
                prevBook = books[j - 1]

        print('memo', memo)

        return memo[len(books)]



def test ():
    params = [
        {
            'input': [[[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4],
            'output': 6,
        },
        {
            'input': [[[1,3],[2,4],[3,2]], 6],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minHeightShelves(param['input'][0], param['input'][1])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()

'''
4, 6

[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]
1     3     4     5     5     5     6



'''
