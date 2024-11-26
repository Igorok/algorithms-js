/**
 * @param {number[][]} board
 * @return {number}
 */
var slidingPuzzle = function(board) {
    const puzzlePath = [
        [1, 3],
        [0, 2, 4],
        [1, 5],
        [0, 4],
        [1, 3, 5],
        [2, 4],
    ];

    const boardArr = board.reduce((acc, val) => ([...acc, ...val]), []);


    console.log('boardArr', boardArr);

    const visited = new Set();

    const queue = [[
        boardArr.findIndex(v => v === 0),
        boardArr.join(''),
        0,
    ]];

    while (queue.length) {
        const [id, puzzle, length] = queue.shift();

        if (visited.has(puzzle)) {
            continue;
        } else {
            visited.add(puzzle);
        }

        if (puzzle === '123450') return length;

        for (const nei of puzzlePath[id]) {
            const arr = puzzle.split('');
            arr[id] = puzzle[nei];
            arr[nei] = '0';
            queue.push([nei, arr.join(''), length + 1]);
        }
    }



    return -1;
};

/*
0 - (0, 0)
1 - (0, 1)
2 - (0, 2)
3 - (1, 0)
4 - (1, 1)
5 - (1, 2)

  0 1 2
0 0 1 2
1 3 4 5

[
    [1, 3],
    [0, 2, 4],
    [1, 5],
    [0, 4],
    [1, 3, 5],
    [2, 4],
]





*/

const test = () => {
    const params = [
        {
            input: [[1,2,3],[4,0,5]],
            output: 1,
        },
        {
            input: [[1,2,3],[5,4,0]],
            output: -1,
        },
        {
            input: [[4,1,2],[5,0,3]],
            output: 5,
        },
    ];

    for (const { input, output } of params) {
        const result = slidingPuzzle(input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
