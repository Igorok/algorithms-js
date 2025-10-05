from typing import List
import json
from collections import defaultdict
import heapq


class FreqStack:

    def __init__(self):
        self._freq = defaultdict(int)
        self._freq_stack = {}
        self._max = []

    def push(self, val: int) -> None:
        self._freq[val] += 1
        cnt = self._freq[val]

        self._freq_stack[cnt] = self._freq_stack.get(cnt, [])
        self._freq_stack[cnt].append(val)

        heapq.heappush(self._max, -cnt)

    def pop(self) -> int:
        if not self._max:
            return -1

        _max = heapq.heappop(self._max)
        _max = -_max
        _val = self._freq_stack[_max].pop()
        self._freq[_val] -= 1

        return _val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


def test ():
    params = [
        {
            'input': [
                ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"],
                [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
            ],
            'output': [None, None, None, None, None, None, None, 5, 7, 5, 4],
        }
    ]

    for param in params:
        commands = param['input'][0]
        data = param['input'][1]
        freqStack = FreqStack(*data[0])

        result = None
        for i in range(1, len(commands)):
            if commands[i] == 'push':
                result = freqStack.push(*data[i])
            elif commands[i] == 'pop':
                result = freqStack.pop(*data[i])

            if json.dumps(param['output'][i]) == json.dumps(result):
                print('SUCCESS', '\n')
            else:
                print(
                    'ERROR \n',
                    'command', commands[i], '\n',
                    'output', param['output'][i], '\n',
                    'result', result, '\n',
                )




if __name__ == '__main__':
    test()
