/**
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var minimizeXor = function(num1, num2) {
    const getSetBit = (num) => {
        let count = 0
        while (num !== 0) {
            count += num % 2;
            num = Math.floor(num / 2);
        }
        return count;
    };

    let set1 = getSetBit(num1);
    const set2 = getSetBit(num2);

    if (set1 === set2) {
        return num1;
    }

    let arr = parseInt(num1).toString(2).split('').reverse();

    if (set1 > set2) {
        let i = 0;
        while (set1 > set2) {
            if (arr[i] === '1') {
                arr[i] = '0';
                set1 -= 1;
            }
            i += 1;
        }
    } else {
        let i = 0;
        while (set1 < set2) {
            if (arr[i] !== '1') {
                arr[i] = '1';
                set1 += 1;
            }
            i += 1;
        }
    }

    return parseInt(arr.reverse().join(''), 2);
};

/*

3 011
5 101


*/

const test = () => {
    const params = [
        {
            input: [3, 5],
            output: 3,
        },
        {
            input: [1, 12],
            output: 3,
        },
        {
            input: [25, 72],
            output: 24,
        },
    ];

    for (const { input, output } of params) {
        const result = minimizeXor(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${JSON.stringify(output)}
            RESULT: ${result}`;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                `SUCCESS: ${message}`,
            );
        } else {
            console.error(`ERROR: ${message}`);
        }
    }
};

test();
