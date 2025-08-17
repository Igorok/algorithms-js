function numberOfWays_0(n: number, x: number): number {
    const mod: number = 7 + 10**9;

    let numbers: number[] = new Array(n + 1).fill(0);
    for (let i: number = 1; i <= n; ++i) {
        const v: number = i ** x;
        if (v > n) {
            break;
        }
        numbers[v] = 1;
    }
    numbers = numbers.reduce((acc: number[], val: number, id: number) => {
        if (val === 1) {
            acc.push(id);
        }
        return acc;
    }, []);

    const memo: Map<string, number> = new Map();

    const dfs = (acc: number, id: number): number => {
        if (acc === n) {
            return 1;
        }
        if (acc > n) {
            return 0;
        }
        if (id === numbers.length) {
            return 0;
        }

        const key: string = `${acc}_${id}`;

        if (memo.has(key)) return memo.get(key);

        let r: number = dfs(acc + numbers[id], id + 1);
        r += dfs(acc, id + 1);

        r %= mod;

        memo.set(key, r);

        return r;
    }


    return dfs(0, 0);
};



function numberOfWays(n: number, x: number): number {
    const mod: number = 7 + 10**9;

    let numbers: number[] = new Array(n + 1).fill(0);
    for (let i: number = 1; i <= n; ++i) {
        const v: number = i ** x;
        if (v > n) {
            break;
        }
        numbers[v] = 1;
    }
    numbers = numbers.reduce((acc: number[], val: number, id: number) => {
        if (val === 1) {
            acc.push(id);
        }
        return acc;
    }, []);

    let prev: number[] = new Array(n+1).fill(0);
    let curr: number[] = new Array(n+1).fill(0);

    for (const num of numbers) {
        curr = new Array(n+1).fill(0);

        for (let sum: number = 1; sum <= n; ++sum) {
            curr[sum] = prev[sum] % mod;
            if (sum === num) {
                curr[sum] += 1;
                curr[sum] %= mod;
                continue;
            }

            curr[sum] += (sum > num) ? prev[sum - num] : 0;
            curr[sum] %= mod;
        }

        prev = curr;
    }

    return curr.at(-1);
};

/*

--0 1 2 3 4 5
0 0 0 0 0 0 0
1 0 1 0 0 0 0
2 0 1 1 1 0 0
3 0 1 1 2 1 1

*/

const test = () => {
    const params = [
        {
            input: {
                n: 10, x: 2,
            },
            output: 1,
        },
        {
            input: {
                n: 4, x: 1,
            },
            output: 2,
        },
        {
            input: {
                n: 20, x: 1,
            },
            output: 64,
        },
        {
            input: {
                n: 30, x: 1,
            },
            output: 296,
        },
        {
            input: {
                n: 100, x: 1,
            },
            output: 444793,
        },
        {
            input: {
                n: 300, x: 1,
            },
            output: 872471266,
        },
    ];

    params.forEach(({ input, output }) => {
        const { n, x } = input;
        const result = numberOfWays(n, x);

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
