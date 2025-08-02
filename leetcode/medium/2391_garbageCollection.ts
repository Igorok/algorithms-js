function garbageCollection(garbage: string[], travel: number[]): number {
    let res: number = 0;

    const totalPath: number[] = new Array(garbage.length).fill(0);
    const truckPath = {
        P: 0,
        G: 0,
        M: 0,
    };


    for (let i: number = 0; i < garbage.length; ++i) {
        if (i > 0) {
            totalPath[i] = travel[i-1] + totalPath[i-1];
        }
        res += garbage[i].length;

        const unique: Set<string> = new Set(garbage[i]);
        unique.forEach((truck: string) => {
            const p: number = totalPath[i] - truckPath[truck];
            truckPath[truck] = totalPath[i];
            res += p;
        });
    }

    return res;
};

/*

garbage: ["G","P","GP","GG"],
travel: [2,4,3]

G
0+1 + 2 + 4+1 + 3+1
0+2+4+3+1
???
0+1+2+4+1+3+2 = 13


P
0+2+1+4+1
---
0+1 + 2 + 4+1 + 3+1 + 0+2+4+3+1+0+2+1+4+1


--



*/

const test = () => {
    const params = [
        {
            input: {
                garbage: ["G","P","GP","GG"],
                travel: [2,4,3]
            },
            output: 21,
        },
        {
            input: {
                garbage: ["MMM","PGM","GP"],
                travel: [3,10],
            },
            output: 37,
        },
    ];

    params.forEach(({input, output}) => {
        const { garbage, travel } = input;

        const result = garbageCollection(garbage, travel);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();