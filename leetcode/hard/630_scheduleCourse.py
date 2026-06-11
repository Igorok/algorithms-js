import heapq
import json
from collections import deque
from typing import List


class Solution_0:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        res = 0
        day = 0

        for course in courses:
            dur, end = course
            if day + dur > end:
                continue
            day += dur
            res += 1

        return res


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        coursesQueue = []
        day = 0

        for course in courses:
            duration, deadline = course
            day += duration
            heapq.heappush(coursesQueue, -duration)

            if day > deadline:
                maxDuration = heapq.heappop(coursesQueue)
                # maxDuration - negative in heap
                day += maxDuration

        return len(coursesQueue)


"""
Сортируем по дедлайнам, делаем все срочное.
шаг 1 всегда вписывается в дедлайн
1) имеет дедлайн равный
а) продолжительность больше или равно, этот элемент вылетит, остальные уже вписываются в дедлайн
б) продолжительность меньше или равна, значит заменит прошлы и время сдвинется назад, все уложилось в дедлайн

2) имеет дедлайн больше
а) продолжительность больше или равно, этот элемент вылетает, остальные уже вписываются в дедлайн
б) продложительность меньше, то почему впишется в дедлай? Если бы у него дедлайн был равен, то точно бы вписался, потому что старые то вписались, а у этого продолжительность еще меньше. А у этого и дедлайн больше, и продолжительность меньше, он точно проходит.
[100,200],[100,200],[99,201]

"""


def test():
    params = [
        {
            "input": [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]],
            "output": 3,
        },
        {
            "input": [[1, 2]],
            "output": 1,
        },
        {
            "input": [[3, 2], [4, 3]],
            "output": 0,
        },
        {
            "input": [[1, 2], [2, 3]],
            "output": 2,
        },
        {
            "input": [[5, 5], [4, 6], [2, 6]],
            "output": 2,
        },
        {
            "input": [
                [5, 15],
                [3, 19],
                [6, 7],
                [2, 10],
                [5, 16],
                [8, 14],
                [10, 11],
                [2, 19],
            ],
            "output": 5,
        },
        {
            "input": [
                [2, 4],
                [2, 2],
                [1, 5],
            ],
            "output": 3,
        },
    ]

    solution = Solution()

    for param in params:
        courses = param["input"]
        result = solution.scheduleCourse(courses)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
