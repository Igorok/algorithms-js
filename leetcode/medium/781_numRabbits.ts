function numRabbits(answers: number[]): number {
    const answByCount: Map<number, number> = new Map();
    for (const num of answers) {
        answByCount.set(num + 1, (answByCount.get(num + 1) || 0) + 1);
    }

    let res: number = 0;

    answByCount.forEach((count: number, num: number) => {
        const groups: number = Math.ceil(count / num);
        res += groups * num;
    });


    return res;
};

/*

[1,1,2]
5

2: 2
3: 1

---

[10,10,10]
11

11: 3

---

[1, 1, 1, 1, 1, 0]
7? 4

2: 5, // 2 2 1
1: 1


*/

const test = () => {
    const params = [
        {
            input: [1,1,2],
            output: 5,
        },
        {
            input: [10,10,10],
            output: 11,
        },
        {
            input: [1, 1, 1, 1, 1, 0],
            output: 7,
        },
    ];

    params.forEach(({input, output}) => {
        const result = numRabbits(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();