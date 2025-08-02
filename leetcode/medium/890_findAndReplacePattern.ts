function findAndReplacePattern(words: string[], pattern: string): string[] {
    const getPattern = (word: string): string => {
        const res: number[] = [];
        const used: Map<string, number> = new Map();
        let val: number = -1;

        for (const char of word) {
            if (!used.has(char)) {
                val += 1;
                used.set(char, val);
            }

            res.push(used.get(char));
        }

        return res.join('_');
    };

    const target: string = getPattern(pattern);
    const res: string[] = [];

    for (const word of words) {
        const r: string = getPattern(word);
        if (target === r) {
            res.push(word);
        }
    }


    return res;
};

const test = () => {
    const params = [
        {
            input: {
                words: ["abc","deq","mee","aqq","dkd","ccc"], pattern: "abb"
            },
            output: ["mee","aqq"],
        },
        {
            input: {
                words: ["a","b","c"], pattern: "a"
            },
            output: ["a","b","c"],
        },
    ];

    params.forEach(({ input, output }) => {
        const { words, pattern } = input;
        const result = findAndReplacePattern(words, pattern);

        console.log(
            JSON.stringify(result) === JSON.stringify(output)
                ? "SUCCESS "
                : "ERROR ",
            "input",
            JSON.stringify(input),
            "output",
            output,
            "result",
            result,
        );
    });
};

test();
