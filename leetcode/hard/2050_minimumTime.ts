function minimumTime(n: number, relations: number[][], time: number[]): number {
    const parents: number[][] = new Array(n + 1).fill(0).map(() => []);
    const childrenCount: number[] = new Array(n + 1).fill(0);
    const timesForNode: number[] = new Array(n + 1).fill(0);

    for (const [s, e] of relations) {
        parents[s].push(e);
        childrenCount[e] += 1;
    }

    const queue: number[] = [];

    for (let s: number = 1; s < parents.length; ++s) {
        if (childrenCount[s] === 0) {
            queue.push(s);
        }
    }

    let res: number = 0;

    while (queue.length !== 0) {
        const start = queue.shift();
        const startTime = timesForNode[start] + time[start - 1];

        res = Math.max(res, startTime);

        for (const parent of parents[start]) {
            timesForNode[parent] = Math.max(timesForNode[parent], startTime);
            childrenCount[parent] -= 1;
            if (childrenCount[parent] === 0) {
                queue.push(parent)
            }
        }
    }

    return res;
};


/*

1------\
2-------5
3----/-/
3--4--/

*/

const test = () => {
    const params = [
        {
            input: {
                n: 3, relations: [[1,3],[2,3]], time: [3,2,5],
            },
            output: 8,
        },
        {
            input: {
                n: 5, relations: [[1,5],[2,5],[3,5],[3,4],[4,5]], time: [1,2,3,4,5]
            },
            output: 12,
        },
    ];

    params.forEach(({input, output}) => {
        const { n, relations, time } = input;
        const result = minimumTime(n, relations, time);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

