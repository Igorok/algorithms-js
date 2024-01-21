/*
Параллельная обработка

По данным n процессорам и m задач определите, для каждой из задач, каким процессором она будет обработана.
Вход.
Число процессоров n и последовательность чисел t[0], . . . , t[m−1], где t[i] — время, необходимое на обработку i-й задачи.
Выход.
Для каждой задачи определите, какой процессор и в какое время начнёт её обрабатывать, предполагая, что каждая задача поступает на обработку первому освободившемуся процессору.

В данной задаче ваша цель — реализовать симуляцию параллельной обработки списка задач. Такие обработчики (диспетчеры) есть во всех операционных системах.
У вас имеется n процессоров и последовательность из m задач. Для каждой задачи дано время, необходимое на её обработку. Очередная работа поступает к первому доступному процессору (то есть если доступных процессоров несколько, то доступный процессор с минимальным номером получает эту работу).

Формат входа.
Первая строка входа содержит числа n и m. Вторая содержит числа t[0], . . . , t[m−1], где t[i] — время, необходимое на обработку i-й задачи. Считаем, что и процессоры, и задачи нумеруются с нуля.

Формат выхода.
Выход должен содержать ровно m строк: i-я (считая с нуля) строка должна содержать номер процессора, который получит i-ю задачу на обработку, и время, когда это произойдёт.
Ограничения. 1 <= n <= 10^5; 1 <= m <= 10^5; 0 <= ti <= 10^9.


Пример.
Вход:
2 5
1 2 3 4 5
Выход:
0 0
1 0
0 1
1 2
0 4

Пример.
Вход:
4 20
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
Выход:
0 0
1 0
2 0
3 0
0 1
1 1
2 1
3 1
0 2
1 2
2 2
3 2
0 3
1 3
2 3
3 3
0 4
1 4
2 4
3 4



16 12
4 5 2 0 1 0 7 2 6 8 0 0
0 0
1 0
2 0
3 0
3 0
4 0
4 0
5 0
6 0
7 0
8 0
8 0

2 15
0 0 1 0 0 0 2 1 2 3 0 0 0 2 1

0 0
0 0
0 0
1 0
1 0
1 0
1 0
0 1
0 2
1 2
0 4
0 4
0 4
0 4
1 5





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
        const result = parallelWorker(data[0][0], data[1]);
        // for (const r of result) {
        //     console.log(r.join(' '));
        // }
    }
});
rl.once('close', () => {
});

const parallelWorker = (processNumber, issues) => {
    const result = new Array(issues.length);

    const processorHeap = new MinHeap(processNumber);
    for (let i = 0; i < processNumber; i++) {
        processorHeap.insert([0, i]);
    }

    for (let i = 0; i < issues.length; i++) {
        const newIssue = issues[i];
        const processor = processorHeap.extractMin();
        result[i] = [processor[1], processor[0]];

        console.log(processor[1], processor[0]);

        processorHeap.insert([
            processor[0] + newIssue,
            processor[1],
        ]);
    }

    return result;
};

class MinHeap {
    size = -1;
    maxSize = 1;
    array = [];
    defaultValue = Math.pow(10, 9) + 1;

    constructor(maxSize) {
        this.maxSize = maxSize || this.maxSize;
        this.array = new Array(maxSize).fill(0).map(() => ([this.defaultValue, this.defaultValue]));
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

    #isBigger(val1, val2) {
        if (val1[0] === val2[0]) {
            return (val1[0] + val1[1]) > (val2[0] + val2[1]);
        }
        return val1[0] > val2[0];
    }

    #siftUp(i) {
        let pId = this.#getParentId(i);
        while (pId >= 0 && this.#isBigger(this.array[pId], this.array[i]) && pId !== i) {
            const tmp = this.array[pId];
            this.array[pId] = this.array[i];
            this.array[i] = tmp;
            i = pId;
            pId = this.#getParentId(i);
        }
    }

    #siftDown(i) {
        let lId = this.#getLeftChildId(i);
        let rId = this.#getRightChildId(i);
        while (i < this.size && (lId <= this.size || rId <= this.size)) {
            let minId;
            if (lId <= this.size) {
                minId = lId;
            }
            if (rId <= this.size && this.#isBigger(this.array[lId], this.array[rId])) {
                minId = rId;
            }

            if (this.#isBigger(this.array[i], this.array[minId])) {
                const tmp = this.array[i];
                this.array[i] = this.array[minId];
                this.array[minId] = tmp;

                i = minId;
                lId = this.#getLeftChildId(i);
                rId = this.#getRightChildId(i);
            }
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
    assert.deepEqual([], []);
    assert.deepEqual(parallelWorker(2, [ 1, 2, 3, 4, 5 ]), [[0, 0], [1, 0], [0, 1], [1, 2], [0, 4]]);
    assert.deepEqual(parallelWorker(4, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [[0, 0,], [1, 0,], [2, 0,], [3, 0,], [0, 1,], [1, 1,], [2, 1,], [3, 1,], [0, 2,], [1, 2,], [2, 2,], [3, 2,], [0, 3,], [1, 3,], [2, 3,], [3, 3,], [0, 4,], [1, 4,], [2, 4,], [3, 4,]]);
    assert.deepEqual(parallelWorker(2, [0, 0, 1, 0, 0, 0, 2, 1, 2, 3, 0, 0, 0, 2, 1]), [[0, 0,], [0, 0,], [0, 0,], [1, 0,], [1, 0,], [1, 0,], [1, 0,], [0, 1,], [0, 2,], [1, 2,], [0, 4,], [0, 4,], [0, 4,], [0, 4,], [1, 5,]]);
};
// test();
