function minDistance(word1, word2) {
    const table = new Array(word2.length + 1).fill(0)
        .map(() => new Array(word1.length + 1).fill(0));

    for (let i = 1; i < word2.length + 1; ++i) {
        table[i][0] = i;
    }

    for (let i = 1; i < word1.length + 1; ++i) {
        table[0][i] = i;
    }

    for (let i = 1; i < table.length; ++i) {
        for (let j = 1; j < table[i].length; ++j) {
            if (word2[i - 1] === word1[j - 1]) {
                table[i][j] = table[i - 1][j - 1];
                continue;
            }

            const del = table[i - 1][j];
            const add = table[i][j - 1];
            const change = table[i - 1][j - 1];

            table[i][j] = Math.min(del, add, change) + 1;
        }
    }

    console.log(JSON.stringify(table));

    return table[word2.length][word1.length];
};

/*
  -
- 0
r 1
o 2
s 2
  - h o r s e
- 0 1 2 3 4 5

    h o r s e
  0 1 2 3 4 5
r 1 1 2 2 3 4
o 2 2 1 2 3 4
s 3 3 2 2 2 3

del = [i - 1][j]
add = [i][j - 1]
change = [i - 1][j - 1]

[
[0,0,0,0,0,0],
[0,1,1,0,1,1],
[0,1,1,1,1,2],
[0,1,2,2,1,2]
]









*/



const test = () => {
    const params = [
        {
            input: ["horse", "ros"],
            output: 3,
        },
        {
            input: ["intention", "execution"],
            output: 5,
        },
    ];

    params.forEach(({input, output}) => {
        const result = minDistance(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', input,
            'output', output,
            'result', result,
        );

    });
};

test();
