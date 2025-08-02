function generate(numRows: number): number[][] {
    const res: number[][] = [[1]];

    const getSum = (r: number, c: number) => {
        const left: number = c - 1 < 0 ? 0 : res[r-1][c-1];
        const middle: number = c === res[r-1].length ? 0 : res[r-1][c];

        return left + middle;
    }

    for (let i: number = 1; i < numRows; ++i) {
        const row: number[] = new Array(i+1).fill(0);
        res.push(row);

        for (let j: number = 0; j <= i; ++j) {
            res[i][j] = getSum(i, j);
        }
    }

    return res;
};

/*

[
    [1],
   [1,1],
  [1,2,1],
 [1,3,3,1],
[1,4,6,4,1]
]


*/

const test = () => {
    const params = [
        {
            input: {
                numRows: 5,
            },
            output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]],
        },
        {
            input: {
                numRows: 1,
            },
            output: [[1]],
        },
    ];

    params.forEach(({input, output}) => {
        const { numRows } = input;

        const result = generate(numRows);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();