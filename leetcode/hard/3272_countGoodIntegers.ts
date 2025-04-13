/*
const factorials = new Array(11).fill(0);
factorials[1] = 1;
for (let i = 2; i < factorials.length; ++i) {
    factorials[i] = i * factorials[i-1];
}
console.log('factorials', JSON.stringify(factorials));
*/

function countGoodIntegers(n: number, k: number): number {
    const factorials: number[] = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800];

    const exists: Set<string> = new Set();
    const middle: number = Math.ceil(n / 2);
    const odd: boolean = (n % 2) === 1;

    const getPalindromString = (str: string): string => {
        const arr: string[] = str.split('');
        let right = [...arr].reverse();
        if (odd) {
            right = right.slice(1);
        }
        return arr.concat(right).join('');
    };

    const getCombinations = (str: string): number => {
        const count: Map<string, number> = new Map();
        for (const char of str) {
            count.set(char, (count.get(char) || 0) + 1);
        }

        let comb: number = factorials[str.length];
        if (count.has('0')) {
            comb = factorials[str.length - 1] * (str.length - (count.get('0') || 0))
        }

        count.forEach((value: number, key: string) => {
            comb /= factorials[value];
        });

        return comb;
    };

    let res: number = 0;
    const generateSequence = (id: number, acc: string) => {
        if (id === middle) {
            const str: string = getPalindromString(acc);

            const key: string = str.split('').sort().join('');

            if (exists.has(key) || (Number(str) % k) !== 0) {
                return;
            }

            exists.add(key);
            res += getCombinations(str);
            return;
        }

        const start: number = (id === 0) ? 1 : 0;
        for (let i = start; i < 10; ++i) {
            generateSequence(id + 1, acc + i)
        }
    }

    generateSequence(0, '');

    return res;
};

/*

3, 5
505
515
525
535
545
555
565
575
585
595


551
551, 515, 155
3!/2! = 3

555
555
3!/3! = 1

550
550, 505
(3-1)(3-1)! / 2! = 2

2002
(4-2)*(4-1)!/ 2!*2! = 2*6/4 = 3
2002, 2020, 2200

20002
(5-3)*(5-1)! / 2!*3! = 2*24/12 = 4
20002
20020
20200
22000




*/

const test = () => {
    const params = [
        {
            input: [10, 6],
            output: 13249798,
        },
        {
            input: [6, 6],
            output: 3109,
        },
        {
            input: [5, 6],
            output: 2468,
        },
        {
            input: [3, 5],
            output: 27,
        },
        {
            input: [1, 4],
            output: 2,
        },

    ];

    params.forEach(({input, output}) => {
        const [n, k] = input;
        const result = countGoodIntegers(n, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();