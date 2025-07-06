function possibleStringCount(word: string): number {
    let res: number = 1;

    for (let i: number = 0; i < word.length; ++i) {
        if (word[i] === word[i-1]) {
            res += 1;
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                word: "abbcccc",
            },
            output: 5,
        },
        {
            input: {
                word: "abcd",
            },
            output: 1,
        },
        {
            input: {
                word: "aaaa",
            },
            output: 4,
        },
    ];

    for (const { input, output } of params) {
        const { word } = input;
        const result = possibleStringCount(word);

        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                'SUCCESS: \n',
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
