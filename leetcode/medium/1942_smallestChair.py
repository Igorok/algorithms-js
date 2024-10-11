from typing import List
import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arrive = []
        for i in range(len(times)):
            s, e = times[i]
            friend = [s, e, i, 0]
            arrive.append((s, friend))

        arrive = sorted(arrive, key=lambda x: -x[0])

        chairs = [i for i in range(len(times) + 1)]
        heapq.heapify(chairs)

        room = []
        while len(arrive):
            start, guest = arrive.pop()
            s, e, i, c = guest

            while len(room) > 0 and room[0][0] <= s:
                end, friend = heapq.heappop(room)
                chair = friend[3]
                heapq.heappush(chairs, chair)

            chair = heapq.heappop(chairs)
            heapq.heappush(room, (e, [s, e, i, chair]))
            if i == targetFriend:
                return chair

        return 0

'''.git/
[[3,10],[1,5],[2,6]]

(3, 10, 0)
(1, 5, 1)
(2, 6, 2)

(1, 5, 1)
(2, 6, 2)
(3, 10, 0)

---

[[7, 12], [10, 15], [5, 10], [12, 17], [2, 7] ]

---


friends [(2, 3, 1), (1, 4, 0), (4, 6, 2)]
friends [(1, 5, 1), (2, 6, 2), (3, 10, 0)]
friends [(2, 7, 0), (5, 10, 1), (7, 12, 2), (10, 15, 3), (12, 17, 4)]


friends [(1, 4, 0), (2, 3, 1), (4, 6, 2)]
friends [(1, 5, 1), (2, 6, 2), (3, 10, 0)]
friends [(2, 7, 0), (5, 10, 1), (7, 12, 2), (10, 15, 3), (12, 17, 4)]

'''



def test ():
    params = [
        {
            'input': [[[1,4],[2,3],[4,6]], 1],
            'output': 1,
        },
        {
            'input': [[[3,10],[1,5],[2,6]],  0],
            'output': 2,
        },
        {
            'input': [[[2, 7], [5, 10], [7, 12], [10, 15], [12, 17]] , 4],
            'output': 0,
        },
        {
            'input': [[[4,5],[12,13],[5,6],[1,2],[8,9],[9,10],[6,7],[3,4],[7,8],[13,14],[15,16],[14,15],[10,11],[11,12],[2,3],[16,17]] , 15],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        times, targetFriend = param['input']

        result = solution.smallestChair(times, targetFriend)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
