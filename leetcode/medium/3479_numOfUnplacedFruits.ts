class BasketsTree {
    arr: number[] = [];
    baskets: number[] = [];

    constructor (baskets: number[]) {
        const height = Math.ceil(Math.log2(baskets.length));
        const size: number = 2 * 2**height;

        this.baskets = baskets;
        this.arr = new Array(size).fill(-1);

        this.fillMax(0, 0, baskets.length - 1);
    }

    private fillMax (id: number, left: number, right: number) {
        if (left === right) {
            this.arr[id] = this.baskets[left];
            return this.arr[id];
        }

        const middle: number = Math.floor((left+right) / 2);

        const lId: number = 1 + 2*id;
        const rId: number = 2 + 2*id;

        const l: number = this.fillMax(lId, left, middle);
        const r: number = this.fillMax(rId, middle+1, right);

        this.arr[id] = Math.max(l, r)
        return this.arr[id];
    }

    public checkMax (val: number) {
        const r: number = this.findMaxAndUpdate(0, val);
        return r === 1;
    }

    private findMaxAndUpdate (id: number, val: number) {
        if (this.arr[id] < val) {
            return -1;
        }

        const lId: number = 1 + 2*id;
        const rId: number = 2 + 2*id;

        if (this.arr[lId] >= val) {
            this.findMaxAndUpdate(lId, val);
            this.arr[id] = Math.max(this.arr[lId], this.arr[rId]);
            return 1;
        }
        if (this.arr[rId] >= val) {
            this.findMaxAndUpdate(rId, val);
            this.arr[id] = Math.max(this.arr[lId], this.arr[rId]);
            return 1;
        }

        this.arr[id] = -1;

        return 1;
    }
}


function numOfUnplacedFruits(fruits: number[], baskets: number[]): number {
    const basketsTree: BasketsTree = new BasketsTree(baskets);
    let res: number = 0;

    for (const fruit of fruits) {
        if(!basketsTree.checkMax(fruit)) {
            res += 1;
        }
    }


    return res;
};

/*
1,2,3,4,5,6,7,8,9,10

1,2,3,4,5,   6,7,8,9,10

1,2,3,      4,5,   6,7,8,   9,10

1,2,    3,      4,  5,   6,7,   8,   9, 10

1,  2,    3,      4,  5,   6,   7,   8,   9, 10



19

const d = Math.ceil(Math.log2(10+1));
const s = 2 * 2**d;
console.log(
    'd', d,
    's', s,
);

[0,2]; 2/2=1; [0,0],[1,2]
[1,2]; 3/2=1; [1,0]



*/

const test = () => {
    const params = [
        {
            input: {
                fruits: [4,2,5], baskets: [3,5,4],
            },
            output: 1,
        },
        {
            input: {
                fruits: [3,6,1], baskets: [6,4,7],
            },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { fruits, baskets } = input;
        const result = numOfUnplacedFruits(fruits, baskets);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();