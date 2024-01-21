/*

Построение кучи

Переставить элементы заданного массива чисел так, чтобы он удовлетворял свойству мин-кучи.
Вход. Массив чисел A[0 ... n − 1].
Выход. Переставить элементы массива так, чтобы выполнялись неравенства A[i] <= A[2i + 1] и A[i] <= A[2i + 2] для всех i.

Построение кучи — ключевой шаг алгоритма сортировки кучей. Данный алгоритм имеет время работы O(n log n) в худшем случае в отличие от алгоритма быстрой сортировки, который гарантирует такую оценку только в среднем случае. Алгоритм быстрой сортировки чаще используют на практике, поскольку в большинстве случаев он работает быстрее, но алгоритм сортировки кучей используется для внешней сортировки данных, когда необходимо отсортировать данные огромного размера, не помещающиеся в память компьютера.

Чтобы превратить данный массив в кучу, необходимо произвести несколько обменов его элементов. Обменом мы называем базовую операцию, которая меняет местами элементы A[i] и A[j]. Ваша цель в данной задаче — преобразовать заданный массив в кучу за линейное количество обменов.

Формат входа.
Первая строка содержит число n. Следующая строка задаёт массив чисел A[0], . . . , A[n − 1].
Формат выхода.
Первая строка выхода должна содержать число обменов m, которое должно удовлетворять неравенству 0 <= m <= 4n. Каждая из последующих m строк должна задавать обмен двух элементов массива A. Каждый обмен задаётся парой различных индексов 0 <= i != j <= n − 1. После применения всех обменов в указанном порядке массив должен превратиться в минкучу, то есть для всех 0 <= i <= n − 1 должны выполняться следующие два условия:
- если 2i + 1 <= n − 1, то A[i] < A[2i + 1].
- если 2i + 2 <= n − 1, то A[i] < A[2i + 2].

Ограничения.
1 <= n <= 10^5 ; 0 <= A[i] <= 10^9 для всех 0 <= i <= n − 1; все A[i] попарно различны; i != j.

Пример.
Вход:
5
5 4 3 2 1

Выход:
3
1 4
0 1
1 3

Пример.
Вход:
5
1 2 3 4 5

Выход:
0

Sample Input 1:
6
0 1 2 3 4 5

Sample Output 1:
0

Sample Input 2:
6
7 6 5 4 3 2

Sample Output 2:
4
2 5
1 4
0 2
2 5

*/



const readline = require('readline');
const assert = require('node:assert');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});

const data = [];

rl.on('line', (line) => {
    data.push(
        line.split(' ').map((n) => Number(n)),
    );

    if (data.length === 2) {
        const [count, array] = buildHeap(data[1]);
        console.log(count);
        for (const ids of array) {
            console.log(ids.join(' '));
        }
    }
});
rl.once('close', () => {
});


const buildHeap = (array) => {
    const h = new MinHeap();
    h.buildHeap(array);
    return [ h.countOfChanges, h.arrayOfChanges ];
}

class MinHeap {
    size = -1;
    maxSize = 1;
    array = [];
    defaultValue = Math.pow(10, 9) + 1;

    constructor(maxSize) {
        this.maxSize = maxSize || this.maxSize;
        this.array = new Array(maxSize).fill(this.defaultValue);
    }

    #getParentId(i) {
        return Math.floor((i - 1) / 2);
    }

    #getLeftChildId(i) {
        return 2 * i + 1;
    }

    #getRightChildId(i) {
        return 2 * i + 2;
    }

    #siftUp(i) {
        let pId = this.#getParentId(i);
        while (this.array[pId] > this.array[i] && pId !== i) {
            const tmp = this.array[pId];
            this.array[pId] = this.array[i];
            this.array[i] = tmp;
            i = pId;
            pId = this.#getParentId(i);
        }
    }

    countOfChanges = 0;
    arrayOfChanges = [];

    #siftDown(i) {
        let lId = this.#getLeftChildId(i);
        let rId = this.#getRightChildId(i);
        while (i < this.size && (lId <= this.size || rId <= this.size)) {
            const left = lId <= this.size ? this.array[lId] : this.defaultValue;
            const right = rId <= this.size ? this.array[rId] : this.defaultValue;
            const minId = left < right ? lId : rId;

            if (this.array[i] <= this.array[minId]) {
                break;
            }

            this.countOfChanges += 1;
            this.arrayOfChanges.push([i, minId]);

            const tmp = this.array[i];
            this.array[i] = this.array[minId];
            this.array[minId] = tmp;

            i = minId;
            lId = this.#getLeftChildId(i);
            rId = this.#getRightChildId(i);
        }
    }

    insert(value) {
        this.size += 1;
        this.array[this.size] = value;
        this.#siftUp(this.size);
    }

    extractMin() {
        const max = this.array[0];
        this.array[0] = this.array[this.size];
        this.size -= 1;
        this.#siftDown(0);

        return max;
    }

    remove() {}

    getMin() {
        return this.array[0];
    }

    changePriority() {}

    buildHeap(array) {
        this.maxSize = array.length;
        this.size = array.length - 1;
        this.array = array;
        let pastNodeId = Math.floor((array.length - 1) / 2);
        while (pastNodeId >= 0) {
            this.#siftDown(pastNodeId);
            pastNodeId -= 1;
        }
    }
}



const test = () => {
    assert.deepEqual(buildHeap([5, 4, 3, 2, 1]), [3, [[1, 4], [0, 1], [1, 3]]]);
    assert.deepEqual(buildHeap([1, 2, 3, 4, 5]), [0, []]);
    assert.deepEqual(buildHeap([0, 1, 2, 3, 4, 5]), [0, []]);
    assert.deepEqual(buildHeap([7, 6, 5, 4, 3, 2]), [4, [[2, 5], [1, 4], [0, 2], [2, 5]]]);
};
test();

