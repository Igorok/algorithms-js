function uniqueMorseRepresentations(words: string[]): number {
    const codes: string[] = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
    const aCode: number = 'a'.charCodeAt(0);
    const unique: Set<string> = new Set();

    for (const word of words) {
        const encoded: string[] = [];

        for (const char of word) {
            const code: number = char.charCodeAt(0) - aCode;
            encoded.push(codes[code]);
        }

        unique.add(encoded.join(''));
    }

    return unique.size;
};

const test = () => {
    const params = [
        {
            input: {
                words: ["gin","zen","gig","msg"],
            },
            output: 2,
        },
        {
            input: {
                words: ["a"]
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { words } = input;
        const result = uniqueMorseRepresentations(words);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();