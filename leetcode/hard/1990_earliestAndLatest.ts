function earliestAndLatest(n: number, firstPlayer: number, secondPlayer: number): number[] {
    let left: number = Math.min(firstPlayer, secondPlayer);
    let right: number = Math.max(firstPlayer, secondPlayer);

    // check the mirror position;
    // 2+4-1 = 5
    if (left + right - 1 === n) {
        return [1, 1];
    }
    // 1 2 3 4; 2 4;
    if (n <= 4) {
        return [2, 2];
    }

    // mirror to left
    if (left - 1 > n - right) {
        const tmp: number = left;
        left = n + 1 - right;
        right = n - (tmp - 1);
    }

    let min: number = n;
    let max: number = 1;
    const nextN: number = Math.ceil(n / 2);

    // one side; 1 2 3 4 5
    if (right * 2 <= n + 1) {
        const before: number = left - 1;
        const between: number = right - left - 1;
        // 0 - all loose, before - all win
        for (let i: number = 0; i <= before; ++i) {
            for (let j: number = 0; j <= between; ++j) {
                // 0+1; all loose, only left player win
                const firstPos: number = i + 1;
                // 0+0+2; all loose, only left and right players win
                const secondPos: number = i + j + 2;
                const [mi, ma] = earliestAndLatest(nextN, firstPos, secondPos);
                min = Math.min(min, mi + 1);
                max = Math.max(max, ma + 1);
            }
        }
    }
    // different sizes
    else {
        const mirrorRight: number = n - right + 1; // this one will loose
        const before: number = left - 1; // before left combinations
        const beforeMirror: number = mirrorRight - left - 1; // before left and mirror combinations
        const afterMirror: number = right - mirrorRight - 1; // before mirror and right
        const newAfterMirror = Math.ceil(afterMirror / 2); // half of them will loose, not important which one

        for (let i: number = 0; i <= before; ++i) {
            for (let j: number = 0; j <= beforeMirror; ++j) {
                const firstPos: number = i + 1; // left player + players who win
                const secondPos: number = i + j + newAfterMirror + 2; // left + right + win + half after mirror

                const [mi, ma] = earliestAndLatest(nextN, firstPos, secondPos);
                min = Math.min(min, mi + 1);
                max = Math.max(max, ma + 1);
            }
        }
    }


    return [min, max];
};

/*

1 2 3 4 5

1 2 3 4 -
- 2 3 4 -
1 2 3 - -

- 2 3 4 5
- 3 4 5


*/

const test = () => {
    const params = [
        {
            input: {
                n: 5, firstPlayer: 1, secondPlayer: 4,
            },
            output: [2, 2],
        },
        {
            input: {
                n: 11, firstPlayer: 2, secondPlayer: 4,
            },
            output: [3,4],
        },
        {
            input: {
                n: 5, firstPlayer: 1, secondPlayer: 5,
            },
            output: [1,1],
        },
    ];

    params.forEach(({ input, output }) => {
        const { n, firstPlayer, secondPlayer } = input;
        const result = earliestAndLatest(n, firstPlayer, secondPlayer);

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
