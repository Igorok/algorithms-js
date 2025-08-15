function nthSuperUglyNumber(n: number, primes: number[]): number {
    const allIds: Map<number, number> = new Map();
    const allNumbers: Map<number, number[]> = new Map();
    for (const prime of primes) {
        allIds.set(prime, 0);
        allNumbers.set(prime, [1]);
    }

    let i: number = 1;

    while (i <= n) {
        let min: number = Number.MAX_SAFE_INTEGER;

        allNumbers.forEach((arr: number[], prime: number) => {
            const id: number = allIds.get(prime);
            min = Math.min(min, arr[id]);
        });

        if (i === n) {
            return min;
        }

        allNumbers.forEach((arr: number[], prime: number) => {
            arr.push(min * prime);
            allNumbers.set(prime, arr);
        });

        allNumbers.forEach((arr: number[], prime: number) => {
            let id: number = allIds.get(prime);
            while (arr[id] === min) {
                id += 1;
            }
            allIds.set(prime, id);
        });

        i += 1;
    }

    return 0;
};

const test = () => {
    const params = [
        {
            input: {
                n: 12, primes: [2,7,13,19],
            },
            output: 32,
        },
        {
            input: {
                n: 1, primes: [2,3,5]
            },
            output: 1,
        },
    ];

    params.forEach(({ input, output }) => {
        const { n, primes } = input;
        const result = nthSuperUglyNumber(n, primes);

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
