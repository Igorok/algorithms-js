
function reconstructQueue_0(people: number[][]): number[][] {
    const res: number[][] = [];

    const insert = (p: number[]) => {
        res.push(p);

        let less: number = 0;
        for (let i: number = res.length - 1; i > 0; --i) {
            if (res[i][0] > res[i-1][0]) {
                const tmp = res[i-1];
                res[i-1] = res[i];
                res[i] = tmp;
                continue;
            }

            if (less < res[i][1]) {
                if (res[i-1][0] >= res[i][0]) {
                    less += 1;
                }
                const tmp = res[i-1];
                res[i-1] = res[i];
                res[i] = tmp;
                continue;
            }

            break;
        }
    };

    people.sort((a, b) => {
        if (a[1] === b[1]) {
            return a[0] - b[0];
        }

        return a[1] - b[1];
    });

    for (const p of people) {
        insert(p);
    }

    return res.reverse();
};


function reconstructQueue(people: number[][]): number[][] {
    let res: number[][] = [];

    people.sort((a, b) => {
        if (a[0] === b[0]) {
            return a[1] - b[1];
        }

        return b[0] - a[0];
    });

    for (const p of people) {
        if (p[1] === 0) {
            res.unshift(p);
            continue;
        }
        res = [
            ...res.slice(0, p[1]),
            p,
            ...res.slice(p[1]),
        ]
    }

    return res;
};

/*

[[5,0],[7,0],[6,1],[7,1],[5,2],[4,4]]

[5,0]
[7,0]
[7,1]
[5,2]


[6,1]
[4,4]




*/

const test = () => {
    const params = [
        {
            input: {
                people: [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]],
            },
            output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]],
        },
        {
            input: {
                people: [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]],
            },
            output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]],
        },
    ];

    params.forEach(({input, output}) => {
        const { people } = input;
        const result = reconstructQueue(people);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();