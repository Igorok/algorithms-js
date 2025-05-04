function maxTaskAssign(tasks: number[], workers: number[], pills: number, strength: number): number {
    let n = tasks.length;
    let m = workers.length;
    tasks.sort((a, b) => a - b);
    workers.sort((a, b) => a - b);


    const check = (mid: number): boolean => {
        let p: number = pills;
        let wQueue: number[] = new Array();
        let wId: number = m - 1;

        for (let i = mid - 1; i >= 0; --i) {
            while (wId >= workers.length - mid && workers[wId] + strength >= tasks[i]) {
                wQueue.unshift(workers[wId]);
                wId -= 1;
            }
            if (wQueue.length === 0) {
                return false;
            } else if (wQueue.at(-1) >= tasks[i]) {
                wQueue.pop();
            } else {
                if (!p) {
                    return false;
                }
                p -= 1;
                wQueue.shift();
            }
        }

        return true;
    };

    let left: number = 1
    let right: number = Math.min(m, n);
    let res: number = 0;
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (check(mid)) {
            res = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return res;
};

/*

2 4 6 7 8 9 10; 1 3
1 3 6 9

*/

const test = () => {
    const params = [
        {
            input: { tasks: [10,10,10], workers: [7,7,10], pills: 1, strength: 3 },
            output: 2,
        },
        {
            input: { tasks: [3,2,1], workers: [0,3,3], pills: 1, strength: 1 },
            output: 3,
        },
        {
            input: { tasks: [5,4], workers: [0,0,0], pills: 1, strength: 5 },
            output: 1,
        },
        {
            input: { tasks: [10,15,30], workers: [0,10,10,10,10], pills: 3, strength: 10 },
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const { tasks, workers, pills, strength } = input;

        const result = maxTaskAssign(tasks, workers, pills, strength);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();