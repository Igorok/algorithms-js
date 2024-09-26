from typing import List
import json

class MyCalendar:
    def __init__(self):
        self.booking = []

    def book(self, start: int, end: int) -> bool:
        if len(self.booking) > 0:
            for s, e in self.booking:
                if start >= s and start < e:
                    return False
                if end > s and end <= e:
                    return False
                if start < s and end > e:
                    return False

        self.booking.append((start, end))

        return True


def test ():
    params = [
        {
            'input': [[10,20],[15,25],[20,30]],
            'output': [True, False, True],
        },
        {
            'input': [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]],
            'output': [True,True,False,False,True,False,True,True,True,False],
        },
        {
            'input': [[37,50],[33,50],[4,17],[35,48],[8,25]],
            'output': [True,False,True,False,False],
        },
        {
            'input': [[97,100],[33,51],[89,100],[83,100],[75,92],[76,95],[19,30],[53,63],[8,23],[18,37],[87,100],[83,100],[54,67],[35,48],[58,75],[70,89],[13,32],[44,63],[51,62],[2,15]],
            'output': [True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True],
        },
    ]


    for param in params:
        solution = MyCalendar()
        result = []
        for p in param['input']:
            s, e = p
            result.append(solution.book(s, e))

        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'], '\n',
            'output', param['output'], '\n',
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
