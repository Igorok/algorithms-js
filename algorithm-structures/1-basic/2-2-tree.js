/*

Высота дерева
Вычислить высоту данного дерева.
Вход. Корневое дерево с вершинами {0, . . . , n−1}, заданное как последовательность parent0 , . . . , parentn−1 , где parenti — родитель i-й вершины.
Выход. Высота дерева.

Формат входа. Первая строка содержит натуральное число n. Вторая строка содержит n целых чисел parent0 , . . . , parentn−1 . Для каждого 0 ≤ i ≤ n − 1, parenti — родитель вершины i; если parenti = −1, то i является корнем. Гарантируется, что корень ровно один. Гарантируется, что данная последовательность задаёт дерево.
Формат выхода. Высота дерева.
Ограничения. 1 ≤ n ≤ 105 .

Пример.
Вход:
5
4 -1 4 1 1
Выход:
3

Пример.
Вход:
5
-1 0 4 0 3
Выход:
4

Sample Input:
10
9 7 5 5 2 9 9 9 2 -1
Sample Output:
4

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
    data.push(line.split(' ').map(v => Number(v)));
    if (data.length === 2) {
        const result = getHeight(data[1]);
        console.log(result);
    }
});
rl.once('close', () => {
});

const getHeight = (arr) => {
    if (arr.length < 2) {
        return arr.length;
    }

    let t = 0;
    const children = new Array(arr.length).fill(0).map(() => {
        return new Array();
    });
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == -1) {
            t = i;
        } else {
            children[arr[i]].push(i);
        }
    }

    let s = 1;
    const queue = [{ i: t, s: 1}];
    while (queue.length) {
        const node = queue.pop();
        if (children[node.i]) {
            for (const i of children[node.i]) {
                queue.push({ i, s: node.s + 1});
                if (node.s + 1 > s) {
                    s = node.s + 1;
                }
            }
        }
    }

    return s;
};



const test = () => {
    assert.equal(getHeight([4, -1, 4, 1, 1]), 3);
    assert.equal(getHeight([-1, 0, 4, 0, 3]), 4);
    assert.equal(getHeight([9, 7, 5, 5, 2, 9, 9, 9, 2, -1]), 4);
};
test();
