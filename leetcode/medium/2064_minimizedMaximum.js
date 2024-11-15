/**
 * @param {number} n
 * @param {number[]} quantities
 * @return {number}
 */
var minimizedMaximum_1 = function(n, quantities) {
    const goods = [...quantities].sort((a, b) => a - b);
    let sum = goods.reduce((acc, q) => acc + q, 0);
    let average = Math.round(sum / n);

    console.log(
        'sum', sum,
        'average', average,
        'goods', goods,
    );

    let max = average;
    const stores = [];
    let gId = 0;
    for (let i = 0; i < n; ++i) {
        average = Math.ceil(sum / (n - i));
        console.log(
            'i', i,
            'n - i', n - i,
            'sum', sum,
            'average', average,
        );

        let count = 0;

        if (i === n-1 || goods[gId] <= average || (goods[gId] - average) < (goods[gId] / 10) ) {
            count = goods[gId];
        } else {
            count = average;
        }

        max = Math.max(max, count);

        stores.push(count);
        goods[gId] -= count;
        if (goods[gId] == 0) {
            gId += 1;
        }
        sum -= count;



        console.log(
            'count', count,
            'sum', sum,
        );
    }

    console.log(
        'max', max,
        'stores', stores,
    );




    return max;
};

/*
6, [11,6]
11 = 2, 3, 3, 3
6 = 3, 3
max(2, 3, 3, 3, 3, 3) = 3

7, [15,10,10]
15 = 5,5,5
10 = 5,5
10 = 5,5
max(5,5,5, 5,5, 5,5) = 5


(11+6) / 6 = Math.floor()

*/

var minimizedMaximum = function(n, quantities) {
    const checkFill = (num) => {
        const products = [...quantities];
        const shops = [];
        let prodId = 0;
        for (let i = 0; i < n; ++i) {
            if (prodId === products.length) {
                return true;
            }
            if (products[prodId] <= num) {
                shops.push(products[prodId]);

                products[prodId] = 0;
                prodId += 1;
            } else {
                shops.push(num);

                products[prodId] -= num;
            }
        }

        if (prodId !== products.length) {
            return false;
        }

        return true;
    };

    const maxQ = Math.max(...quantities);

    // for (let i = 1; i <= maxQ; ++i) {
    //     if (checkFill(i)) {
    //         return i;
    //     }
    // }

    let start = 1;
    let end = maxQ;
    let res = -1;

    while (start <= end) {
        const middle = Math.floor((start + end) / 2);
        if (checkFill(middle)) {
            res = middle;
            end = middle - 1;
        } else {
            start = middle + 1;
        }
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: [6, [11,6]],
            output: 3,
        },
        {
            input: [7, [15,10,10]],
            output: 5,
        },
        {
            input: [1, [100000]],
            output: 100000,
        },
        {
            input: [4, [100, 1]],
            output: 34,
        },
        {
            input: [22, [25,11,29,6,24,4,29,18,6,13,25,30]],
            output: 13,
        },
        {
            input: [26, [24,18,12,6,3,24,5,19,10,20,2,18,27,3,13,22,11,16,19,13]],
            output: 19,
        },
    ];

    for (const { input, output } of params) {
        const result = minimizedMaximum(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (result === output) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
