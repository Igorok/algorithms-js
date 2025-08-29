function findDiagonalOrder(mat: number[][]): number[] {
    const m: number = mat.length;
    const n: number = mat[0].length;

    let res: number[] = [];
    let iteration: number = 0;

    const walk = (row: number, col: number) => {
        let acc: number[] = [];

        let r: number = row;
        let c: number = col;
        while (r > -1 && c < n) {
            acc.push(mat[r][c]);
            r -= 1;
            c += 1;
        }

        if (iteration % 2) {
            acc = acc.reverse();
        }
        res = [...res, ...acc];

        iteration += 1;
    }

    for (let row: number = 0; row < m; ++row) {
        walk(row, 0);
    }
    for (let col: number = 1; col < n; ++col) {
        walk(m-1, col);
    }

    return res;
};

/*
[
[1, 2],
[3, 4],
[5, 6],
[7, 8],
]

[
[1, 2 ,3 ,4,]
[5, 6 ,7, 8,]
]
*/

const test = () => {
    const params = [
        {
            input: {
                mat: [[1,2,3],[4,5,6],[7,8,9]]
            },
            output: [1,2,4,7,5,3,6,8,9],
        },
        {
            input: {
                mat: [[1,2],[3,4]]
            },
            output: [1,2,3,4],
        },
    ];

    params.forEach(({input, output}) => {
        const { mat } = input;
        const result = findDiagonalOrder(mat);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();