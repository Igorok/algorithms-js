function maxValue(events: number[][], k: number): number {
    events.sort((a, b) => {
        if (a[0] === b[0]) return a[1] - b[1];
        return a[0] - b[0];
    });

    const memo: number[][] = new Array(events.length).fill(0).map(() => new Array(k).fill(-1));

    const getMaxSum = (id: number, count: number) => {
        if (id >= events.length || count === k) {
            return 0;
        }
        if (memo[id][count] !== -1) {
            return memo[id][count];
        }

        let sum: number = getMaxSum(id + 1, count);
        memo[id][count] = Math.max(memo[id][count], sum);

        sum = events[id][2];

        let left: number = id + 1;
        let right: number = events.length - 1;
        let res: number = -1;
        while (left <= right) {
            const middle: number = Math.floor((left + right) / 2);
            if (events[middle][0] > events[id][1]) {
                res = middle;
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }

        if (res !== -1) {
            sum += getMaxSum(res, count + 1);
        }

        memo[id][count] = Math.max(memo[id][count], sum);

        return memo[id][count];
    };

    let res: number = 0;

    for (let i: number = 0; i < events.length; ++i) {
        const r: number = getMaxSum(i, 0);
        res = Math.max(res, r);
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                events: [[1,2,4],[3,4,3],[2,3,1]], k: 2
            },
            output: 7,
        },
        {
            input: {
                events: [[1,2,4],[3,4,3],[2,3,10]], k: 2
            },
            output: 10,
        },
        {
            input: {
                events: [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k: 3
            },
            output: 9,
        },
    ];

    params.forEach(({input, output}) => {
        const { events, k } = input;
        const result = maxValue(events, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

