function snakesAndLadders(board: number[][]): number {
    const visited: number[] = new Array(board.length**2).fill(0);
    let res: number = Number.MAX_VALUE;

    const getLocById = (id: number): number[] => {
        const rowRem: number = Math.ceil(id / board.length);
        const row: number = board.length - rowRem;

        let rem: number = id % board.length;
        let col: number = (board.length + rem - 1) % board.length;
        if ((rowRem % 2) === 0) {
            col = (board.length - rem) % board.length;
        }
        return [row, col];
    }

    const dfs = (id: number, steps: number): void => {
        if (id === board.length**2) {
            res = Math.min(res, steps);
            return;
        }

        for (let i: number = 1; i < 7; ++i) {
            const nei: number = id + 1;
            if (nei > board.length**2 || visited[nei] === 1) {
                continue;
            }
            visited[nei] = 1;
            const [r, c] = getLocById(nei);

            if (board[r][c] === -1) {
                dfs(nei, steps + 1);
            } else {
                dfs(board[r][c], steps + 1);
            }
        }
    }
    // dfs(1, 0);

    // console.log(
    //     'id', 36, getLocById(36),
    //     'id', 35, getLocById(35),
    //     'id', 34, getLocById(34),
    //     'id', 31, getLocById(31),
    //     'id', 25, getLocById(25),
    //     'id', 30, getLocById(30),
    //     'id', 24, getLocById(24),
    //     'id', 19, getLocById(19),
    //     'id', 1, getLocById(1),
    //     'id', 6, getLocById(6),
    // )

    const queue: number[][] = [[1, 0]];

    while (queue.length) {
        const [id, steps] = queue.shift();

        if (id === board.length**2) {
            res = Math.min(res, steps);
            continue;
        }

        for (let i: number = 1; i < 7; ++i) {
            const nei: number = id + i;
            if (nei > board.length**2 || visited[nei] === 1) {
                continue;
            }

            visited[nei] = 1;
            const [r, c] = getLocById(nei);

            if (board[r][c] === -1) {
                queue.push([nei, steps + 1]);
            } else {
                queue.push([board[r][c], steps + 1]);
            }
        }
    }

    return res === Number.MAX_VALUE ? -1 : res;
};

/*

[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]
]

*/

const test = () => {
    const params = [
        {
            input: [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]],
            output: 4,
        },
        {
            input: [
                [-1,-1],
                [-1,3]
            ],
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const result = snakesAndLadders(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();