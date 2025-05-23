function maximumValueSum(nums: number[], k: number, edges: number[][]): number {
    const delta: number[] = [];
    let sum: number = 0;

    for (const n of nums) {
        sum += n;
        delta.push((n ^ k) - n);
    }

    delta.sort((a, b) => b-a);

    for (let i: number = 0; i < delta.length; i+=2) {
        const diff: number = delta[i] + delta[i+1];
        if (diff > 0) {
            sum += diff;
        }
    }

    return sum;
};


/*
{ nums: [1,2,1], k: 3, edges: [[0,1],[0,2]] }

3 = 11
1 = 01
2 = 10



*/

const test = () => {
    const params = [
        {
            input: { nums: [1,2,1], k: 3, edges: [[0,1],[0,2]] },
            output: 6,
        },
        {
            input: { nums: [2,3], k: 7, edges: [[0,1]] },
            output: 9,
        },
        {
            input: { nums: [7,7,7,7,7,7], k: 3, edges: [[0,1],[0,2],[0,3],[0,4],[0,5]] },
            output: 42,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, k, edges } = input;

        const result = maximumValueSum(nums, k, edges);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();