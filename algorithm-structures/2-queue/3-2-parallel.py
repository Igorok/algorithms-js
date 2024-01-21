import sys
from heapq import heapify, heappush, heappop

def parallelProcessors(processorsCount, issues):
    processorHeap = [[0, i] for i in range(processorsCount)]
    heapify(processorHeap)

    for i in range(len(issues)):
        processor = heappop(processorHeap)
        print(processor[1], processor[0])
        heappush(processorHeap, [processor[0] + issues[i], processor[1]])


def main():
    data = []
    for line in sys.stdin:
        data.append([int(i) for i in line.split(' ')])

    parallelProcessors(data[0][0], data[1])


if __name__ == '__main__':
    main()