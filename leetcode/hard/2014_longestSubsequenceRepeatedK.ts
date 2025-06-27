function longestSubsequenceRepeatedK(s: string, k: number): string {
    const isValidSubsequence = (substring: string) => {
        let count: number = 0;
        let i: number = 0;

        for (const char of s) {
            if (char === substring[i]) {
                i += 1;
                if (i === substring.length) {
                    count += 1;
                    i = 0;
                }
            }
        }

        return count >= k;
    };


    const queue: string[] = [];
    const chars: Map<string, number> = new Map();

    for (const char of s) {
        const count: number = chars.get(char) || 0;
        chars.set(char, count + 1);
    }

    for (let i: number = 0; i < 26; ++i) {
        const char: string = String.fromCharCode(97 + i);
        const count: number = chars.get(char) || 0;
        if (count >= k) {
            queue.push(char);
        }
    }


    let res: string = '';

    while (queue.length > 0) {
        const substring: string = queue.shift();
        if (!isValidSubsequence(substring)) {
            continue;
        }
        res = substring;

        for (let i: number = 0; i < 26; ++i) {
            const char: string = String.fromCharCode(97 + i);
            const count: number = chars.get(char) || 0;
            if (count < k) {
                continue;
            }

            queue.push(substring + char);
        };

    }

    return res;
};


const test = () => {
    const params = [
        {
            input: {
                s: 'letsleetcode', k: 2,
            },
            output: 'let',
        },
        {
            input: {
                s: 'bb', k: 2,
            },
            output: 'b',
        },
        {
            input: {
                s: 'ab', k: 2,
            },
            output: '',
        },
        {
            input: {
                s: 'aaabbb', k: 2,
            },
            output: 'b',
        },
        {
            input: {
                s: 'bbbaaa', k: 2,
            },
            output: 'b',
        },
    ];

    params.forEach(({input, output}) => {
        const { s, k } = input;
        const result = longestSubsequenceRepeatedK(s, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

