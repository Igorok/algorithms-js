function answerString_0(word: string, numFriends: number): string {
    if (numFriends === 1) {
        return word;
    }

    let res: string = word[0];

    const maxLength: number = word.length - numFriends + 1;
    let left: number = 0;
    for (let right = 1; right < word.length; ++right) {
        let length: number = right - left + 1;

        while (length > maxLength || (left < right && word[left] < word[left + 1])) {
            left += 1;
            length = right - left + 1;

            const w: string = word.slice(left, right+1);
            if (w > res) {
                res = w;
            }
        }

        const w: string = word.slice(left, right+1);
        if (w > res) {
            res = w;
        }
    }

    let length: number = word.length - left + 1;
    while (length > maxLength || (left < word.length)) {
        left += 1;
        length = word.length - left + 1;

        const w: string = word.slice(left, word.length);
        if (w > res) {
            res = w;
        }
    }


    return res;
};

function answerString(word: string, numFriends: number): string {
    if (numFriends === 1) {
        return word;
    }

    let res: string = word[0];

    const maxDiff: number = word.length - numFriends + 1;
    for (let i = 0; i < word.length; ++i) {
        const w: string = word.slice(i, Math.min(word.length, i + maxDiff));

        if (w > res) {
            res = w;
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                word: "chgm", numFriends: 2,
            },
            output: 'm',
        },
        {
            input: {
                word: "dbca", numFriends: 2,
            },
            output: 'dbc',
        },
        {
            input: {
                word: "gggg", numFriends: 4,
            },
            output: 'g',
        },
        {
            input: {
                word: "abcdefjk", numFriends: 4,
            },
            output: 'k',
        },
        {
            input: {
                word: "abcdefjk", numFriends: 1,
            },
            output: 'abcdefjk',
        },
    ];

    params.forEach(({input, output}) => {
        const { word, numFriends } = input;

        const result = answerString(word, numFriends);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();
