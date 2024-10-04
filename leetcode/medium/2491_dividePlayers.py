from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        teamCount = len(skill) / 2
        s = sum(skill)
        ts = s // teamCount
        if s % teamCount != 0:
            return -1

        r = 0
        data = sorted(skill)
        start = 0
        end = len(data) - 1
        while start < end:
            if data[start] + data[end] != ts:
                return -1
            r += data[start] * data[end]
            start += 1
            end -= 1

        return r

    def dividePlayers_(self, skill: List[int]) -> int:
        teamCount = len(skill) // 2
        countByNums = {}
        allSum = 0
        for v in skill:
            count = countByNums.get(v, 0)
            countByNums[v] = count + 1
            allSum += v

        teamSum = allSum // teamCount

        if (allSum % teamCount) != 0:
            return -1

        r = 0
        compared = 0
        for v in skill:
            count = countByNums.get(v, 0)

            if count == 0:
                continue

            nei = teamSum - v
            neiCount = countByNums.get(nei, 0)
            if neiCount == 0:
                return -1

            compared += 1
            r += (v * nei)

            countByNums[v] = count - 1
            countByNums[nei] = countByNums.get(nei, 0) - 1

            if compared == teamCount:
                break

        return r


def test ():
    params = [
        {
            'input': [3,2,5,1,3,4],
            'output': 22,
        },
        {
            'input': [3,4],
            'output': 12,
        },
        {
            'input': [1,1,2,3],
            'output': -1,
        },
        {
            'input': [2,4,1,3],
            'output': 10,
        },
        {
            'input': [2,1,5,2],
            'output': -1,
        },
        {
            'input': [3,4,3,2,1,5,1,5],
            'output': 27,
        },


    ]
    solution = Solution()

    for param in params:
        result = solution.dividePlayers(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
