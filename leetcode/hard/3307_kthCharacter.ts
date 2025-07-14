function kthCharacter_0(k: number, operations: number[]): string {
    let codes: number[] = [0];

    let op: number = 0;
    while (codes.length <= k) {
        if (operations[op] === 0) {
            codes = [...codes, ...codes];
        } else {
            const end: number = codes.length;
            for (let i: number = 0; i < end; ++i) {
                codes.push((codes[i] + 1) % 26);
            }
        }

        if (codes.length >= k) {
            return String.fromCharCode(97 + codes[k-1]);
        }

        op += 1;
    }

    return 'a';
};

function kthCharacter(k: number, operations: number[]): string {
    let count: number = 0;

    while (k > 1) {
        let degree: number = Math.ceil(Math.log2(k));
        count += operations[degree - 1];
        let prevDegree: number = degree - 1;
        let prevLength: number = 2**prevDegree;
        k = k - prevLength;
    }

    count %= 26;

    console.log('count', count);


    return String.fromCharCode(97 + count);
};

/*
k: 10, operations: [0,1,0,1]
- a
0 aa
1 aabb
0 aabbaabb
1 aabbaabb bbccbbcc



*/

const test = () => {
    const params = [
        {
            input: {
                k: 5, operations: [0,0,0],
            },
            output: 'a',
        },
        {
            input: {
                k: 10, operations: [0,1,0,1]
            },
            output: 'b',
        },
        {
            input: {
                k: 28172699, operations: [0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,1,1,0,0,1,1,1,0,1],
            },
            output: 'f',
        },
    ];

    params.forEach(({ input, output }) => {
        const { k, operations } = input;
        const result = kthCharacter(k, operations);

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
