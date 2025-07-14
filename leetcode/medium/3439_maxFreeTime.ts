function maxFreeTime(eventTime: number, k: number, startTime: number[], endTime: number[]): number {
    let res: number = 0;

    let left: number = 0;
    let count: number = startTime[0] - 0;

    for (let right: number = 0; right < startTime.length; ++right) {
        const nextStart: number = right + 1 === startTime.length ? eventTime : startTime[right+ 1];
        count += nextStart - endTime[right]

        while (right - left >= k) {
            const prevEnd: number = left > 0 ? endTime[left - 1] : 0;
            count -= startTime[left] - prevEnd;
            left += 1;
        }

        res = Math.max(res, count);
    }


    return res;
};


/*

eventTime: 10, k: 2, startTime: [1,3,7], endTime: [2,5,8],

0 1 2 3 4 5 6 7 8 9 10
  1-1 1  -1   1-1
  1 0  -1         1 -1


[1,2], [3,5], [7,8]
[0,1], [5,7], [7,8]
[1,2], [2,4], [9,10]

*/


const test = () => {
    const params = [
        {
            input: {
                eventTime: 5, k: 1, startTime: [1,3], endTime: [2,5],
            },
            output: 2,
        },
        {
            input: {
                eventTime: 10, k: 1, startTime: [0,2,9], endTime: [1,4,10],
            },
            output: 6,
        },
        {
            input: {
                eventTime: 5, k: 2, startTime: [0,1,2,3,4], endTime: [1,2,3,4,5],
            },
            output: 0,
        },
        {
            input: {
                eventTime: 10, k: 2, startTime: [1,3,7], endTime: [2,5,8],
            },
            output: 5,
        },
        {
            input: {
                eventTime: 34, k: 2, startTime: [0,17], endTime: [14,19],
            },
            output: 18,
        },
    ];

    params.forEach(({input, output}) => {
        const { eventTime, k, startTime, endTime } = input;
        const result = maxFreeTime(eventTime, k, startTime, endTime);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

