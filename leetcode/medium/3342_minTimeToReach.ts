class MinHeap {
    arr: unknown[] = [];

    constructor() {
        this.arr = [];
    }
    private getLeftChildIndex(index: number): number {
        return index * 2 + 1;
    }
    private getRightChildIndex(index: number): number {
        return index * 2 + 2;
    }
    private getParentIndex(index: number): number {
        return Math.floor((index - 1) / 2);
    }
    public isEmpty(): boolean {
        return this.arr.length === 0;
    }
    public push(val: unknown[]): void {
        this.arr.push(val);
        let index: number = this.arr.length - 1;
        while (index > 0 && this.arr[this.getParentIndex(index)][0] > this.arr[index][0]) {
            const tmp: unknown[] = this.arr[this.getParentIndex(index)] as unknown[];
            this.arr[this.getParentIndex(index)] = this.arr[index];
            this.arr[index] = tmp;
            index = this.getParentIndex(index);
        }
    }
    public pop(): unknown[] | undefined {
        const val: unknown[] = this.arr[0] as unknown[];
        const last: unknown[] = this.arr.pop() as unknown[];
        if (this.arr.length !== 0) {
            this.arr[0] = last;
        }

        let index: number = 0;
        let lId: number = this.getLeftChildIndex(index);
        let rId: number = this.getRightChildIndex(index);
        while (
            (this.arr[lId] !== undefined && this.arr[index][0] > this.arr[lId][0]) ||
            (this.arr[rId] !== undefined && this.arr[index][0] > this.arr[rId][0])
        ) {
            let minIndex: number = lId;
            if (this.arr[rId] && this.arr[rId] < this.arr[lId]) {
                minIndex = rId;
            }

            const tmp: unknown[] = this.arr[index] as unknown[];
            this.arr[index] = this.arr[minIndex];
            this.arr[minIndex] = tmp;
            index = minIndex;
            lId = this.getLeftChildIndex(index);
            rId = this.getRightChildIndex(index);
        }

        return val;
    }
}

function minTimeToReach(moveTime: number[][]): number {
    const shifts: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const n: number = moveTime.length;
    const m: number = moveTime[0].length;
    const minTime: number[][] = new Array(n).fill(0).map(() => new Array(m).fill(-1));
    minTime[0][0] = 0;
    minTime[1][0] = moveTime[1][0] + 1;
    minTime[0][1] = moveTime[0][1] + 1;

    const minHeap: MinHeap = new MinHeap();
    const vBottom: number[] = [ moveTime[1][0] + 1, 1, 0, 1 ];
    const vRight: number[] = [ moveTime[0][1] + 1, 0, 1, 1 ]
    minHeap.push(vBottom);
    minHeap.push(vRight);

    while (!minHeap.isEmpty()) {
        const [time, y, x, price] = minHeap.pop() as number[];

        for (const [dy, dx] of shifts) {
            const ny: number = y + dy;
            const nx: number = x + dx;
            if (ny < 0 || ny === n || nx < 0 || nx === m) {
                continue;
            }
            const nPrice: number = price === 1 ? 2 : 1;
            const nVal: number = Math.max(time, moveTime[ny][nx]) + nPrice;
            if (minTime[ny][nx] === -1 || minTime[ny][nx] > nVal) {
                minTime[ny][nx] = nVal;
                if (ny === n - 1 && nx === m - 1) {
                    continue;
                }
                minHeap.push([nVal, ny, nx, nPrice]);
            }
        }
    }

    return minTime.at(-1).at(-1);
};

/*

[0,0,0,0],
[0,0,0,0]

*/

const test = () => {
    const params = [
        // {
        //     input: { moveTime: [[0,4],[4,4]] },
        //     output: 7,
        // },
        // {
        //     input: { moveTime: [[0,0,0,0],[0,0,0,0]] },
        //     output: 6,
        // },
        // {
        //     input: { moveTime: [[29,42],[51,59]] },
        //     output: 61,
        // },
        {
            input: { moveTime: [[1,0,89],[86,61,11]] },
            output: 61,
        },


    ];

    params.forEach(({input, output}) => {
        const { moveTime } = input;

        const result = minTimeToReach(moveTime);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();