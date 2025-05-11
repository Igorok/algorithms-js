function threeConsecutiveOdds(arr: number[]): boolean {
    if (arr.length < 3) return false;

    let count: number = 0;
    for (let i: number = 0; i < arr.length; ++i) {
        if (i - 3 > -1 && (arr[i-3] % 2) === 1) {
            count -= 1;
        }
        if ((arr[i] % 2) === 1) {
            count += 1;
            if (count === 3) {
                return true;
            }
        }

    }

    return false;
};

const test = () => {
    const params = [
        {
            input: [2,6,4,1],
            output: false,
        },
        {
            input: [1,2,34,3,4,5,7,23,12],
            output: true,
        },
    ];

    for (const { input, output } of params) {
        const result = threeConsecutiveOdds(input);
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
