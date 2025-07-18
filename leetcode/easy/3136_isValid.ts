function isValid(word: string): boolean {
    if (word.length < 3) {
        return false;
    }

    word = word.toLowerCase();
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);

    let vCount: number = 0;
    let cCount: number = 0;

    for (let i: number = 0; i < word.length; ++i) {
        if (Number.isInteger(parseInt(word[i]))) {
            continue;
        }

        const code: number = word.charCodeAt(i);
        if (code < 97 || code > 122) {
            return false;
        }

        if (vowels.has(word[i])) {
            vCount += 1;
        } else {
            cCount += 1;
        }
    }


    return vCount !== 0 && cCount !== 0;
};

/*
a - 97
z - 122
A - 65
Z - 90



*/

const test = () => {
    const params = [
        {
            input: {
                word: "234Adas",
            },
            output: true,
        },
        {
            input: {
                word: "b3",
            },
            output: false,
        },
        {
            input: {
                word: "a3$e",
            },
            output: false,
        },
    ];

    params.forEach(({input, output}) => {
        const { word } = input;
        const result = isValid(word);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();