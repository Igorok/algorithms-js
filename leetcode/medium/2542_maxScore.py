from typing import List
from json import dumps
import heapq

# We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
class Solution:
    def maxScore_1(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0

        def rec(arr):
            nonlocal res
            if len(arr) == k:
                arr1 = [nums1[i] for i in arr]
                arr2 = [nums2[i] for i in arr]
                r = sum(arr1) * min(arr2)
                res = max(res, r)
            else:
                for i in range(arr[-1]+1, len(nums1)):
                    rec(arr + [i])

        for i in range(len(nums1)):
            rec([i])

        return res

    def maxScore_2(self, nums1: List[int], nums2: List[int], k: int) -> int:
        newArr = [
            (nums1[i], nums2[i], i) for i in range(len(nums1))
        ]
        newArr.sort(key=lambda x: -(x[0]*x[1]))

        # print('newArr', newArr)

        s = 0
        m = 10e5
        for i in range(k):
            id = newArr[i][2]
            s += nums1[id]
            m = min(m, nums2[id])


        res = s * m

        return res


    def maxScore_3(self, nums1: List[int], nums2: List[int], k: int) -> int:
        h = []
        nums = []
        for i in range(len(nums1)):
            nums.append((nums1[i], nums2[i]))
            h.append((-nums1[i], (nums1[i], nums2[i])))

        nums.sort(key=lambda x: x[1])
        heapq.heapify(h)
        res = 0

        for i in range(len(nums) - k + 1):
            frst, sec = nums[i]

            maxSum = []
            sumOfF = frst
            dupl = False
            while len(maxSum) < k - 1:
                item = heapq.heappop(h)
                id, arr = item
                f, s = arr
                if s < sec:
                    continue
                if f == frst and s == sec and not dupl:
                    dupl = True
                    continue
                maxSum.append(item)
                sumOfF += f

            # print('h', h)

            r = sec * sumOfF


            # print(
            #     'sec', sec,
            #     'sum(sumOfFirst)', sum(sumOfFirst),
            #     'r', r,
            # )

            res = max(r, res)

            for item in maxSum:
                heapq.heappush(h, item)

        return res


    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = [(nums1[i], nums2[i]) for i in range(len(nums1))]
        nums.sort(key=lambda x: -x[1])

        h = []
        res = -1
        sumOfFirst = 0
        for i in range(len(nums)):
            first, second = nums[i]

            sumOfFirst += first

            if len(h) > k - 1:
                v = heapq.heappop(h)
                sumOfFirst -= v
            if len(h) == k - 1:
                res = max(res, sumOfFirst * second)

            heapq.heappush(h, first)
        return res

def test ():
    params = [
        {
            'input': [[1,1,1,100,100,100], [10,10,10,1,1,1], 3],
            'output': 300,
        },
        {
            'input': [[1,1,1,100,100,100], [10,10,10,0,0,0], 3],
            'output': 30,
        },
        {
            'input': [[1,3,3,2], [2,1,3,4], 3],
            'output': 12,
        },
        {
            'input': [[4,2,3,1,1], [7,5,10,9,6], 1],
            'output': 30,
        },
        {
            'input': [
                [93,463,179,2488,619,2006,1561,137,53,1765,2304,1459,1768,450,1938,2054,466,331,670,1830,1550,1534,2164,1280,2277,2312,1509,867,2223,1482,2379,1032,359,1746,966,232,67,1203,2474,944,1740,1775,1799,1156,1982,1416,511,1167,1334,2344],
                [345,229,976,2086,567,726,1640,2451,1829,77,1631,306,2032,2497,551,2005,2009,1855,1685,729,2498,2204,588,474,693,30,2051,1126,1293,1378,1693,1995,2188,1284,1414,1618,2005,1005,1890,30,895,155,526,682,2454,278,999,1417,1682,995],
                42

            ],
            'output': 26653494,
        },
        {
            'input': [
                [2,1,14,12],
                [11,7,13,6],
                3,
            ],
            'output': 168,
        },
    ]
    solution = Solution()

    for param in params:
        nums1, nums2, k = param['input']
        result = solution.maxScore(nums1, nums2, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
