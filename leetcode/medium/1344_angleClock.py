import heapq
import math
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from typing import List


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        degreeToMinutes = 360 / 60
        degreeToHours = 360 / 12

        minutesPosition = minutes * degreeToMinutes
        hourPosition = (hour % 12) * degreeToHours

        # every minute the hour hand move 1/60 step by circle towards to next hour
        hourMove = 1 / 60 * minutes * degreeToHours

        # print(
        #     "minutesPosition",
        #     minutesPosition,
        #     "hourPosition",
        #     hourPosition,
        #     "hourMove",
        #     hourMove,
        # )

        angle = abs(hourPosition + hourMove - minutesPosition)
        #  min angle
        angle = min(angle, 360 - angle)

        return angle


def test():
    params = [
        {
            "input": [12, 30],
            "output": 165,
        },
        {
            "input": [3, 30],
            "output": 75,
        },
        {
            "input": [3, 15],
            "output": 7.5,
        },
    ]
    solution = Solution()

    for param in params:
        hour, minutes = param["input"]
        result = solution.angleClock(hour, minutes)
        print(
            "SUCCESS" if result == param["output"] else "ERROR",
            "input",
            param["input"],
            "output",
            param["output"],
            "result",
            result,
            "\n",
        )


if __name__ == "__main__":
    test()
