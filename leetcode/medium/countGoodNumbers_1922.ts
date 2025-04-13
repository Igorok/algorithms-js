
function countGoodNumbers(n: number): number {
    const mod: bigint = 1_000_000_007n;

    const even: bigint = BigInt(Math.ceil(n / 2));
    const odd: bigint = BigInt(n) - even;


    const binaryExponentiation = (num: bigint, degree: bigint): bigint => {
        let res: bigint = 1n;
        while (degree > 0n) {
            if ((degree % 2n) === 1n) {
                res *= num;
                res %= mod;
            }

            num = (num * num) % mod;
            degree = degree / 2n;
        }
        return res;
    };


    const eDegree: bigint = binaryExponentiation(5n, even);
    const oDegree: bigint = binaryExponentiation(4n, odd);

    return Number((eDegree * oDegree) % mod);
};

/*
res = 1
2**11 = 2**5 * 2**5 * 2**1

res = 2
4**5 = 4**2 * 4**2 * 4**1

res = 8
16**2 = 16**1 * 16**1

res = 8
256

res = 2048


*/


const test = () => {
    const params = [
        {
            input: 1,
            output: 5,
        },
        {
            input: 4,
            output: 400,
        },
        {
            input: 50,
            output: 564908303,
        },
        {
            input: 806166225460393,
            output: 643535977,
        },
    ];

    params.forEach(({input, output}) => {
        const result = countGoodNumbers(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();