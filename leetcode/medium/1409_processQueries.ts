function processQueries(queries: number[], m: number): number[] {
    const nums: number[] = new Array(m).fill(0);
    for (let i: number = 0; i < m; ++i) {
        nums[i] = i + 1;
    }

    const res: number[] = new Array(queries.length).fill(0);

    for (let i: number = 0; i < queries.length; ++i) {
        const q: number = queries[i];

        if (nums[0] === q) {
            res[i] = 0;
            continue;
        }

        let tmp: number = nums[0];
        for (let j: number = 1; j < m; ++j) {
            const t: number = nums[j];
            nums[j] = tmp;
            tmp = t;

            if (tmp === q) {
                res[i] = j;
                break;
            }
        }
        nums[0] = q;

    }

    return res;
};


const test = () => {
    const params = [
        {
            input: {
                queries: [3,1,2,1], m: 5
            },
            output: [2,1,2,1] ,
        },
        {
            input: {
                queries: [4,1,2,2], m: 4,
            },
            output: [3,1,2,0],
        },
        {
            input: {
                queries: [7,5,5,8,3], m: 8
            },
            output: [6,5,0,7,5],
        },
    ];

    params.forEach(({input, output}) => {
        const { queries, m } = input;
        const result = processQueries(queries, m);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();