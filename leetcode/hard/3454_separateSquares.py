import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math


class SegmentTree:
    def __init__(self, coords):
        self.n = len(coords) - 1
        self.coords = coords
        # How many squares completely cover this node's range?
        self.count = [0] * (4 * self.n)
        # The total horizontal distance within this node’s range that is covered by at least one square.
        self.length = [0.0] * (4 * self.n)

    def _updateNode(self, id, left, right):
        # this interval is covered
        if self.count[id] > 0:
            self.length[id] = float(self.coords[right+1] - self.coords[left])
        # this interval is not covered, but its child can be
        elif left < right:
            self.length[id] = self.length[2*id] + self.length[2*id + 1]
        # left == right
        else:
            self.length[id] = 0.0

    def update(self, id, left, right, qLeft, qRight, val):
        if qLeft <= left and  right <= qRight:
            self.count[id] += val
        else:
            middle = (left + right) // 2
            if qLeft <= middle:
                self.update(2*id, left, middle, qLeft, qRight, val)
            if qRight > middle:
                self.update(2*id + 1, middle+1, right, qLeft, qRight, val)
        self._updateNode(id, left, right)

    def query(self):
        return self.length[1]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        y_events = []
        x_coords = set()

        for x, y, l in squares:
            x_coords.add(x)
            x_coords.add(x+l)
            # add event
            y_events.append((y, 1, x, x+l))
            # remove event
            y_events.append((y+l, -1, x, x+l))

        y_events.sort()
        # all possible intervals
        sorted_x = sorted(list(x_coords))
        x_map = { val: i for i, val in enumerate(sorted_x) }

        st = SegmentTree(sorted_x)

        # total area
        total_area = 0.0
        for i in range(len(y_events) - 1):
            y_curr, type_curr, x1, x2 = y_events[i]
            st.update(1, 0, st.n-1, x_map[x1], x_map[x2]-1, type_curr)

            y_next = y_events[i+1][0]
            width = st.query()
            total_area += width * (y_next - y_curr)

        target_area = total_area / 2.0
        current_area = 0.0

        # half of area
        st = SegmentTree(sorted_x)

        for i in range(len(y_events) - 1):
            y_curr, type_curr, x1, x2 = y_events[i]
            st.update(1, 0, st.n-1, x_map[x1], x_map[x2]-1, type_curr)

            y_next = y_events[i+1][0]
            width = st.query()
            slice_area = width * (y_next - y_curr)

            if current_area + slice_area >= target_area:
                if width == 0:
                    return float(y_curr)
                remaining = target_area - current_area
                return float(y_curr + (remaining / width))

            current_area += slice_area

        return y_events[-1][0]






def test():
    params = [
        {
            "input": [[0,0,1],[2,2,1]],
            "output": 1.00000,
        },
        {
            "input": [[0,0,2],[1,1,1]],
            "output": 1.00000,
        },
    ]
    solution = Solution()

    for param in params:
        squares = param["input"]
        result = solution.separateSquares(squares)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            # msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
