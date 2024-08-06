'''
Sample Input 1:
3
2 1 5
1
Sample Output 1:
2 1 5

Sample Input 2:
8
2 7 3 1 5 2 6 2
4
Sample Output 2:
7 7 5 6 6

'''


import sys

def printAnswer(n, m, nums):
    print(
        'n', n,
        'm', m,
        'nums', nums,
    )


'''
8
2 7 3 1 5 2 6 2
4
2 7 3 1 5 2 6 2
7 7 7 7 - - - -
- 7 7 7 7 - - -
- - 5 5 5 5 - -
- - - 6 6 6 6 -
- - - - 6 6 6 6


2 7 3 1 5 2 6 2
2 7 3 1 - - - -
- 7 3 1 5 - - -
- - 3 1 5 2 - -
- - - 1 5 2 6 -
- - - - 5 2 6 2


2 7 3 1 5 2 6 2
2 7 7 7
- 7 7 7 7
- - ? ? ? ?

1   2   3   4   5   6   7   8
1,1 2,2 3,3 4,4
-   2,2 3,3 4,4 5,5
-   -   3,3 4,4 5,5 6,6
-   -   -   4,4 5,5 6,6 7,7
-   -   -   -   5,5 6,6 7,7 8,8

8   7   6   5   4   3   2   1
8,8 7,8 6,8 5,8
    7,8 6,8 5,8 4,4






'''

def main():
    i = 0
    n = 0
    m = 0
    nums = []
    for line in sys.stdin:
        if i == 0:
            n = int(line.strip())
        elif i == 1:
            nums = [int(v) for v in line.strip().split(' ')]
        elif i == 2:
            m = int(line.strip())

        i += 1

    printAnswer(n, m, nums)


if __name__ == '__main__':
    main()
