function numSubmat(mat: number[][]): number {
    let res: number = 0;

    for (let r: number = 0; r < mat.length; ++r) {
        for (let c: number = 0; c < mat[0].length; ++c) {
            if (mat[r][c] === 0) continue;

            mat[r][c] += c > 0 ? mat[r][c-1] : 0;

            let width: number = mat[r][c];
            for (let currRow: number = r; currRow > -1; --currRow) {
                if (mat[currRow][c] === 0) break;

                width = Math.min(width, mat[currRow][c]);
                res += width;
            }
        }
    }

    return res;
};

/*

[1,1,1,1,0],    4
[1,0,0,1,0],    2
[0,0,1,0,1],
[0,1,0,0,0],



*/

const test = () => {
    const params = [
        {
            input: {
                mat: [[1,1,1,1,0],[1,0,0,1,0],[0,0,1,0,1],[0,1,0,0,0]]
            },
            output: 17,
        },
        {
            input: {
                mat: [[1,0,1],[0,1,0],[1,0,1]]
            },
            output: 5,
        },
        {
            input: {
                mat: [[1,0,1],[1,1,0],[1,1,0]]
            },
            output: 13,
        },
        {
            input: {
                mat: [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
            },
            output: 24,
        },
    ];

    params.forEach(({input, output}) => {
        const { mat } = input;
        const result = numSubmat(mat);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();