function findingUsersActiveMinutes(logs: number[][], k: number): number[] {
    const countByUsers: Map<number, Set<number>> = new Map();
    for (const [id, min] of logs) {
        const cnt: Set<number> = countByUsers.get(id) || new Set();
        cnt.add(min);
        countByUsers.set(id, cnt)
    }

    const countByUAM: Map<number, number> = new Map();

    countByUsers.forEach((val) => {
        const cnt: number = countByUAM.get(val.size) || 0;
        countByUAM.set(val.size, cnt + 1);
    });

    const res: number[] = new Array(k).fill(0);

    for (let i: number = 1; i <= k; ++i) {
        res[i-1] = countByUAM.get(i) || 0;
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                logs: [[0,5],[1,2],[0,2],[0,5],[1,3]], k: 5,
            },
            output: [0,2,0,0,0],
        },
        {
            input: {
                logs: [[1,1],[2,2],[2,3]], k: 4,
            },
            output: [1,1,0,0],
        },
    ];

    params.forEach(({ input, output }) => {
        const { logs, k } = input;
        const result = findingUsersActiveMinutes(logs, k);

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
