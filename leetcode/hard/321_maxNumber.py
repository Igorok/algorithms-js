from typing import List
import json
from collections import deque, defaultdict

class Solution_0:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)

        def findMax(arr, start, end):
            acc = []

            for i in range(start, end):
                if not acc:
                    acc.append((i, arr[i]))
                    continue
                if acc[-1][1] > arr[i]:
                    continue
                else:
                    acc.append((i, arr[i]))
            return acc


        def compare(arr1, arr2):
            if not arr1:
                return 2
            if not arr2:
                return 1

            length = min(len(arr1), len(arr2))


            for i in range(1, length+1):
                if arr1[-i][1] == arr2[-i][1]:
                    continue

                if i == 1:
                    return 1 if arr1[-i][1] > arr2[-i][1] else 2
                else:
                    return 2 if arr1[-i][1] > arr2[-i][1] else 1


            id1 = arr1[-i][0]
            id2 = arr2[-i][0]

            if id1 == n1-1:
                return 2
            if id2 == n2-1:
                return 1

            return 1 if nums1[id1+1] >= nums2[id2+1] else 2

        def findMinId(arr, target):
            start = 0
            end = len(arr) -1
            res = arr[start][0]

            while start <= end:
                middle = (start + end) // 2
                if arr[middle][1] == target:
                    res = arr[middle][0]
                    end = middle - 1
                else:
                    start = middle + 1

            return res

        res = []

        s1 = 0
        s2 = 0

        while len(res) < k:
            required = k - len(res)
            l1 = n1 - s1
            l2 = n2 - s2
            e1 = min(n1, n1 + l2 - required + 1)
            e2 = min(n2, n2 + l1 - required + 1)

            max1 = findMax(nums1, s1, e1)
            max2 = findMax(nums2, s2, e2)

            selected = compare(max1, max2)

            # print(
            #     'max1', max1,
            #     'max2', max2,
            #     'selected', selected,
            # )

            if selected == 1:
                res.append(max1[-1][1])
                id = findMinId(max1, max1[-1][1])
                s1 = id + 1
            else:
                res.append(max2[-1][1])
                id = findMinId(max2, max2[-1][1])
                s2 = id + 1



        return res


'''

[[3,4,6,5], [9,1,2,5,8,3], 5],

'''

class Solution_1:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)

        def getMax(arr, start, length):
            n = len(arr)
            if start == n:
                return ('', [])

            stack = []
            for i in range(start, n):
                while stack and stack[-1][0] < arr[i] and len(stack)-1 + n-i >= length:
                    stack.pop()
                stack.append((arr[i], i))

            ids = [v[1] for v in stack]
            text = [str(v[0]) for v in stack]

            return (''.join(text), ids)

        def mergeStrings(str1, str2):
            i = 0
            j = 0
            res = ''

            while i < len(str1) and j < len(str2):
                if str1[i:] >= str2[j:]:
                    res += str1[i]
                    i += 1
                else:
                    res += str2[j]
                    j += 1

            res += str1[i:] + str2[j:]

            return res

        res = []

        s1 = 0
        s2 = 0
        while len(res) < k:
            remainder = k - len(res)
            l1 = n1 - s1
            l2 = n2 - s2

            req1 = remainder - l2
            req2 = remainder - l1

            text1, ids1 = getMax(nums1, s1, req1)
            rem1 = ''.join([str(nums2[i]) for i in range(s2, n2)])
            # rem1 = getMax(nums2, s2, l2 - len(text1))
            # rem1 = rem1[0]
            merged1 = '' if text1 == '' else mergeStrings(text1, rem1)[:remainder]
            # merged1 = merged1[:remainder]
            # text1 += rem1

            text2, ids2 = getMax(nums2, s2, req2)
            rem2 = ''.join([str(nums1[i]) for i in range(s1, n1)])
            # rem2 = getMax(nums1, s1, l1 - len(text1))
            # rem2 = rem2[0]
            merged2 = '' if text2 == '' else mergeStrings(text2, rem2)[:remainder]
            # merged2 = merged2[:remainder]
            # text2 += rem2

            if merged1 > merged2 or (merged1 == merged2 and text1 > text2):
                res.append(nums1[ids1[0]])
                s1 = ids1[0] + 1
            else:
                res.append(nums2[ids2[0]])
                s2 = ids2[0] + 1

        return res



class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)

        def getMaxStr(arr, length):
            n = len(arr)
            stack = []

            for i in range(n):
                while stack and stack[-1] < arr[i] and len(stack) - 1 + n-i >= length:
                    stack.pop()
                if len(stack) < length:
                    stack.append(arr[i])

            return ''.join([str(num) for num in stack])

        def mergeStrings(str1, str2):
            i = 0
            j = 0
            res = ''

            while i < len(str1) and j < len(str2):
                if str1[i:] >= str2[j:]:
                    res += str1[i]
                    i += 1
                else:
                    res += str2[j]
                    j += 1

            res += str1[i:] + str2[j:]

            return res

        res = ''


        for i in range(k+1):
            j = k - i

            left = '' if i == 0 else getMaxStr(nums1, i)
            right = '' if j == 0 else getMaxStr(nums2, j)

            if len(left) + len(right) < k:
                continue

            merged = mergeStrings(left, right)
            if merged > res:
                res = merged

        return [int(v) for v in res]


'''

'input': [[1,7,9,3], [3,8,9,3,7], 7],
'output': [9,3,8,9,3,7,3],

1,7,9,3
3,8,9,3,7


9,3,7 + 1,7,9,3
9,3 + 3,8,9,3,7

'''

def test ():
    params = [
        {
            'input': [[8,1,8,8,6], [4], 2],
            'output': [8,8],
        },
        {
            'input': [[1,2,6,6], [1,9,2,4], 4],
            'output': [9,6,6,4],
        },
        {
            'input': [[1,7,9,3], [3,8,9,3,7], 7],
            'output': [9,3,8,9,3,7,3],
        },
        {
            'input': [[3,4,6,5], [9,1,2,5,8,3], 5],
            'output': [9,8,6,5,3],
        },
        {
            'input': [[6,7], [6,0,4], 5],
            'output': [6,7,6,0,4],
        },
        {
            'input': [[3,9], [8,9], 3],
            'output': [9,8,9],
        },
        {
            'input': [[8,9], [3,9], 3],
            'output': [9,8,9],
        },
        {
            'input': [[5,5,1], [4,0,1], 3],
            'output': [5,5,4],
        },
        {
            'input': [[2,5,6,4,4,0], [7,3,8,0,6,5,7,6,2], 15],
            'output': [7,3,8,2,5,6,4,4,0,6,5,7,6,2,0],
        },
        {
            'input': [
                [5,0,2,1,0,1,0,3,9,1,2,8,0,9,8,1,4,7,3],
                [7,6,7,1,0,1,0,5,6,0,5,0],
                31,
            ],
            'output': [7,6,7,5,1,0,2,1,0,1,0,5,6,0,5,0,1,0,3,9,1,2,8,0,9,8,1,4,7,3,0],
        },
    ]
    solution = Solution()

    for param in params:
        nums1, nums2, k = param['input']
        result = solution.maxNumber(nums1, nums2, k)
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
