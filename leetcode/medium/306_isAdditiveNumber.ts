function isAdditiveNumber(num: string): boolean {
    const rec = (id: number, stack: number[]) => {
        if (id === num.length) {
            return stack.length >= 3;
        }

        if (stack.length < 2) {
            for (let i = id+1; i <= num.length; ++i) {
                const sliced: string = num.slice(id, i);
                if (sliced.length > 1 && sliced.startsWith('0')) {
                    return false;
                }
                const n: number = Number(num.slice(id, i));
                stack.push(n);
                if (rec(i, stack)) {
                    return true;
                }
                stack.pop();
            }
            return false;
        }

        const target: string = String((stack.at(-1)||0) + (stack.at(-2)||0));

        if (id + target.length > num.length) {
            return false;
        }

        const sliced: string = num.slice(id, id + target.length);
        if (sliced !== target || (sliced.length > 1 && sliced.startsWith('0'))) {
            return false;
        }

        stack.push(Number(sliced));

        const r: boolean = rec(id + target.length, stack);

        stack.pop();

        return r;
    }


    return rec(0, []);
};

const test = () => {
    const params = [
        {
            input: '011112',
            output: false,
        },
        {
            input: '1023',
            output: false,
        },
        {
            input: '101',
            output: true,
        },
        {
            input: '111',
            output: false,
        },
        {
            input: '112358',
            output: true,
        },
        {
            input: '199100199',
            output: true,
        },
        {
            input: '1',
            output: false,
        },
    ];

    params.forEach(({input, output}) => {
        const result = isAdditiveNumber(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();