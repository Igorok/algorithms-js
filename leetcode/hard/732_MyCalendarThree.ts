
class MyCalendarThree_0 {
    starts: Map<number, number> = new Map();
    ends: Map<number, number> = new Map();
    res: number = 0;
    min: number = Number.MAX_SAFE_INTEGER;
    max: number = Number.MIN_SAFE_INTEGER;

    constructor() {
        this.starts = new Map();
        this.ends = new Map();
        this.res = 0;
    }

    book(startTime: number, endTime: number): number {
        this.min = Math.min(this.min, startTime);
        this.max = Math.max(this.max, endTime);

        let cnt: number = this.starts.get(startTime) || 0;
        this.starts.set(startTime, cnt + 1);

        cnt = this.ends.get(endTime) || 0;
        this.ends.set(endTime, cnt + 1);

        let res: number = 0;
        let open: number = 0;

        for (let i: number = this.min; i < this.max; ++i) {
            open += this.starts.get(i) || 0;
            open -= this.ends.get(i) || 0;

            res = Math.max(res, open);
        }

        this.res = Math.max(this.res, res);

        return this.res;
    }
}


class MyCalendarThree {
    starts: number[] = [];
    ends: number[] = [];
    max: number = 0;

    constructor() {
        this.starts = [];
        this.ends = [];
    }

    private getClosed (num: number) {
        let start: number = 0;
        let end: number = this.ends.length - 1;
        let res: number = -1;

        while (start <= end) {
            const middle: number = Math.floor((start + end) / 2);
            if (this.ends[middle] <= num) {
                res = middle;
                start = middle + 1;
            } else {
                end = middle - 1;
            }
        }

        return res;
    }

    book(startTime: number, endTime: number): number {
        this.starts.push(startTime);
        this.ends.push(endTime);
        this.starts.sort((a, b) => a - b);
        this.ends.sort((a, b) => a - b);


        for (let i: number = 0; i < this.starts.length; ++i) {
            let open: number = i+1;
            let closed: number = this.getClosed(this.starts[i]);
            closed = (closed === -1) ? 0 : closed + 1;

            this.max = Math.max(this.max, open - closed);
        }

        return this.max;
    }
}

/*

book: [[10, 20], [50, 60], [10, 40], [25, 55]]








[[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]} output
[1,1,2,2,3,3,3,3,4,4]
[1,1,1,1,1,2,3,3,3,3]


0 - - - - - - - - - 10
0 - 2
0 - - 3
- 1 - 3
- 1 - - 4
- - 2 - - - 6
- - 2 - - - - 7
- - - 3 - - 6
- - - - - - - - 9 - 10


*/

const test = () => {
    const params = [
        {
            input: {
                book: [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
            },
            output: [1, 1, 2, 3, 3, 3],
        },
        {
            input: {
                book: [[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]
            },
            output: [1,1,2,2,3,3,3,3,4,4],
        },

        {
            input: {
                book: [[10, 20], [50, 60], [10, 51], [25, 55]]
            },
            output: [1, 1, 2, 3],
        },
    ];

    params.forEach(({input, output}) => {
        const calendar = new MyCalendarThree();
        const result = input.book.map(([s, e]) => calendar.book(s, e));

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();
