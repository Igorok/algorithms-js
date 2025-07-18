function generateMatrix(n: number): number[][] {
    const matrix: number[][] = new Array(n).fill(0).map(() => new Array(n).fill(0));

    const fillLine = (y: number, x: number, num: number) => {
        if (y > Math.ceil(n/2)) return;

        const top: number = n - y*2;
        const right: number = Math.max(top - 1, 0);
        const bottom: number = Math.max(top - 1, 0);
        const left: number = Math.max(top - 2, 0);

        for (let i: number = 0; i < top; ++i) {
            matrix[y][x] = num;
            num += 1;
            x += 1;
        }
        x-= 1;
        y += 1

        if (right === 0) return;

        for (let i: number = 0; i < right; ++i) {
            matrix[y][x] = num;
            num += 1;
            y += 1;
        }
        y -= 1;
        x -= 1;

        for (let i: number = 0; i < bottom; ++i) {
            matrix[y][x] = num;
            num += 1;
            x -= 1;
        }
        x += 1;
        y -= 1;

        for (let i: number = 0; i < left; ++i) {
            matrix[y][x] = num;
            num += 1;
            y -= 1;
        }
        y += 1;
        x += 1;

        fillLine(y, x, num);
    };

    fillLine(0, 0, 1);


    return matrix;
};

const test = () => {
    const params = [
        {
            input: {
                n: 3,
            },
            output: [[1,2,3],[8,9,4],[7,6,5]],
        },
        {
            input: {
                n: 1,
            },
            output: [[1]],
        },
    ];

    params.forEach(({input, output}) => {
        const { n } = input;
        const result = generateMatrix(n);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();