function minNumberOperations(target: number[]): number {
    let res: number = 0;
    const stack: number[] = [];

    for (const num of target) {
        if (stack.length === 0) {
            res += num;
            stack.push(num);
            continue;
        }

        if (stack.at(-1) === num) {
            continue;
        }

        if (stack.at(-1) < num) {
            res += num - stack.at(-1);
            stack.push(num);
            continue;
        }

        if (stack.at(-1) > num) {
            while (stack.length !== 0 && stack.at(-1) > num) {
                stack.pop();
            }
            if (stack.length === 0 || stack.at(-1) < num) {
                stack.push(num);
            }
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                target: [1,2,3,2,1],
            },
            output: 3,
        },
        {
            input: {
                target: [3,1,1,2],
            },
            output: 4,
        },
        {
            input: {
                target: [3,1,5,4,2],
            },
            output: 7,
        },
    ];

    params.forEach(({input, output}) => {
        const { target } = input;
        const result = minNumberOperations(target);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();