function wordBreak_0(s: string, wordDict: string[]): string[] {
    const res: string[] = [];

    const dfs = (s: string, sentence: string[]) => {
        if (s.length === 0) {
            res.push(sentence.join(' '));
            return;
        }

        for (let i: number = 0; i < wordDict.length; ++i) {
            const w: string = wordDict[i];
            if (s.startsWith(w)) {
                sentence.push(w);

                dfs(s.slice(w.length), sentence);

                sentence.pop();
            }
        }
    };

    dfs(s, []);

    return res;
};

function wordBreak(s: string, wordDict: string[]): string[] {
    const memo: Map<string, string[]> = new Map();

    const dfs = (str: string) => {
        if (str.length === 0) {
            return [];
        }

        if (memo.has(str)) {
            return memo.get(str);
        }

        let res: string[] = [];

        for (let i: number = 0; i < wordDict.length; ++i) {
            const w: string = wordDict[i];

            if (w === str) {
                res.push(w);
            } else if (str.startsWith(w)) {
                const substrings: string[] = dfs(str.slice(w.length));

                if (substrings.length !== 0) {
                    for (const substr of substrings) {
                        res.push([w, substr].join(' '));
                    }
                }
            }
        }

        memo.set(str, res);

        return res;
    };

    return dfs(s);
};

/*

ERROR  input {"s":"pineapplepenapple","wordDict":["apple","pen","applepen","pine","pineapple"]} output [
  'pine apple pen apple',
  'pineapple pen apple',
  'pine applepen apple'
] result [ 'pine applepen apple', 'pineapple pen apple' ]


pine apple pen apple


*/


const test = () => {
    const params = [
        {
            input: {
                s: "catsanddog", wordDict: ["cat","cats","and","sand","dog"],
            },
            output: ["cats and dog","cat sand dog"],
        },
        {
            input: {
                s: "pineapplepenapple", wordDict: ["apple","pen","applepen","pine","pineapple"],
            },
            output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"],
        },
        {
            input: {
                s: "catsandog", wordDict: ["cats","dog","sand","and","cat"]
            },
            output: [],
        },
    ];

    params.forEach(({input, output}) => {
        const { s, wordDict } = input;

        const result = wordBreak(s, wordDict);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();