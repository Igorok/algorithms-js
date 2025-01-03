/**
 * @param {string[]} words
 * @param {number[][]} queries
 * @return {number[]}
 */
var vowelStrings = function(words, queries) {
    const vowels = ['a', 'e', 'i', 'o', 'u'];
    const prefix = new Array(words.length).fill(0);

    for (let i = 0; i < words.length; ++i) {
        const prev = i > 0 ? prefix[i-1] : 0;
        prefix[i] = prev;
        if (
            vowels.includes(words[i][0]) &&
            vowels.includes(words[i].at(-1))
        ) {
            prefix[i] += 1;
        }
    }

    return queries.map(([s, e]) => {
        const left = s > 0 ? prefix[s-1] : 0;
        return prefix[e] - left;
    });
};

const test = () => {
    const params = [
        {
            input: [['aba','bcb','ece','aa','e'], [[0,2],[1,4],[1,1]]],
            output: [2,3,0],
        },
        {
            input: [['a','e','i'], [[0,2],[0,1],[2,2]]],
            output: [3,2,1],
        },
    ];

    params.forEach(({input, output}) => {
        const result = vowelStrings(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();