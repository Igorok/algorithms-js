function maxProfit_0(prices: number[]): number {
    const cache: number[] = new Array(prices.length).fill(-1);

    function getProfit(start: number): number {
        if (start >= prices.length - 1) {
            return 0;
        }
        if (cache[start] !== -1) {
            return cache[start];
        }

        let res1: number = 0;
        for (let i = start + 1; i < prices.length; ++i) {
            let r: number = prices[i] - prices[start];
            if (r <= 0) {
                break;
            }
            r += getProfit(i + 2);
            res1 = Math.max(res1, r);
        }

        let res2 = getProfit(start + 1);

        cache[start] = Math.max(res1, res2);

        return cache[start];
    };

    return getProfit(0);
};

/*
States?
noStock[n]; from: Math.max([noStock[n-1], sellStock[n-1]])
inStock[n]; from: Math.max([inStock[n-1], buy = noStock[n-1] - price[n]])
sellStock[n]; from: [sell = inStock[n-1] + price[n]]

---

prices =    [1,     2,      3,      0,      2]
noStock =   [0,     0,      1,      2,      2];
inStock =   [-1,    -1,     -1,     1,      1];
sellStock = [0,     1,      2,      -1,     3];

---

 */
function maxProfit(prices: number[]): number {
    const noStock: number[] = new Array(prices.length).fill(0);
    const inStock: number[] = new Array(prices.length).fill(0);
    const sellStock: number[] = new Array(prices.length).fill(0);

    inStock[0] = -prices[0];

    for (let i = 1; i < prices.length; ++i) {
        noStock[i] = Math.max(noStock[i - 1], sellStock[i - 1]);
        inStock[i] = Math.max(inStock[i - 1], noStock[i - 1] - prices[i]);
        sellStock[i] = inStock[i - 1] + prices[i];
    }

    return Math.max(noStock.at(-1), sellStock.at(-1));
};

const test = () => {
    const params = [
        {
            input: [2,1,4],
            output: 3,
        },
        {
            input: [1,2,3,0,2],
            output: 3,
        },
        {
            input: [1],
            output: 0,
        },
        {
            input: [1,2,3,0,2,1,2,3,0,2],
            output: 5,
        },
    ];

    params.forEach(({input, output}) => {
        const result = maxProfit(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();