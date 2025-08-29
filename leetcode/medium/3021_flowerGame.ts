function flowerGame_0(n: number, m: number): number {
    const total: number = n + m;
    if (total < 3) return 0;

    let res: number = 0;
    const [min, max] = [n, m].sort((a, b) => a - b);

    for (let i: number = 3; i <= total; i += 2) {
        let localMax: number = Math.min(max, i-1);
        let localMin: number = i - localMax;

        const comb: number = 1 + Math.min(min, localMax) - localMin;

        res += comb;
    }


    return res;
};


const flowerGame = (n: number, m: number): number => Math.floor(n*m/2);

/*

A
1 2 3
1 2
B

A 1, B 2, A 2, B 1, A 3.

---

A
1 2 3 4
B

---

3

1 1
1

1
1 1

---

5

1 1 1 1
1

1 1 1
1 1

1 1
1 1 1

1
1 1 1 1

---

2 + 3 = 5

1 1
1


---

*/

const test = () => {
    const params = [
        {
            input: {
                n: 4, m: 4,
            },
            output: 8,
        },
        {
            input: {
                n: 3, m: 2,
            },
            output: 3,
        },
        {
            input: {
                n: 1, m: 1,
            },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { n, m } = input;
        const result = flowerGame(n, m);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();