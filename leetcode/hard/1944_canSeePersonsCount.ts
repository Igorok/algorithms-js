function canSeePersonsCount(heights: number[]): number[] {
    const res: number[] = new Array(heights.length).fill(0);

    const stack: number[] = [heights.at(-1)];

    for (let i: number = heights.length - 2; i > -1; --i) {
        while (stack.length && stack.at(-1) <= heights[i]) {
            res[i] += 1;
            stack.pop();
        }
        if (stack.length) {
            res[i] += 1;
        }
        stack.push(heights[i]);
    }


    return res;
};

const test = () => {
    const params = [
        {
            input: {
                heights: [10,6,8,5,11,9],
            },
            output: [3,1,2,1,1,0],
        },
        {
            input: {
                heights: [5,1,2,3,10]
            },
            output: [4,1,1,1,0],
        },
    ];

    params.forEach(({ input, output }) => {
        const { heights } = input;
        const result = canSeePersonsCount(heights);

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
