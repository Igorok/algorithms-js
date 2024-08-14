from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.sorted = sorted(list(nums))[-k : len(nums)]
        if len(self.sorted) > k:
            self.sorted = self.sorted[-k : len(nums)]

        print(
            'self.k', self.k,
            'self.nums', self.nums,
            'self.sorted', self.sorted,
        )

    def add(self, val: int) -> int:
        self.nums.append(val)
        if (len(self.sorted) < self.k or val > self.sorted[0]):
            self.sorted.append(val)
            self.sorted = sorted(self.sorted)
            if len(self.sorted) > self.k:
                self.sorted = self.sorted[-self.k : len(self.sorted)]

        return self.sorted[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


def test ():
    params = [
        {
            'input': [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
            'output': [4, 5, 5, 8, 8],
        },
        {
            'input': [[1,[]],[-3],[-2],[-4],[0],[4]],
            'output': [-3,-2,-2,0,4]
,
        },
    ]



    for param in params:
        kthLargest = KthLargest(param['input'][0][0], param['input'][0][1])
        for i in range(1, len(param['input'])):
            result = kthLargest.add(param['input'][i][0])
            print(
                'SUCCESS' if result == param['output'][i - 1] else 'ERROR',
                'input', param['input'][i][0],
                'output', param['output'][i - 1],
                'result', result,
                '\n',
            )


if __name__ == '__main__':
    test()
