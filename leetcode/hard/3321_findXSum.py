from typing import List
import json
from collections import deque, defaultdict
from sortedcontainers import SortedList


class Solution_0:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        sumOfWindow = 0
        maxFreq = SortedList()
        minFreq = SortedList()
        countFreq = {}

        for i in range(k):
            num = nums[i]
            countFreq[num] = countFreq.get(num, 0) + 1

        for key in countFreq:
            minFreq.add((countFreq[key], key))

        for i in range(min(x, len(minFreq))):
            cnt, val = minFreq.pop()
            sumOfWindow += cnt * val
            maxFreq.add((-cnt, -val))

        res = [sumOfWindow]

        for i in range(k, n):
            prevId = i - k
            prevNum = nums[prevId]
            num = nums[i]

            if prevNum == num:
                res.append(sumOfWindow)
                continue

            cnt = countFreq[prevNum]

            countFreq[prevNum] = cnt - 1
            if (-cnt, -prevNum) in maxFreq:
                sumOfWindow -= cnt * prevNum
                maxFreq.remove((-cnt, -prevNum))
            else:
                minFreq.remove((cnt, prevNum))

            if cnt > 1:
                minFreq.add((cnt-1, prevNum))


            cnt = countFreq.get(num, 0)
            countFreq[num] = cnt + 1

            if (-cnt, -num) in maxFreq:
                maxFreq.remove((-cnt, -num))
                sumOfWindow -= cnt * num
            elif (cnt, num) in minFreq:
                minFreq.remove((cnt, num))

            minFreq.add((cnt+1, num))

            def isPop():
                if len(maxFreq) == 0 or len(minFreq) == 0:
                    return False

                if -maxFreq[-1][0] < minFreq[-1][0]:
                    return True

                if  -maxFreq[-1][0] == minFreq[-1][0] and -maxFreq[-1][1] < minFreq[-1][1]:
                    return True

                return False

            while isPop():
                cnt, num = maxFreq.pop()
                sumOfWindow -= cnt * num
                minFreq.add((-cnt, -num))

                cnt, num = minFreq.pop()
                sumOfWindow += cnt * num
                maxFreq.add((-cnt, -num))

            while len(maxFreq) < x and len(minFreq) != 0:
                cnt, num = minFreq.pop()
                sumOfWindow += cnt * num
                maxFreq.add((-cnt, -num))

            res.append(sumOfWindow)

        return res




class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        sumOfWindow = 0
        maxFreq = SortedList()
        minFreq = SortedList()
        countFreq = {}

        for i in range(k):
            num = nums[i]
            countFreq[num] = countFreq.get(num, 0) + 1

        for key in countFreq:
            minFreq.add((countFreq[key], key))

        for i in range(min(x, len(minFreq))):
            cnt, val = minFreq.pop()
            sumOfWindow += cnt * val
            maxFreq.add((-cnt, -val))

        res = [sumOfWindow]

        for i in range(k, n):
            prevId = i - k
            prevNum = nums[prevId]
            num = nums[i]

            if prevNum == num:
                res.append(sumOfWindow)
                continue

            cnt = countFreq[prevNum]

            countFreq[prevNum] = cnt - 1
            if (-cnt, -prevNum) in maxFreq:
                sumOfWindow -= cnt * prevNum
                maxFreq.remove((-cnt, -prevNum))
            else:
                minFreq.remove((cnt, prevNum))

            if cnt > 1:
                minFreq.add((cnt-1, prevNum))

            cnt = countFreq.get(num, 0)
            countFreq[num] = cnt + 1
            if (-cnt, -num) in maxFreq:
                maxFreq.remove((-cnt, -num))
                sumOfWindow -= cnt * num
            elif (cnt, num) in minFreq:
                minFreq.remove((cnt, num))

            minFreq.add((cnt+1, num))

            def isPop():
                if len(maxFreq) == 0 or len(minFreq) == 0:
                    return False

                if -maxFreq[-1][0] < minFreq[-1][0]:
                    return True

                if  -maxFreq[-1][0] == minFreq[-1][0] and -maxFreq[-1][1] < minFreq[-1][1]:
                    return True

                return False

            while isPop():
                cnt, num = maxFreq.pop()
                sumOfWindow -= cnt * num
                minFreq.add((-cnt, -num))

                cnt, num = minFreq.pop()
                sumOfWindow += cnt * num
                maxFreq.add((-cnt, -num))

            while len(maxFreq) < x and len(minFreq) != 0:
                cnt, num = minFreq.pop()
                sumOfWindow += cnt * num
                maxFreq.add((-cnt, -num))

            res.append(sumOfWindow)

        return res

def test ():
    params = [
        {
            'input': [[5,5,5,5],3,2],
            'output': [15,15],
        },
        {
            'input': [[1,9,10,4],2,1],
            'output': [9,10,10],
        },
        {
            'input': [[1,1,2,2,3,4,2,3], 6, 2],
            'output': [6,10,12],
        },
        {
            'input': [[3,8,7,8,7,5], 2, 2],
            'output': [11,15,15,15,12],
        },
    ]
    solution = Solution()

    for param in params:
        nums, k, x = param['input']
        result = solution.findXSum(nums, k, x)
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
