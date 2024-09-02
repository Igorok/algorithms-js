from typing import List

class Solution:
    def compress_(self, chars: List[str]) -> int:
        comprStr = ''
        count = 1
        char = chars[0]
        for i in range(1, len(chars)):
            if chars[i] == char:
                count += 1
            else:
                if count == 1:
                    comprStr = comprStr + char
                else:
                    comprStr = comprStr + char + str(count)
                char = chars[i]
                count = 1

        if count == 1:
            comprStr = comprStr + char
        else:
            comprStr = comprStr + char + str(count)

        return len(comprStr)


    def compress(self, chars: List[str]) -> int:
        count = 1
        char = chars[0]
        id = 0
        length = 0

        def update(char, id, chars, length):
            part = char if count == 1 else char + str(count)
            length += len(part)
            for i in range(len(part)):
                chars[id] = part[i]
                id += 1
            return [id, length]

        for i in range(1, len(chars)):
            if chars[i] == char:
                count += 1
            else:
                id, length = update(char, id, chars, length)
                char = chars[i]
                count = 1

        id, length = update(char, id, chars, length)

        return length


def test ():
    params = [
        {
            'input': ["a","a","b","b","c","c","c"],
            'output': 6,
        },
        {
            'input': ["a"],
            'output': 1,
        },
        {

            'input': ["a","b","b","b","b","b","b","b","b","b","b","b","b"],
            'output': 4,
        }
    ]
    solution = Solution()

    for param in params:
        result = solution.compress(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
