class BIT {
    private sums: number[];

    constructor (arr: number[]) {
        this.sums = new Array(arr.length + 1).fill(0);

        for (let i: number = 0; i < arr.length; ++i) {
            this.update(i, arr[i]);
        }
    }

    public update (id: number, diff: number): void {
        let i: number = id + 1;
        while (i < this.sums.length) {
            this.sums[i] += diff;
            i += (i & (-i));
        }
    }

    private query (end: number): number {
        let sum: number = 0;

        while (end > 0) {
            sum += this.sums[end];
            end -= (end & (-end));
        }

        return sum;
    }

    public getSum (start: number, end: number): number {
        return this.query(end + 1) - this.query(start + 1);
    }
}

function countSmaller(nums: number[]): number[] {
    const maxVal: number = 1 + 10e3;
    const res: number[] = new Array(nums.length).fill(0);
    const bit: BIT = new BIT(new Array(maxVal * 2).fill(0));
    const arr: number[] = nums.map((num: number) => num + maxVal);

    for (let i: number = nums.length - 1; i > -1; --i) {
        bit.update(arr[i], 1);
        const s: number = bit.getSum(0, arr[i] - 1);

        res[i] = s;
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [5,2,6,1],
            output: [2,1,1,0],
        },
        {
            input: [-1],
            output: [0],
        },
        {
            input: [-1,-1],
            output: [0, 0],
        },
    ];

    params.forEach(({input, output}) => {
        const result = countSmaller(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();