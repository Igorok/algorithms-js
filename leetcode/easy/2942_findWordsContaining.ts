function findWordsContaining(words: string[], x: string): number[] {
    return words.reduce((acc: number[], val: string, id: number) => {
        if (val.includes(x)) {
            acc.push(id);
        }
        return acc;
    }, []);
};

const test = () => {
    const params = [
        {
            input: { words: ["leet","code"], x: "e" },
            output: [0,1],
        },
        {
            input: { words: ["abc","bcd","aaaa","cbc"], x: "a" },
            output: [0,2],
        },
        {
            input: { words: ["abc","bcd","aaaa","cbc"], x: "z" },
            output: [],
        },
    ];

    params.forEach(({input, output}) => {
        const { words, x } = input;
        const result = findWordsContaining(words, x);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();