function countNegatives(grid: number[][]): number {
    const n: number = grid.length
    const m: number = grid[0].length;

    const findNegative = (row: number[]): number => {
        let left: number = 0;
        let right: number = m - 1;
        let end: number = -1;

        while (left <= right) {
            const middle = Math.floor((left + right) / 2);

            if (row[middle] < 0) {
                end = middle;
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }

        return end;
    };

    let res: number = 0;
    for (let i: number = 0; i < n; ++i) {
        const end: number = findNegative(grid[i]);
        if (end !== -1) {
            res += m - end;
        }
    }

    return res;
};

/*
4
[
[4,3,2,-1],
[3,2,1,-1],
[1,1,-1,-2],
[-1,-1,-2,-3]
]

*/

const test = () => {
    const params = [
        {
            input: {
                grid: [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]],
            },
            output: 8,
        },
        {
            input: {
                grid: [[3,2],[1,0]]
            },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { grid } = input;
        const result = countNegatives(grid);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

