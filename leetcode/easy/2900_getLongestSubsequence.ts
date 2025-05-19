function getLongestSubsequence(words: string[], groups: number[]): string[] {
    const sequences: number[][] = [[], []];

    for (let i: number = 0; i < groups.length; ++i) {
        const group: number = groups[i];

        if (group === 0) {
            if (sequences[0].length === 0 || groups[sequences[0].at(-1)] === 1) {
                sequences[0].push(i);
            }

            if (groups[sequences[1].at(-1)] === 1) {
                sequences[1].push(i);
            }
        } else {
            if (sequences[1].length === 0 || groups[sequences[1].at(-1)] === 0) {
                sequences[1].push(i);
            }

            if (groups[sequences[0].at(-1)] === 0) {
                sequences[0].push(i);
            }
        }
    }

    let res: string[] = (sequences[0].length > sequences[1].length ? sequences[0] : sequences[1])
        .map((i: number) => words[i]);

    return res;
};

/*

1 0 1 0 1
1 1 1 0 0
0 0 1 1 0 1 0 1


*/

const test = () => {
    const params = [
        {
            input: { words: ["e","a","b"], groups: [0,0,1] },
            output: ["e","b"],
        },
        {
            input: { words: ["a","b","c","d"], groups: [1,0,1,1] },
            output: ["a","b","c"],
        },
    ];

    params.forEach(({input, output}) => {
        const { words, groups } = input;

        const result = getLongestSubsequence(words, groups);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();