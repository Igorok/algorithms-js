function subarrayBitwiseORs(arr: number[]): number {
    const visited: Set<number> = new Set();
    let prev: Set<number> = new Set();

    for (let i = 0; i < arr.length; ++i) {
        let curr: Set<number> = new Set();
        curr.add(arr[i]);

        prev.forEach((val: number) => {
            curr.add(arr[i] | val);
        });

        curr.forEach((val: number) => {
            visited.add(val);
        });

        prev = curr;
    }

    return visited.size;
};

/*

1,2,4
001
010
100

-
001

010 2-2
011 1-2

100 3
110 2-3
111 1-3

*/

const test = () => {
    const params = [
        {
            input: {
                arr: [1,2,4],
            },
            output: 6,
        },
        {
            input: {
                arr: [31,86,44,78,66,71,44],
            },
            output: 12,
        },
        {
            input: {
                arr: [0],
            },
            output: 1,
        },
        {
            input: {
                arr: [1,1,2],
            },
            output: 3,
        },

    ];

    params.forEach(({ input, output }) => {
        const { arr } = input;
        const result = subarrayBitwiseORs(arr);

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
