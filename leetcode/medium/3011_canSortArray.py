from typing import List
from json import dumps
import heapq

class Solution:
    def canSortArray_1(self, nums: List[int]) -> bool:
        l = len(nums)
        def getSetOfBits(num):
            s = 0
            while num != 0:
                s += num % 2
                num = num // 2
            return s

        arrWithBits = [None]*l
        for i in range(l):
            print('getSetOfBits', nums[i], getSetOfBits(nums[i]))
            arrWithBits[i] = (
                nums[i], i, getSetOfBits(nums[i])
            )
        arrWithBits.sort(key=lambda x: x[0])


        print('arrWithBits', arrWithBits)

        for i in range(l):
            curr = arrWithBits[i]
            if i > 0:
                prev = arrWithBits[i - 1]
                if prev[1] > curr[1] and prev[2] != curr[2]:
                    return False
            if i != l - 1:
                nxt = arrWithBits[i + 1]
                if nxt[1] < nxt[1] and prev[2] != curr[2]:
                    return False

        return True

    def canSortArray_2(self, nums: List[int]) -> bool:
        l = len(nums)
        cache = {}
        def getSetOfBits(num):
            if num in cache:
                return cache[num]
            s = 0
            while num != 0:
                s += num % 2
                num = num // 2
            cache[num] = s
            return s

        res = True
        def mergeSort(arr):
            nonlocal res
            if len(arr) < 2 or not res:
                return arr
            pivot = len(arr) // 2
            left = mergeSort(arr[:pivot])
            right = mergeSort(arr[pivot:])

            newArr = []
            i = j = 0
            while i < len(left) and j < len(right):
                lb = getSetOfBits(left[i])
                rb = getSetOfBits(right[j])

                if left[i] <= right[j]:
                    newArr.append(left[i])
                    i += 1
                else:
                    if rb != lb:
                        res = False
                        return arr
                    newArr.append(right[j])
                    j +=1

            while i < len(left):
                newArr.append(left[i])
                i += 1

            while j < len(right):
                newArr.append(right[j])
                j +=1

            return newArr

        newNums = mergeSort(nums)
        print('newNums', newNums)

        return res

    def canSortArray(self, nums: List[int]) -> bool:
        cache = {}
        def getSetOfBits(num):
            if num in cache:
                return cache[num]
            return bin(num).count('1')

        numMax, prevMax = nums[0], nums[0]

        for num in nums:
            print(
                'num', num,
                'getSetOfBits(numMax)', getSetOfBits(num),
            )
            if num > numMax:
                if getSetOfBits(num) != getSetOfBits(numMax):
                    prevMax = numMax
                numMax = num
                continue

            if num < numMax and getSetOfBits(num) != getSetOfBits(numMax):
                return False
            if num < prevMax and getSetOfBits(num) != getSetOfBits(prevMax):
                return False


        return True

def test ():
    params = [
        {
            'input': [8,4,2,30,15],
            'output': True,
        },
        {
            'input': [1,2,3,4,5],
            'output': True,
        },
        {
            'input': [3,16,8,4,2],
            'output': False,
        },
        {
            'input': [100,3,1],
            'output': False,
        },
        {
            'input': [136,256,10],
            'output': False,
        },
        {
            'input': [1,201,251,191],
            'output': False,
        },
        {
            'input': [100,161,11,69,7,21,148,76,231,238,63,246,95,246,231,219,255,255,255,255,255,255,255,255,255],
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.canSortArray(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
