function maxFreeTime_0(eventTime: number, startTime: number[], endTime: number[]): number {
    let res: number = 0;
    const gaps: number[] = [];

    if (startTime[0] > 0) {
        gaps.push(startTime[0]);
    }
    if ((endTime.at(-1) || 0) < eventTime) {
        gaps.push(eventTime - (endTime.at(-1) || 0));
    }

    for (let i: number = 1; i < startTime.length; ++i) {
        const gap: number = startTime[i] - endTime[i-1];
        if (gap === 0) {
            continue;
        }

        gaps.push(gap);
    }
    gaps.sort((a, b) => a - b);


    for (let i: number = 0; i < startTime.length; ++i) {
        const leftGap: number = (i === 0)
            ? startTime[0]
            : startTime[i] - endTime[i-1];
        const rightGap: number = (i === startTime.length - 1)
            ? eventTime - endTime[i]
            : startTime[i+1] - endTime[i];

        const size: number = endTime[i] - startTime[i];

        res = Math.max(res, leftGap + rightGap);

        let id: number = -1;
        let left: number = 0;
        let right: number = gaps.length - 1;

        while (left <= right) {
            const middle: number = Math.floor((left + right) / 2);
            if (gaps[middle] < size) {
                left = middle + 1;
            } else {
                id = middle;
                right = middle - 1;
            }
        }
        if (id === -1) {
            continue;
        }

        [leftGap, rightGap].sort((a, b) => a - b).forEach((gap) => {
            if (id < gaps.length && gap === gaps[id]) {
                id += 1;
            }
        });
        if (id === gaps.length) {
            continue;
        }

        res = Math.max(leftGap + rightGap + size, res);

    }


    return res;
};


function maxFreeTime(eventTime: number, startTime: number[], endTime: number[]): number {
    let res: number = 0;
    let gaps: number[] = [];

    if (startTime[0] > 0) {
        gaps.push(startTime[0]);
    }
    if ((endTime.at(-1) || 0) < eventTime) {
        gaps.push(eventTime - (endTime.at(-1) || 0));
    }

    for (let i: number = 1; i < startTime.length; ++i) {
        const gap: number = startTime[i] - endTime[i-1];
        if (gap === 0) {
            continue;
        }

        gaps.push(gap);
    }
    gaps.sort((a, b) => a - b);


    for (let i: number = 0; i < startTime.length; ++i) {
        const leftGap: number = (i === 0)
            ? startTime[0]
            : startTime[i] - endTime[i-1];
        const rightGap: number = (i === startTime.length - 1)
            ? eventTime - endTime[i]
            : startTime[i+1] - endTime[i];

        const size: number = endTime[i] - startTime[i];

        res = Math.max(res, leftGap + rightGap);

        let id: number = gaps.length - 1;
        [leftGap, rightGap]
            .sort((a, b) => b-a)
            .forEach((gap) => {
                if (id > -1 && gaps[id] === gap) {
                    id -= 1;
                }
            });

        if (id === -1 || gaps[id] < size) {
            continue;
        }

        res = Math.max(leftGap + rightGap + size, res);

    }


    return res;
};


/*


0 2-4 4-6 6-9 9-16 18-20 20

2 2

*/

const test = () => {
    const params = [
        {
            input: {
                eventTime: 10, startTime: [0,7,9], endTime: [1,8,10],
            },
            output: 7,
        },
        {
            input: {
                eventTime: 20, startTime: [2,4,6,9,18], endTime: [4,6,9,16,20],
            },
            output: 4,
        },
        {
            input: {
                eventTime: 21, startTime: [7,10,16], endTime: [10,14,18],
            },
            output: 10,
        },
        {
            input: {
                eventTime: 41, startTime: [17,24], endTime: [19,25],
            },
            output: 24,
        },




        {
            input: {
                eventTime: 10, startTime: [0,7,9], endTime: [1,8,10],
            },
            output: 7,
        },

        {
            input: {
                eventTime: 10, startTime: [0,3,7,9], endTime: [1,4,8,10],
            },
            output: 6,
        },
        {
            input: {
                eventTime: 5, startTime: [1,3], endTime: [2,5],
            },
            output: 2,
        },
        {
            input: {
                eventTime: 5, startTime: [0,1,2,3,4], endTime: [1,2,3,4,5],
            },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { eventTime, startTime, endTime } = input;
        const result = maxFreeTime(eventTime, startTime, endTime);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

