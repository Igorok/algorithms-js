function numOfUnplacedFruits(fruits: number[], baskets: number[]): number {
    let res: number = 0;

    for (let i: number = 0; i < fruits.length; ++i) {
        let found: number = 1;

        for (let j: number = 0; j < baskets.length; ++j) {
            if (baskets[j] >= fruits[i]) {
                baskets[j] = -1;
                found = 0;
                break;
            }
        }

        res += found;
    }


    return res;
};

const test = () => {
    const params = [
        {
            input: {
                fruits: [4,2,5], baskets: [3,5,4],
            },
            output: 1,
        },
        {
            input: {
                fruits: [3,6,1], baskets: [6,4,7],
            },
            output: 0,
        },
    ];

    params.forEach(({ input, output }) => {
        const { fruits, baskets } = input;
        const result = numOfUnplacedFruits(fruits, baskets);

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
