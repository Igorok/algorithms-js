from typing import List

class Solution:
    def chalkReplacer_(self, chalk: List[int], k: int) -> int:
        chalkId = 0
        chalkSum = 0
        while chalkSum < k:
            chalkSum += chalk[chalkId]
            if chalkSum > k:
                return chalkId

            chalkId += 1
            if chalkId == len(chalk):
                chalkId = 0

        return chalkId

    def binarySearch(self, arr, num):
        start = 0
        end = len(arr) - 1
        while start <= end:
            middle = (start + end) // 2
            print(
                'middle', middle
            )
            if arr[middle] == num:
                print('arr[middle] == num', middle, num)
                return middle + 1

            if arr[middle] < num:
                start = middle + 1
            else:
                end = middle - 1

        print(
            'start', start,
            'end', end,
        )

        while arr[start] < num:
            start += 1

        print(
            'start', start,
            'end', end,
        )

        return start


    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prfixSum = [0] * len(chalk)
        oneLoopSum = 0
        for i in range(len(chalk)):
            oneLoopSum += chalk[i]
            prfixSum[i] = oneLoopSum
            if oneLoopSum > k:
                return i

        remainder = k % oneLoopSum

        print(
            'oneLoopSum', oneLoopSum,
            'remainder', remainder,
            'prfixSum', prfixSum,
        )

        # return self.chalkReplacer_(chalk, k)
        return self.binarySearch(prfixSum, remainder)



def test ():
    params = [
        {
            'input': [[5,1,5], 22],
            'output': 0,
        },
        {
            'input': [[3,4,1,2], 25],
            'output': 1,
        },
        {

            'input': [
                [93,87,71,59,95,27,74,37,24,40,95,36,12,96,19,36,78,43,25,22,18,93,69,72,34,44,11,60,62,26,97,67,45,100,48,14,51,81,17,6,88,63,79,80,36,14,49,21,41,23,10,7,83,50,50,95,91,100,14,73,40,55,46,84,81,56,73,89,97,18,22,48,78,54,27,91,19,65,88,28,80,21,12,55,23,3,36,38,64,45,84,83,54,77,45,30,73,59,31,90,20,39,57,27,35,55,93,12,46,43,17,95,25,90,97,74,58,1,92,38,15,85,59,52,79],
                984068366
            ],
            'output': 25,
        }
    ]
    solution = Solution()

    for param in params:
        chalk, k = param['input']
        result = solution.chalkReplacer(chalk, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
