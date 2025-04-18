function countGoodTriplets_0(arr: number[], a: number, b: number, c: number): number {
    let res:  number = 0;

    for (let i: number = 0; i < arr.length; ++i) {
        for (let j: number = i+1; j < arr.length; ++j) {
            for (let k: number = j+1; k < arr.length; ++k) {
                if (
                    Math.abs(arr[i] - arr[j]) <= a &&
                    Math.abs(arr[j] - arr[k]) <= b &&
                    Math.abs(arr[i] - arr[k]) <= c
                ) {
                    res += 1;
                }
            }
        }
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: [[2,6,9,0,1,8], 3, 1, 2],
            output: 2,
        },
        {
            input: [[3,0,1,1,9,7], 7, 2, 3],
            output: 4,
        },
        {
            input: [[1,1,2,2,3], 0, 0, 1],
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const arr: number[] = input[0] as number[];
        const a: number = input[1] as number;
        const b: number = input[2] as number;
        const c: number = input[3] as number;
        const result = countGoodTriplets(arr, a, b, c);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();