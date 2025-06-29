function getPermutation(n: number, k: number): string {
    const factorials: number[] = new Array(10).fill(0);
    factorials[1] = 1;
    for (let i: number = 2; i < 10; ++i) {
        factorials[i] = factorials[i-1] * i;
    }

    let res: string = '';

    const getVal = (visited: Set<number>, acc: number) => {
        if (visited.size === n) {
            return visited;
        }

        let id: number = 0;
        let prev: number = acc;
        const comb: number = factorials[n - visited.size - 1];

        for (let i: number = 1; i < n + 1; ++i) {
            if (visited.has(i)) {
                continue;
            }

            id += 1;
            const count: number = Math.max(id * comb, 1);

            if (acc + count < k) {
                prev = acc + count;
                continue;
            }

            visited.add(i);
            res += String(i);

            return getVal(visited, prev);
        }

        return visited;
    };

    const visited = getVal(new Set(), 0);
    console.log('visited', visited);

    return res;
};

/*





*/

const test = () => {
    const params = [
        {
            input: {
                n: 3, k: 2,
            },
            output: '132',
        },
        {
            input: {
                n: 1, k: 1,
            },
            output: '1',
        },
        {
            input: {
                n: 3, k: 1,
            },
            output: '123',
        },
        {
            input: {
                n: 3, k: 3,
            },
            output: '213',
        },
        {
            input: {
                n: 4, k: 9,
            },
            output: '2314',
        },
        {
            input: {
                n : 3, k: 1,
            },
            output: '123',
        },
    ];

    params.forEach(({input, output}) => {
        const { n, k } = input;

        const result = getPermutation(n, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();
