function kthCharacter(k: number): string {
    // a 97
    // z 122
    let word: number[] = [0];
    let left: number = 0;

    while (word.length <= k) {
        for (let i: number = 0; i <= left; ++i) {
            word.push((word[i] + 1) % 26);
            if (word.length === k) {
                return String.fromCharCode(97 + word.at(-1));
            }
        }
        left = word.length - 1;
    }

    return 'a';
};

const test = () => {
    const params = [
        {
            input: {
                k: 5
            },
            output: 'b',
        },
        {
            input: {
                k: 10
            },
            output: 'c',
        },
    ];

    for (const { input, output } of params) {
        const { k } = input;
        const result = kthCharacter(k);

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
