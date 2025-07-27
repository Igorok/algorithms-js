function maximumGain_0(s: string, x: number, y: number): number {
    const stack: string[] = [];
    let res: number = 0;

    for (const char of s) {
        if (char === 'b' && stack.length && stack.at(-1) === 'a') {
            stack.pop();
            res += x;
            continue;
        }

        if (char === 'a' && stack.length && stack.at(-1) === 'b') {
            stack.pop();
            res += y;
            continue;
        }

        stack.push(char);
    }

    return res;
};

function maximumGain(s: string, x: number, y: number): number {
    let res: number = 0;

    const rec = (str: string, remove: string) => {
        const stack: string[] = []

        for (const char of str) {
            if (remove === 'x' && char === 'b' && stack.length && stack.at(-1) === 'a') {
                stack.pop();
                res += x;
                continue;
            }

            if (remove === 'y' && char === 'a' && stack.length && stack.at(-1) === 'b') {
                stack.pop();
                res += y;
                continue;
            }

            stack.push(char);
        }

        return stack.join('');
    };


    if (x > y) {
        const str: string = rec(s, 'x');
        rec(str, 'y');
    } else {
        const str: string = rec(s, 'y');
        rec(str, 'x');
    }

    return res;
};


/*

abababa

*/



const test = () => {
    const params = [
        {
            input: {
                s: "cdbcbbaaabab", x: 4, y: 5,
            },
            output: 19,
        },
        {
            input: {
                s: "aabbaaxybbaabb", x: 5, y: 4,
            },
            output: 20,
        },
    ];

    params.forEach(({input, output}) => {
        const { s, x, y } = input;
        const result = maximumGain(s, x, y);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();