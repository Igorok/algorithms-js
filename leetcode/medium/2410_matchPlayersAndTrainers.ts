function matchPlayersAndTrainers(players: number[], trainers: number[]): number {
    players.sort((a, b) => a - b);
    trainers.sort((a, b) => a - b);

    let i: number = 0;
    let j: number = 0;

    while (i < players.length && j < trainers.length) {
        if (players[i] <= trainers[j]) {
            i += 1;
            j += 1;
        } else {
            j += 1;
        }
    }

    return i;
};

const test = () => {
    const params = [
        {
            input: {
                players: [4,7,9], trainers: [8,2,5,8]
            },
            output: 2,
        },
        {
            input: {
                players: [1,1,1], trainers: [10]
            },
            output: 1,
        },
    ];

    params.forEach(({ input, output }) => {
        const { players, trainers } = input;
        const result = matchPlayersAndTrainers(players, trainers);

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
