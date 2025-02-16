class MedianFinder_0:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian_(self) -> float:
        l = len(self.heap)
        m = l // 2

        maxHeap = []
        q = [(self.heap[0], 0)]

        while q:
            val, id = heapq.heappop(q)
            heapq.heappush(maxHeap, -self.heap[id])

            if len(maxHeap) == m+1:
                # print(
                #     'self.heap', self.heap,
                #     'maxHeap', maxHeap,
                #     'l', l,
                #     'm', m,
                # )

                if (l%2) == 1:
                    return -heapq.heappop(maxHeap)

                first = -heapq.heappop(maxHeap)
                second = -heapq.heappop(maxHeap)
                return (first + second) / 2

            leftId = (id+1)*2-1
            rightId = (id+1)*2

            if leftId < l:
                heapq.heappush(q, (self.heap[leftId], leftId))
            if rightId < l:
                heapq.heappush(q, (self.heap[rightId], rightId))

    def findMedian(self) -> float:
        l = len(self.heap)
        m = l // 2
        if l == 1:
            return self.heap[0]
        if l == 2:
            return (self.heap[0] + self.heap[1]) / 2

        q = self.heap.copy()

        prev = None
        for i in range(m+1):
            v = heapq.heappop(q)
            if i == m:
                if (l % 2) == 1:
                    return v
                else:
                    return (prev + v) / 2
            prev = v




class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        if self.maxHeap and self.minHeap and (len(self.maxHeap) - len(self.minHeap) > 1 or -self.maxHeap[0] > self.minHeap[0]):
            v = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, v)

        while len(self.minHeap) > len(self.maxHeap):
            v = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -v)

    def findMedian(self) -> float:
        l = len(self.maxHeap) + len(self.minHeap)
        if (l % 2) == 1:
            return self.maxHeap[0]

        return (self.maxHeap[0] + self.minHeap[0]) / 2


'''

["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
[[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]
[null,null,-1.00000,null,-1.50000,null,-1.00000,null,-2.50000,null,-2.00000]
[null,null,-1.00000,null,-1.50000,null,-2.00000,null,-2.50000,null,-3.00000]

8
0 1 2 3 4 5 6 7
1,2,3,4,5,6,7,8,

0, (1+0)*2=2, (1+0)*2-1=1
1, (1+1)*2=4, (1+1)*2-1=3
2, (1+2)*2=6, (1+2)*2-1=5
3, (1+3)*2=8, (1+3)*2-1=7
4, (1+4)*2=10, (1+4)*2-1=9


'''