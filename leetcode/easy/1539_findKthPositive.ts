function findKthPositive(arr: number[], k: number): number {
    let count: number = arr[0] - 1;
    if (count >= k) {
        return k;
    }

    for (let i: number = 1; i < arr.length; ++i) {
        if (arr[i] - arr[i - 1] > 1) {
            const missed: number = arr[i] - arr[i - 1] - 1;
            if (count + missed < k) {
                count += missed;
                continue;
            }

            const remainder: number = k - count;
            return arr[i-1] + remainder;
        }
    }

    const remainder: number = k - count;

    return arr.at(-1) + remainder;
};

const test = () => {
    const params = [
        {
            input: {
                arr: [2,3,4,7,11], k: 5,
            },
            output: 9,
        },
        {
            input: {
                arr: [1,2,3,4], k: 2,
            },
            output: 6,
        },
    ];

    for (const { input, output } of params) {
        const { arr, k } = input;
        const result = findKthPositive(arr, k);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
