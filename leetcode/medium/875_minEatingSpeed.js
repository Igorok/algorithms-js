/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    const eatingAll = (num) => {
        let id = 0;
        let hours = 0;
        for (let i = 0; i < piles.length; ++i) {
            hours += Math.ceil(piles[i] / num);
            if (hours > h) return false;
        }
        return hours <= h;
    };

    const binarySearch = () => {
        let sum = piles.reduce((acc, p) => acc + p, 0);
        let start = Math.floor(sum / h);
        let end = Math.max(...piles);
        let res = end;
        while (start <= end) {
            const middle = Math.floor((start + end) / 2);
            if (eatingAll(middle)) {
                res = middle;
                end = middle - 1;
            } else {
                start = middle + 1;
            }
        }
        return res;
    }

    return binarySearch();
};

const test = () => {
    const params = [
        {
            input: [[3,6,7,11], 8],
            output: 4,
        },
        {
            input: [[30,11,23,4,20], 5],
            output: 30,
        },
        {
            input: [[30,11,23,4,20], 6],
            output: 23,
        },
        {
            input: [[332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184], 823855818],
            output: 14,
        },
    ];

    params.forEach(({input, output}) => {
        const result = minEatingSpeed(...input);

        console.log(
            result === output ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();