function findRestaurant(list1: string[], list2: string[]): string[] {
    const idByName: Map<string, number[]> = new Map();
    for (let i: number = 0; i < list1.length; ++i) {
        idByName.set(list1[i], [i, 1]);
    }

    let minSum: number = Number.MAX_SAFE_INTEGER;
    for (let i: number = 0; i < list2.length; ++i) {
        if (!idByName.has(list2[i])) {
            continue;
        }
        const l1: number[] = idByName.get(list2[i]) || [1000, 1000];
        l1[0] += i;
        l1[1] += 1;
        idByName.set(list2[i], l1);
        minSum = Math.min(minSum, l1[0]);
    }

    let res: string[] = [];
    idByName.forEach((value: number[], key: string) => {
        if (value[0] === minSum && value[1] === 2) {
            res.push(key);
        }
    });

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                list1: ["Shogun","Tapioca Express","Burger King","KFC"],
                list2: ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"],
            },
            output: ["Shogun"],
        },
        {
            input: {
                list1: ["Shogun","Tapioca Express","Burger King","KFC"],
                list2: ["KFC","Shogun","Burger King"]
            },
            output: ["Shogun"],
        },
        {
            input: {
                list1: ["happy","sad","good"],
                list2: ["sad","happy","good"]
            },
            output: ["sad","happy"],
        },
    ];

    params.forEach(({input, output}) => {
        const { list1, list2 } = input;
        const result = findRestaurant(list1, list2);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();