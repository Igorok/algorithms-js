/**
 * @param {character[][]} box
 * @return {character[][]}
 */
var rotateTheBox = function(box) {
    const res = new Array(box[0].length).fill(0).map(() => new Array(box.length).fill('.'));

    console.log('res', res);

    const fillBox = (y, x, count) => {
        let i = x;
        let j = res[0].length - y - 1;

        while (count !== 0) {
            res[i][j] = '#';
            i -= 1;
            count -= 1;
        }
    }

    for (let i = 0; i < box.length; ++i) {
        let countStones = 0;
        for (let j = 0; j < box[0].length; ++j) {
            if (box[i][j] === '#') countStones += 1;
            if (box[i][j] === '*') {
                res[j][res[0].length - 1 - i] = '*';

                fillBox(i, j - 1, countStones);
                countStones = 0;
            }
        }
        fillBox(i, box[0].length - 1, countStones);
    }

    return res;
};



const test = () => {
    const params = [
        {
            input: [["#",".","#"]],
            output: [
                ["."],
                ["#"],
                ["#"]
            ],
        },
        {
            input: [
                ["#",".","*","."],
                ["#","#","*","."]
            ],
            output: [
                ["#","."],
                ["#","#"],
                ["*","*"],
                [".","."]
            ],
        },
        {
            input: [
                ["#","#","*",".","*","."],
                ["#","#","#","*",".","."],
                ["#","#","#",".","#","."]
            ],
            output: [
                [".","#","#"],
                [".","#","#"],
                ["#","#","*"],
                ["#","*","."],
                ["#",".","*"],
                ["#",".","."]
            ],
        },
    ];

    params.forEach(({input, output}) => {
        const result = rotateTheBox(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();