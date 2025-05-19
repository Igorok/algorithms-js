function getWordsInLongestSubsequence(words: string[], groups: number[]): string[] {
    const length: number[] = new Array(words.length).fill(1);
    const parent: number[] = new Array(words.length).fill(-1);
    let maxId: number = 0;


    const isSubsequence = (i1: number, i2: number): boolean => {
        if (groups[i1] === groups[i2]) {
            return false;
        }
        const w1: string = words[i1];
        const w2: string = words[i2];
        if (w1.length !== w2.length) {
            return false;
        }

        let diff: number = 0;
        for (let i = 0; i < w1.length; ++i) {
            if (w1[i] !== w2[i]) {
                diff += 1;
                if (diff === 2) {
                    return false;
                }
            }
        }

        return true;
    }

    for (let i: number = 0; i < words.length; ++i) {
        for (let j: number = i - 1; j > -1; --j) {
            if (isSubsequence(i, j)) {
                if (length[j] + 1 > length[i]) {
                    length[i] = length[j] + 1;
                    parent[i] = j;
                }
                if (length[i] > length[maxId]) {
                    maxId = i;
                }
            }
        }
    }

    let res: string[] = [];

    while (maxId !== -1) {
        res.push(words[maxId]);
        maxId = parent[maxId];
    }


    return res.reverse();
};


const test = () => {
    const params = [
        {
            input: { words: ["cb","dcc","da","cbb","bd","dbc","ab","db"], groups: [4,5,5,7,8,1,3,4] },
            output: ["cb","ab","db"],
        },
        {
            input: { words: ["bab","dab","cab"], groups: [1,2,2] },
            output: ["bab","cab"],
        },
        {
            input: { words: ["a","b","c","d"], groups: [1,2,3,4] },
            output: ["a","b","c","d"],
        },
    ];

    params.forEach(({input, output}) => {
        const { words, groups } = input;

        const result = getWordsInLongestSubsequence(words, groups);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();