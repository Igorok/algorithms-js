
var StockSpanner = function() {
    this.days = [];

    this.stack = [];
    this.i = 0;
};

/**
 * @param {number} price
 * @return {number}
 */
StockSpanner.prototype.next_1 = function(price) {
    this.days.push(price);

    for (let i = this.days.length - 1; i > -1; --i) {
        if (this.days[i] > price) {
            return this.days.length - 1 - i;
        }
    }

    return this.days.length;
};

/*



*/

StockSpanner.prototype.next = function(price) {
    this.i += 1;
    while (this.stack.length && this.stack[this.stack.length - 1][0] <= price) {
        this.stack.pop()
    }
    const id = this.stack.length ? this.stack[this.stack.length - 1][1] : 0;
    this.stack.push([price, this.i]);

    return this.i - id;
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */


const test = () => {
    const params = [
        {
            input: [
                ["next", "next", "next", "next", "next", "next", "next"],
                [[100], [80], [60], [70], [60], [75], [85]]
            ],
            output: [1, 1, 1, 2, 1, 4, 6],
        },
    ];

    params.forEach(({input, output}) => {
        const stockSpanner = new StockSpanner();

        for (let i = 0; i < input[0].length; ++i) {
            const command = input[0][i];
            const num = input[1][i][0];
            const result = stockSpanner[command](num);

            console.log(
                JSON.stringify(result) === JSON.stringify(output[i]) ? 'SUCCESS ' : 'ERROR ',
                'input', JSON.stringify(input),
                'output', output[i],
                'result', result,
            );
        }


    });
};

test();