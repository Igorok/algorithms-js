from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

def generateNums():
    def getAvailbaleNumbers(length):
        if length == 0:
            return [[]]
        if length == 1:
            return [['1']]

        res = []
        for i in range(length, 0, -1):
            curr = [str(i)] * i
            nextLength = length - i

            if nextLength > i:
                break

            r = getAvailbaleNumbers(nextLength)
            for comb in r:
                if len(comb) != nextLength:
                    continue
                if comb and comb[0] == str(i):
                    continue

                res.append(curr + comb)

        return res

    nums = []
    for i in range(1, 8):
        res = getAvailbaleNumbers(i)
        nums = nums + res

    return nums

def getCombinations(nums):
    n = len(nums)
    visited = [0] * n
    res = set()

    def dfs(acc):
        if len(acc) == n:
            res.add(acc)
            return

        for i in range(n):
            if visited[i] == 1:
                continue

            visited[i] = 1

            dfs(acc + nums[i])

            visited[i] = 0

    dfs('')

    return [int(n) for n in res]


def getAllNums():
    nums = generateNums()

    print('nums', nums)

    allNums = []
    for arr in nums:
        allNums = allNums + getCombinations(arr)
    allNums.sort()


    return allNums

nums = getAllNums()
print('getAllNums', nums)

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        nums = [1, 22, 122, 212, 221, 333, 1333, 3133, 3313, 3331, 4444, 14444, 22333, 23233, 23323, 23332, 32233, 32323, 32332, 33223, 33232, 33322, 41444, 44144, 44414, 44441, 55555, 122333, 123233, 123323, 123332, 132233, 132323, 132332, 133223, 133232, 133322, 155555, 212333, 213233, 213323, 213332, 221333, 223133, 223313, 223331, 224444, 231233, 231323, 231332, 232133, 232313, 232331, 233123, 233132, 233213, 233231, 233312, 233321, 242444, 244244, 244424, 244442, 312233, 312323, 312332, 313223, 313232, 313322, 321233, 321323, 321332, 322133, 322313, 322331, 323123, 323132, 323213, 323231, 323312, 323321, 331223, 331232, 331322, 332123, 332132, 332213, 332231, 332312, 332321, 333122, 333212, 333221, 422444, 424244, 424424, 424442, 442244, 442424, 442442, 444224, 444242, 444422, 515555, 551555, 555155, 555515, 555551, 666666, 1224444, 1242444, 1244244, 1244424, 1244442, 1422444, 1424244, 1424424, 1424442, 1442244, 1442424, 1442442, 1444224, 1444242, 1444422, 1666666, 2124444, 2142444, 2144244, 2144424, 2144442, 2214444, 2241444, 2244144, 2244414, 2244441, 2255555, 2412444, 2414244, 2414424, 2414442, 2421444, 2424144, 2424414, 2424441, 2441244, 2441424, 2441442, 2442144, 2442414, 2442441, 2444124, 2444142, 2444214, 2444241, 2444412, 2444421, 2525555, 2552555, 2555255, 2555525, 2555552, 3334444, 3343444, 3344344, 3344434, 3344443, 3433444, 3434344, 3434434, 3434443, 3443344, 3443434, 3443443, 3444334, 3444343, 3444433, 4122444, 4124244, 4124424, 4124442, 4142244, 4142424, 4142442, 4144224, 4144242, 4144422, 4212444, 4214244, 4214424, 4214442, 4221444, 4224144, 4224414, 4224441, 4241244, 4241424, 4241442, 4242144, 4242414, 4242441, 4244124, 4244142, 4244214, 4244241, 4244412, 4244421, 4333444, 4334344, 4334434, 4334443, 4343344, 4343434, 4343443, 4344334, 4344343, 4344433, 4412244, 4412424, 4412442, 4414224, 4414242, 4414422, 4421244, 4421424, 4421442, 4422144, 4422414, 4422441, 4424124, 4424142, 4424214, 4424241, 4424412, 4424421, 4433344, 4433434, 4433443, 4434334, 4434343, 4434433, 4441224, 4441242, 4441422, 4442124, 4442142, 4442214, 4442241, 4442412, 4442421, 4443334, 4443343, 4443433, 4444122, 4444212, 4444221, 4444333, 5225555, 5252555, 5255255, 5255525, 5255552, 5522555, 5525255, 5525525, 5525552, 5552255, 5552525, 5552552, 5555225, 5555252, 5555522, 6166666, 6616666, 6661666, 6666166, 6666616, 6666661, 7777777]

        start = 0
        end = len(nums)
        res = -1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] > n:
                res = middle
                end = middle - 1
            else:
                start = middle + 1


        return nums[res]


def test ():
    params = [
        {
            'input': 1,
            'output': 22,
        },
        {
            'input': 1000,
            'output': 1333,
        },
        {
            'input': 3000,
            'output': 3133,
        },
        {
            'input': 59866,
            'output': 122333,
        },
    ]
    solution = Solution()

    for param in params:
        n = param['input']
        result = solution.nextBeautifulNumber(n)
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
