class SegmentTree {
    nums: number[];
    sums: number[];

    constructor (nums: number[]) {
        this.nums = nums;

        const height: number = this.getArrHeight(this.nums.length);
        this.sums = new Array(height).fill(0);

        this.constructTree(0, this.nums.length - 1, 0);
    }

    private getArrHeight (length: number) {
        const height: number = Math.ceil(Math.log2(length));
        return 2 * (2**height) - 1;
    }
    private getLeftChild (id: number) {
        return id * 2 + 1;
    }
    private getRightChild (id: number) {
        return id * 2 + 2;
    }
    private getMiddle (s: number, e: number) {
        return Math.floor((e + s) / 2);
    }
    private constructTree (start: number, end: number, sumId: number) {
        if (start === end) {
            this.sums[sumId] = this.nums[start];
            return this.sums[sumId];
        }

        const middle: number = this.getMiddle(start, end);
        const leftSum: number = this.constructTree(start, middle, this.getLeftChild(sumId));
        const rightSum: number = this.constructTree(middle + 1, end, this.getRightChild(sumId));

        this.sums[sumId] = leftSum + rightSum;
        return this.sums[sumId];
    }
    private update (start: number, end: number, sumId: number, id: number, diff: number) {
        if (id < start || id > end) {
            return;
        }

        this.sums[sumId] += diff;

        if (start === end) {
            return;
        }

        const middle: number = this.getMiddle(start, end);
        const leftChild: number = this.getLeftChild(sumId);
        const rightChild: number = this.getRightChild(sumId);

        this.update(start, middle, leftChild, id, diff);
        this.update(middle + 1, end, rightChild, id, diff);
    }
    private getSum (start: number, end: number, sumId: number, queryStart: number, queryEnd: number): number {
        if (start >= queryStart && end <= queryEnd) {
            return this.sums[sumId];
        }

        if (start > queryEnd || end < queryStart) {
            return 0;
        }

        const middle: number = this.getMiddle(start, end);
        const leftChild: number = this.getLeftChild(sumId);
        const rightChild: number = this.getRightChild(sumId);

        const leftSum: number = this.getSum(start, middle, leftChild, queryStart, queryEnd);
        const rightSum: number = this.getSum(middle + 1, end, rightChild, queryStart, queryEnd);

        return leftSum + rightSum;
    }

    public updateIndex (id: number, val: number): null {
        if (id < 0 || id >= this.nums.length) {
            return null;
        }

        const diff: number = val - this.nums[id];
        this.nums[id] = val;

        this.update(0, this.nums.length - 1, 0, id, diff);

        return null;
    }

    public getSumOfRange (start: number, end: number): number {
        if (start < 0 || end >= this.nums.length || start > end) {
            return -1;
        }

        return this.getSum(0, this.nums.length - 1, 0, start, end);
    }
}

class NumArray {
    sTree: SegmentTree;

    constructor(nums: number[]) {
        this.sTree = new SegmentTree(nums);
    }

    update(index: number, val: number): void {
        this.sTree.updateIndex(index, val);
    }

    sumRange(left: number, right: number): number {
        return this.sTree.getSumOfRange(left, right);
    }
}



const test = () => {
    const params = [
        {
            input: [
                ["NumArray", "sumRange", "update", "sumRange"],
                [[1, 3, 5], [0, 2], [1, 2], [0, 2]]
            ],
            output: [null, 9, null, 8],
        },
        {
            input: [
                ["NumArray","sumRange","update","sumRange"],
                [[-1],[0,0],[0,1],[0,0]]
            ],
            output: [null, 9, null, 8],
        },
    ];

    params.forEach(({ input, output }) => {
        const arr: number[] = input[1][0] as number[];
        const na = new NumArray(arr);

        for (let i: number = 1; i < input[0].length; ++i) {
            const p: number[] = input[1][i] as number[];
            let result: number|null = null;

            if (input[0][i] === 'sumRange') {
                result = na.sumRange(p[0], p[1]);
            } else {
                na.update(p[0], p[1]);
            }

            console.log(
                result === output[i] ? 'SUCCESS ' : 'ERROR ',
                'input', JSON.stringify([input[0][i], input[1][i]]),
                'output', output[i],
                'result', result,
            );
        }
    });
};

test();