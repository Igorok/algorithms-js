function longestSubstring_0(s: string, k: number): number {
    if (k > s.length) return 0;
    if (k === 1) return s.length;

    const aCode: number = 'a'.charCodeAt(0);

    const countOnChar = new Array(s.length).fill(0).map(() => new Array(26).fill(0));
    for (let i: number = 0; i < s.length; ++i) {
        if (i > 0) {
            for (let j: number = 0; j < 26; ++j) {
                countOnChar[i][j] += countOnChar[i-1][j];
            }
        }

        const code: number = s.charCodeAt(i) - aCode;
        countOnChar[i][code] += 1;
    }

    let res: number = 0;

    for (let i: number = 0; i < s.length; ++i) {
        const prev: number[] = i === 0 ? new Array(26).fill(0) : countOnChar[i-1];

        for (let j: number = i+1; j < s.length; ++j) {
            let length: number = 0;

            for (let c: number = 0; c < 26; ++c) {
                const v: number = countOnChar[j][c] - prev[c];
                if (v >= k) {
                    length += v;
                }
                if (v !== 0 && v < k) {
                    length = 0;
                    break;
                }
            }

            res = Math.max(res, length);
        }
    }


    return res;
};

function longestSubstring(s: string, k: number): number {
    if (k > s.length) return 0;
    if (k === 1) return s.length;

    const aCode: number = 'a'.charCodeAt(0);

    const countChars = new Array(26).fill(0);
    for (let i: number = 0; i < s.length; ++i) {
        const code: number = s.charCodeAt(i) - aCode;
        countChars[code] += 1;
    }

    let id: number = -1;
    for (let i: number = 0; i < s.length; ++i) {
        const code: number = s.charCodeAt(i) - aCode;
        if (countChars[code] < k) {
            id = i
            break;
        }
    }

    if (id === -1) {
        return s.length;
    }

    const left: number = longestSubstring(s.slice(0, id), k);
    const right: number = longestSubstring(s.slice(id+1), k);


    return Math.max(left, right);
};

const test = () => {
    const params = [
        {
            input: {
                s: "bbaaacbd", k: 3,
            },
            output: 3,
        },
        {
            input: {
                s: "aaabb", k: 3,
            },
            output: 3,
        },
        {
            input: {
                s: "ababbc", k: 2,
            },
            output: 5,
        },
    ];

    params.forEach(({input, output}) => {
        const { s, k } = input;
        const result = longestSubstring(s, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();