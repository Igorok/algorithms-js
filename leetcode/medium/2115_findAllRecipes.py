from typing import List
import json
from collections import deque, defaultdict
import heapq


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        readyRecipes = {}
        incomingIngr = {}
        adj = {}

        for sup in supplies:
            incomingIngr[sup] = set()

        for i in range(len(recipes)):
            rec = recipes[i]
            ingrArr = ingredients[i]

            incomingIngr[rec] = set(ingrArr)
            readyRecipes[rec] = False

            for product in incomingIngr[rec]:
                if not product in adj:
                    adj[product] = set()
                adj[product].add(rec)

        productsQue = deque()
        for key in incomingIngr:
            if len(incomingIngr[key]) == 0:
                productsQue.append(key)

        while productsQue:
            product = productsQue.popleft()
            if not product in adj:
                continue
            for rec in adj[product]:
                incomingIngr[rec].remove(product)
                if len(incomingIngr[rec]) == 0:
                    readyRecipes[rec] = True
                    productsQue.append(rec)

        res = []
        for rec in recipes:
            if readyRecipes[rec]:
                res.append(rec)

        return res

'''

["yeast","flour","meat"]

["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]

["bread","sandwich","burger"]

'''



def test ():
    params = [
        {
            'input': [["bread"], [["yeast","flour"]], ["yeast","flour","corn"]],
            'output': ["bread"],
        },
        {
            'input': [["bread","sandwich"], [["yeast","flour"],["bread","meat"]], ["yeast","flour","meat"]],
            'output': ["bread","sandwich"],
        },
        {
            'input': [
                ["bread","sandwich","burger"],
                [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]],
                ["yeast","flour","meat"]
            ],
            'output': ["bread","sandwich","burger"],
        },
    ]
    solution = Solution()

    for param in params:
        recipes, ingredients, supplies = param['input']
        result = solution.findAllRecipes(recipes, ingredients, supplies)
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
