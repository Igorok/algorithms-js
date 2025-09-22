from typing import List
from json import dumps
import heapq
from collections import deque

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.dataByFood = {}
        self.heapByCuis = {}
        for id in range(len(foods)):
            food = foods[id]
            self.dataByFood[food] = {
                'c': cuisines[id],
                'r': ratings[id],
            }

            cuis = cuisines[id]
            item = (-ratings[id], food)

            if cuis not in self.heapByCuis:
                self.heapByCuis[cuis] = [item]
                continue

            queue = self.heapByCuis[cuis]
            heapq.heappush(queue, item)

    def isWrong(self, cuis):
        if len(self.heapByCuis[cuis]) == 0:
            return False

        rt = -self.heapByCuis[cuis][0][0]
        food = self.heapByCuis[cuis][0][1]
        return rt != self.dataByFood[food]['r']


    def changeRating(self, food: str, newRating: int) -> None:
        self.dataByFood[food]['r'] = newRating
        cuis = self.dataByFood[food]['c']

        while self.isWrong(cuis):
            heapq.heappop(self.heapByCuis[cuis])

        heapq.heappush(self.heapByCuis[cuis], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.isWrong(cuisine):
            heapq.heappop(self.heapByCuis[cuisine])

        food = self.heapByCuis[cuisine][0][1]
        return food

def test ():
    params = [
        {
            'input': [
                ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"],
                [
                    [
                        ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                        ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                        [9, 12, 8, 15, 14, 7]
                    ],
                    ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]
                ]
            ],
            'output': [None, "kimchi", "ramen", None, "sushi", None, "ramen"],
        },
        {
            'input': [
                ["FoodRatings","changeRating","changeRating"],
                [
                    [
                        ["biihw"],["okxsrcqn"],[13]
                    ],
                    ["biihw",9],
                    ["biihw",6]
                ]
            ],
            'output': [None, "kimchi", "ramen", None, "sushi", None, "ramen"],
        },
    ]

    for param in params:
        commands, data = param['input']

        foods, cuisines, ratings = data[0]
        foodRatings = FoodRatings(foods, cuisines, ratings)

        for i in range(1, len(commands)):
            command = commands[i]
            argument = data[i]

            if command == 'highestRated':
                r = foodRatings.highestRated(argument[0])
                print(
                    'SUCCESS' if r == param['output'][i] else 'ERROR',
                    '\n input', command, argument,
                    '\n output', param['output'][i],
                    '\n result', r,
                    '\n',
                )
            else :
                foodRatings.changeRating(argument[0], argument[1])


if __name__ == '__main__':
    test()
