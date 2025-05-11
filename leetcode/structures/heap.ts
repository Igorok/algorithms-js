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



const test = (): void => {
    const data: number[] = [];
    for (let i: number = 0; i < 1000; ++i) {
        data.push(Math.floor(Math.random() * 1000));
    }
    const sorted: number[] = [...data].sort((a: number, b: number) => a - b);

    const heap: MinHeap = new MinHeap(1000);
    for (let i: number = 0; i < data.length; ++i) {
        heap.push([data[i]]);
    }
    for (let i: number = 0; i < data.length; ++i) {
        const num: number[] = heap.pop() as number[];
        if (num[0] !== sorted[i]) {
            console.log('ERROR', i, num, sorted[i]);
            return;
        }
    }

    for (let i: number = 0; i < 1000; ++i) {
        const num: number[] = heap.pop();
        if (num[0] !== sorted[i]) {
            console.log('ERROR', i, num, sorted[i]);
            return
        }
    }

    if (!heap.isEmpty()) {
        console.log('ERROR', 'heap is not empty', heap);
        return;
    }

};