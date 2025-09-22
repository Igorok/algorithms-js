from typing import List
from json import dumps
import heapq
from collections import deque
import re

class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0]*1002 for i in range(26)]

    def __getCoords(self, cell: str):
        col = ord(cell[0].lower()) - ord('a')
        id = int(cell[1:])
        return (col, id)

    def __getNum(self, text: str):
        if text.isdigit():
            return int(text)

        col, id = self.__getCoords(text)
        return self.sheet[col][id]

    def setCell(self, cell: str, value: int) -> None:
        col, id = self.__getCoords(cell)
        self.sheet[col][id] = value

    def resetCell(self, cell: str) -> None:
        col, id = self.__getCoords(cell)
        self.sheet[col][id] = 0

    def getValue(self, formula: str) -> int:
        plus = formula.index('+')
        left = self.__getNum(formula[1:plus])
        right = self.__getNum(formula[plus+1:])
        return left + right



def test ():
    params = [
        {
            'input': [
                ["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"],
                [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]],
            ],
            'output': [None, 12, None, 16, None, 25, None, 15],
        },
    ]

    for param in params:
        commands, data = param['input']

        spreadsheet = Spreadsheet(data[0][0])

        for i in range(1, len(commands)):
            command = commands[i]
            argument = data[i]

            if command == 'setCell':
                spreadsheet.setCell(argument[0], argument[1])
            if command == 'resetCell':
                spreadsheet.resetCell(argument[0])
            elif command == 'getValue':
                r = spreadsheet.getValue(argument[0])
                print(
                    'SUCCESS' if r == param['output'][i] else 'ERROR',
                    '\n input', command, argument,
                    '\n output', param['output'][i],
                    '\n result', r,
                    '\n',
                )


if __name__ == '__main__':
    test()
