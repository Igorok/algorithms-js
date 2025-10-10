from typing import List
from json import dumps
from collections import defaultdict, deque
import heapq


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        tIds = set()
        tables = {}

        for customer, table, food in orders:
            foods.add(food)
            tIds.add(table)
            tables[table] = tables.get(table, {})
            tables[table][food] = tables[table].get(food, 0)
            tables[table][food] += 1

        foods = list(foods)
        foods.sort()
        tIds = list(tIds)
        tIds.sort(key=lambda x: int(x))

        res = [
            ["Table"],
        ]
        for food in foods:
            res[0].append(food)

        for tId in tIds:
            row = [
                tId,
            ]
            for food in foods:
                r = 0 if food not in tables[tId] else tables[tId][food]
                row.append(str(r))
            res.append(row)

        return res


"""
ERROR input [['David', '3', 'Ceviche'], ['Corina', '10', 'Beef Burrito'], ['David', '3', 'Fried Chicken'], ['Carla', '5', 'Water'], ['Carla', '5', 'Ceviche'], ['Rous', '3', 'Ceviche']] output

[
['Table', 'Beef Burrito', 'Ceviche', 'Fried Chicken', 'Water'],
['3', '0', '2', '1', '0'],
['5', '0', '1', '0', '1'],
['10', '1', '0', '0', '0']
]
result
[
['Table', 'Beef Burrito', 'Ceviche', 'Fried Chicken', 'Water'],
['3', 0, 2, 1, 0],
['5', 0, 1, 0, 1],
['10', 1, 0, 0, 0]
]


"""


def test():
    params = [
        {
            "input": [
                ["David", "3", "Ceviche"],
                ["Corina", "10", "Beef Burrito"],
                ["David", "3", "Fried Chicken"],
                ["Carla", "5", "Water"],
                ["Carla", "5", "Ceviche"],
                ["Rous", "3", "Ceviche"],
            ],
            "output": [
                ["Table", "Beef Burrito", "Ceviche", "Fried Chicken", "Water"],
                ["3", "0", "2", "1", "0"],
                ["5", "0", "1", "0", "1"],
                ["10", "1", "0", "0", "0"],
            ],
        },
        {
            "input": [
                ["James", "12", "Fried Chicken"],
                ["Ratesh", "12", "Fried Chicken"],
                ["Amadeus", "12", "Fried Chicken"],
                ["Adam", "1", "Canadian Waffles"],
                ["Brianna", "1", "Canadian Waffles"],
            ],
            "output": [
                ["Table", "Canadian Waffles", "Fried Chicken"],
                ["1", "2", "0"],
                ["12", "0", "3"],
            ],
        },
        {
            "input": [
                ["Laura", "2", "Bean Burrito"],
                ["Jhon", "2", "Beef Burrito"],
                ["Melissa", "2", "Soda"],
            ],
            "output": [
                ["Table", "Bean Burrito", "Beef Burrito", "Soda"],
                ["2", "1", "1", "1"],
            ],
        },
    ]
    solution = Solution()

    for param in params:
        orders = param["input"]
        result = solution.displayTable(orders)
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
