'''
Задача на программирование: очередь с приоритетами

Первая строка входа содержит число операций 1 ≤ n ≤ 10^5 . Каждая из последующих n строк задают операцию одного из следующих двух типов:
Insert x, где 0 ≤ x ≤ 10^9  — целое число;
ExtractMax.
Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.

Sample Input:
6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax

Sample Output:
200
500
'''

import sys
import math

class Heap:
    heap = []

    def get_parent_i(self, i):
        return math.floor(i / 2)

    def get_left_i(self, i):
        return 2 * i

    def get_right_i(self, i):
        return 2 * i + 1

    def insert(self, value):
        self.heap.append(value)
        idx = len(self.heap) - 1
        parent_idx = self.get_parent_i(idx)

        while self.heap[parent_idx] < self.heap[idx] and idx > 0:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
            parent_idx = self.get_parent_i(idx)

    def extract_max(self):
        if len(self.heap) == 0:
            return

        value = self.heap[0]
        last = self.heap.pop()

        if len(self.heap) == 0:
            return value

        idx = 0
        self.heap[idx] = last
        heap_len = len(self.heap)

        while idx < heap_len:
            left_idx = self.get_left_i(idx)
            right_idx = self.get_right_i(idx)
            max_idx = idx
            if left_idx < heap_len and self.heap[left_idx] > self.heap[idx]:
                max_idx = left_idx

            if right_idx < heap_len and self.heap[right_idx] > self.heap[max_idx]:
                max_idx = right_idx

            if max_idx == idx:
                break

            self.heap[idx], self.heap[max_idx] = self.heap[max_idx], self.heap[idx]
            idx = max_idx

        return value



def main():
    heap = Heap()
    for line in sys.stdin:
        line = line.strip()
        if line[0] == 'E':
            print(heap.extract_max())
        elif line[0] == 'I':
            [_, value] = line.split()
            heap.insert(int(value))


if __name__ == "__main__":
    main()
