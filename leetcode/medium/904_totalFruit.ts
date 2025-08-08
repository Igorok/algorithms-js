function totalFruit(fruits: number[]): number {
    const countByType: Map<number, number> = new Map();
    let count: number = 0;
    let res: number = 0;
    let left: number = 0;

    for (let right: number = 0; right < fruits.length; ++right) {
        count += 1;
        const rType: number = fruits[right];
        const cnt: number = (countByType.get(rType) || 0) + 1;
        countByType.set(rType, cnt);

        while (countByType.size > 2) {
            const lType: number = fruits[left];
            const cnt: number = (countByType.get(lType) || 0) - 1;
            if (cnt === 0) {
                countByType.delete(lType);
            } else {
                countByType.set(lType, cnt);
            }
            count -= 1;
            left += 1;
        }

        res = Math.max(res, count);
    }


    return res;
};

const test = () => {
    const params = [
        {
            input: {
                fruits: [1,2,1],
            },
            output: 3,
        },
        {
            input: {
                fruits: [0,1,2,2],
            },
            output: 3,
        },
        {
            input: {
                fruits: [1,2,3,2,2],
            },
            output: 4,
        },
    ];

    params.forEach(({ input, output }) => {
        const { fruits } = input;
        const result = totalFruit(fruits);

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
