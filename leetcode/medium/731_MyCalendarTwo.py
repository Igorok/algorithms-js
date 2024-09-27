from typing import List
import json

class MyCalendarTwo:

    def __init__(self):
        self.booking = []
        self.intersect = []


    def book(self, start: int, end: int) -> bool:
        for s, e in self.intersect:
            if start >= e or end <= s:
                continue
            else:
                return False

        for s, e in self.booking:
            if start >= e or end <= s:
                continue
            else:
                self.intersect.append((max(s, start), min(e, end)))

        self.booking.append((start, end))
        return True



def test ():
    params = [
        {
            'input': [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
            'output': [True, True, True, False, True, True],
        },
        {
            'input': [[2, 10], [3, 11], [4, 12], [20, 30], [15, 21], [16, 22], [35, 45], [34, 46], [33, 47]],
            'output': [True, True, False, True, True, False, True, True, False,],
        },
    ]

    for param in params:
        myCalendarTwo = MyCalendarTwo()
        result = []
        for p in param['input']:
            s, e = p
            result.append(myCalendarTwo.book(s, e))
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()