/**
 * @param {number[]} nums
 * @return {boolean}
 */
var primeSubOperation = function(nums) {
    let primeNumbers = [0];
    const isPrimeNumber = (num) => {
        const end = Math.floor(Math.sqrt(num));
        for (let i = 2; i <= end; ++i) {
            if ((num % i) === 0) {
                return false;
            }
        }
        return true;
    };

    for (let i = 2; i <= Math.max(...nums); ++i) {
        if (isPrimeNumber(i)) {
            primeNumbers.push(i);
        }
    }
    primeNumbers = primeNumbers.reverse();

    const arr = [];
    for (const num of nums) {
        let res;
        for (const prime of primeNumbers) {
            res = num - prime;
            if (res <= 0) {
                continue;
            }
            if (!arr.length || arr[arr.length - 1] < res) {
                break;
            }
        }

        if (!arr.length || arr[arr.length - 1] < res) {
            arr.push(res);
        } else {
            return false;
        }
    }

    return true;
};



const test = () => {
    const params = [
        {
            input: [4,9,6,10],
            output: true,
        },
        {
            input: [6,8,11,12],
            output: true,
        },
        {
            input: [5,8,3],
            output: false,
        },
    ];

    for (const { input, output } of params) {
        const result = primeSubOperation(input);
        const message = `
            INPUT: ${input}
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
