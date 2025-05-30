function shortestCompletingWord(licensePlate: string, words: string[]): string {
    const aCode = 'a'.charCodeAt(0);
    const zCode = 'z'.charCodeAt(0);
    const countChars = new Map();

    for (let i = 0; i < licensePlate.length; ++i) {
        const char = licensePlate[i].toLowerCase();
        const chatCode = char.charCodeAt(0);

        if (chatCode >= aCode && chatCode <= zCode) {
            const count = (countChars.get(char) || 0) + 1;
            countChars.set(char, count);
        }
    }

    const getCount = (word: string) => {
        const cCount = new Map();
        for (const char of word) {
            const c: number = (cCount.get(char) || 0) + 1;
            cCount.set(char, c);
        }
        return cCount;
    }

    let res = null;

    for (const word of words) {
        const cCount = getCount(word);

        let isOk = true;

        countChars.forEach((v, k) => {
            const c = cCount.get(k) || 0;
            if (c < v) {
                isOk = false;
                return;
            }
        });

        if (isOk && (res === null || res.length > word.length)) {
            res = word;
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                licensePlate: "1s3 456", words: ["looks","pest","stew","show"]
            },
            output: 'pest',
        },
        {
            input: {
                licensePlate: "1s3 PSt", words: ["step","steps","stripe","stepple"]
            },
            output: 'steps',
        },
    ];

    params.forEach(({input, output}) => {
        const {licensePlate, words} = input;
        const result = shortestCompletingWord(licensePlate, words);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();