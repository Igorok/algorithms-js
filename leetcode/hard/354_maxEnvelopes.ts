function maxEnvelopes_0(envelopes: number[][]): number {
    let maxEnv: number = 1;
    const arr: number[][] = [...envelopes].sort((a, b) => {
        if (a[0] === b[0]) {
            return a[1] - b[1];
        }
        return a[0] - b[0];
    });

    const count: number[] = new Array(arr.length).fill(1);
    for (let i = 1; i < arr.length; ++i) {
        for (let j = i - 1; j > -1; --j) {
            if (arr[j][0] < arr[i][0] && arr[j][1] < arr[i][1]) {
                count[i] = Math.max(count[i], count[j] + 1);
                maxEnv = Math.max(maxEnv, count[i]);
            }
        }
    }

    return maxEnv;
};

function maxEnvelopes(envelopes: number[][]): number {
    const arr: number[][] = [...envelopes].sort((a, b) => {
        if (a[0] === b[0]) {
            return b[1] - a[1];
        }
        return a[0] - b[0];
    });

    const count: number[] = [];

    const binSearch = (num: number) => {
        let start: number = 0;
        let end: number = count.length - 1;

        let res: number = 0;

        while (start <= end) {
            const middle: number = Math.round((start + end) / 2);
            if (count[middle] < num) {
                start = middle + 1;
                res = start;
            } else {
                end = middle - 1;
            }
        }

        return res;
    }

    for (let i = 0; i < arr.length; ++i) {
        const id = binSearch(arr[i][1]);

        if (id === count.length) {
            count.push(arr[i][1]);
        } else {
            count[id] = arr[i][1]
        }
    }

    return count.length;
};


/*


[
    [11, 7],
    [10, 6],
    [10, 10],
    [9, 5],
    [8, 4],
    [7, 3],
    [6, 2],
    [5, 1],
    [5, 9],
    [5, 11],
    [4, 8],
    [4, 12],
    [3, 7],
    [3, 13],
    [2, 6],
    [1, 5],
    [1, 15],
]

JSON.stringify([
    [11, 7],
    [10, 6],
    [10, 10],
    [9, 5],
    [8, 4],
    [7, 3],
    [6, 2],
    [5, 1],
    [5, 9],
    [5, 11],
    [4, 8],
    [4, 12],
    [3, 7],
    [3, 13],
    [2, 6],
    [1, 5],
    [1, 15],
])

[[11,7],[10,6],[10,10],[9,5],[8,4],[7,3],[6,2],[5,1],[5,9],[5,11],[4,8],[4,12],[3,7],[3,13],[2,6],[1,5],[1,15]]

[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [10, 10],
[5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6], [11, 7],

---

[5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6], [11, 7],

LIS - Для поиска длины последовательности есть алгоритм бинарного поиска. Складываем цифры в массив по возрастанию, если у нас есть 1 и 10, по возрастающую последовательность мы найдем для 1 скорее чем для 10. Поэтому мы затираем 10 на 1. Поэтому бинарным поиском ищем первое число больше пришедшего, и затираем его пришедшим, если нет то добавляем в массив.
1 10 2 11 3 12 13 4 ... 10 9 5 6
Даже если массив получится не правильный, то последовательность все равно нужно длинны
1 2 3 4 13
...
1 2 3 4 5 6

*/


const test = () => {
    const params = [
        {
            input: [
                [11, 7],
                [10, 6],
                [10, 10],
                [9, 5],
                [8, 4],
                [7, 3],
                [6, 2],
                [5, 11],
                [5, 9],
                [5, 1],
                [4, 12],
                [4, 8],
                [3, 13],
                [3, 7],
                [2, 6],
                [1, 15],
                [1, 5],
            ],
            output: 7,
        },
        {
            input: [
                [3, 13],
                [4, 12],
                [5, 11],

                [10, 10],

                [9, 5],

                [8, 8],
                [7, 7],
                [6, 6],


                [5, 9],
                [4, 8],
                [3, 7],
                [2, 6],
                [1, 5],

            ],
            output: 6,
        },
        {
            input: [
                [1, 10],
                [2, 11],
                [3, 12],

                [10, 1],
                [11, 2],
                [12, 3],

                [5, 5],
                [7, 7],
            ],
            output: 3,
        },

        {
            input: [[5,4],[6,4],[6,7],[2,3]],
            output: 3,
        },
        {
            input: [[1,1],[1,1],[1,1]],
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const nums = input as number[][];

        const result = maxEnvelopes(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();