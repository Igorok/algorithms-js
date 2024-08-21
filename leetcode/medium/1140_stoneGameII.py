from typing import List

class Solution:
    def stoneGameII_(self, piles: List[int]) -> int:
        self.alice = 0
        self.bob = 0

        def rec (isAlice, id, m, aCount, bCount):
            print(
                'self.alice', self.alice,
                'self.bob', self.bob,
                isAlice, id, m, aCount, bCount,
            )

            if id >= len(piles):
                if isAlice:
                    self.alice = max(self.alice, aCount)
                else:
                    self.bob = max(self.bob, bCount)
                return

            for i in range(1, m * 2 + 1):
                c = aCount if isAlice else bCount
                for j in range(i):
                    if id + j >= len(piles):
                        break
                    c += piles[id + j]

                if isAlice:
                    rec(False, id + i, i, c, bCount)
                else:
                    rec(True, id + i, i, aCount, c)

        rec(True, 0, 1, 0, 0)

        print(
            'self.alice', self.alice,
            'self.bob', self.bob,)


        return self.alice

    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}

        def rec(isAlice, id, m):
            if id == len(piles):
                return 0

            if (isAlice, id, m) in cache:
                return cache[(isAlice, id, m)]

            total = 0
            res = 0 if isAlice else float('inf')
            for i in range(1, m * 2 + 1):
                if id + i > len(piles):
                    break

                total += piles[id + i - 1]
                if isAlice:
                    res = max(res, total + rec(not isAlice, id + i, max(i, m)))
                else:
                    res = min(res, rec(not isAlice, id + i, max(i, m)))

            cache[(isAlice, id, m)] = res
            return res

        return rec(True, 0, 1)


'''



2,7,9,4,4

2
2 7

7 9
9 4 4

---
1,2,3,4,5,100

1
1 2

2 3
3 4 5 100





'''

def test ():
    params = [
        {
            'input': [2,7,9,4,4],
            'output': 10,
        },
        {
            'input': [1,2,3,4,5,100],
            'output': 104,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.stoneGameII(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
