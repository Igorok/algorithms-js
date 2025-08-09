function diagonalSort(mat: number[][]): number[][] {
    const sortMat = (row: number, col: number) => {
        const acc: number[] = [];
        let r: number = row;
        let c: number = col;
        while (r < mat.length && c < mat[0].length) {
            acc.push(mat[r][c]);
            r += 1;
            c += 1;
        }

        acc.sort((a, b) => a - b);

        r = row;
        c = col;
        let id: number = 0;
        while (r < mat.length && c < mat[0].length) {
            mat[r][c] = acc[id];
            id += 1;
            r += 1;
            c += 1;
        }
    }

    for (let i: number = 0; i < mat.length; ++i) {
        sortMat(i, 0);
    }
    for (let i: number = 1; i < mat[0].length; ++i) {
        sortMat(0, i);
    }

    return mat;
};

const test = () => {
    const params = [
        {
            input: {
                mat: [[3,3,1,1],[2,2,1,2],[1,1,1,2]],
            },
            output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]],
        },
        {
            input: {
                mat: [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]],
            },
            output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]],
        },
    ];

    params.forEach(({input, output}) => {
        const { mat } = input;
        const result = diagonalSort(mat);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();