function numberOfBoomerangs(points: number[][]): number {
    if (points.length < 3) {
        return 0;
    }

    const getDistance = (a: number[], b: number[]) => {
        const x: number = (a[0] - b[0])**2;
        const y: number = (a[1] - b[1])**2;
        return  Math.sqrt(x+y);
    };

    const memo: Map<number, number>[] = new Array(points.length).fill(0);

    for (let i: number = 0; i < points.length; ++i) {
        memo[i] = memo[i] || new Map();
        for (let j: number = i+1; j < points.length; ++j) {
            memo[j] = memo[j] || new Map();

            const distance: number = getDistance(points[i], points[j]);

            let val: number = memo[i].get(distance) || 0;
            val += 1;
            memo[i].set(distance, val);

            val = memo[j].get(distance) || 0;
            val += 1;
            memo[j].set(distance, val);
        }
    }

    let res: number = 0;
    for (let i: number = 0; i < memo.length; ++i) {
        memo[i].forEach((val: number) => {
            if (val < 2) {
                return;
            }
            const comb: number = (val - 1) * val;
            res += comb;
        });
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: {
                points: [[0,0],[1,0],[2,0]]
            },
            output: 2,
        },
        {
            input: {
                points: [[1,1],[2,2],[3,3]],
            },
            output: 2,
        },
        {
            input: {
                points: [[1,1]],
            },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { points } = input;
        const result = numberOfBoomerangs(points);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();