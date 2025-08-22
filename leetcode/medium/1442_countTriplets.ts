function countTriplets(arr: number[]): number {
    const prefix: number[] = new Array(arr.length).fill(0);
    prefix[0] = arr[0];
    for (let i: number = 1; i < arr.length; ++i) {
        prefix[i] = arr[i] ^ prefix[i-1];
    }

    let res: number = 0;
    for (let i: number = 0; i < arr.length; ++i) {
        for (let j: number = i+1; j < arr.length; ++j) {
            for (let k: number = j; k < arr.length; ++k) {
                const a: number = i === 0 ? prefix[j-1] : prefix[j-1]^prefix[i-1];
                const b: number = prefix[k] ^ prefix[j-1];

                if (a === b) {
                    res += 1;
                }
            }
        }
    }


    return res;
};

/*

[2,3,1,6,7]


101 - 101
010 - 111
111 - 000 - 111
100 - 100 - 011

100 ^ 111 = 011


The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

*/

const test = () => {
    const params = [
        {
            input: {
                arr: [2,3,1,6,7],
            },
            output: 4,
        },
        {
            input: {
                arr: [1,1,1,1,1],
            },
            output: 10,
        },
    ];

    params.forEach(({input, output}) => {
        const { arr } = input;
        const result = countTriplets(arr);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();