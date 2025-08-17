function nthUglyNumber_0(n: number): number {
    const multipliers = [2, 3, 5]
    const unique: Set<number> = new Set([1]);
    const arr: number[] = [1];

    let i: number = 1;

    while (i <= n) {
        if (i === n) {
            return arr[i-1];
        }

        for (const num of multipliers) {
            const m = num * arr[i-1];
            if (unique.has(m)) {
                continue;
            }

            unique.add(m);
            arr.push(m);
        }

        arr.sort((a, b) => a - b);
        i += 1;
    }


    return arr[n];
};


function nthUglyNumber(n: number): number {
    let i: number = 1;
    let id2: number = 0;
    let id3: number = 0;
    let id5: number = 0;

    const arr2: number[] = [1];
    const arr3: number[] = [1];
    const arr5: number[] = [1];

    while (i <= n) {
        const val: number = Math.min(arr2[id2], arr3[id3], arr5[id5]);
        if (i === n) {
            return val;
        }

        arr2.push(val * 2);
        arr3.push(val * 3);
        arr5.push(val * 5);

        while (arr2[id2] === val) {
            id2 += 1;
        }
        while (arr3[id3] === val) {
            id3 += 1;
        }
        while (arr5[id5] === val) {
            id5 += 1;
        }

        i += 1;
    }


    return 0;
};

/*

2 1*2=2; 2*2=4;  3*2=6;   4*2=8;  5*2=10
3 1*3=3; 2*3=6;  3*3=9;   4*3=12; 5*3=15;
5 1*5=5; 2*5=10; 3*15=15; 4*5=20; 5*4=20;


*/

const test = () => {
    const params = [
        {
            input: {
                n: 10,
            },
            output: 12,
        },
        {
            input: {
                n: 1,
            },
            output: 1,
        },
    ];

    params.forEach(({ input, output }) => {
        const { n } = input;
        const result = nthUglyNumber(n);

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
