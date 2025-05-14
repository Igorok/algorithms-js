function lengthAfterTransformations(s: string, t: number): number {
    const mod: number = 7 + 10e8;
    const chars: number[] = new Array(26).fill(0);

    const aCode: number = 'a'.charCodeAt(0);
    for (const char of s) {
        const code: number = char.charCodeAt(0) - aCode;
        chars[code] += 1;
    }

    const cache: Map<string, number> = new Map();
    const rec = (id: number, count: number): number => {
        if (id + count < 26) {
            return 1;
        }

        const key: string = `${id}_${count}`;
        if (cache.has(key)) {
            return cache.get(key);
        }

        const pathToZ: number = 26 - id;
        const res: number = (rec(0, count - pathToZ) + rec(1, count - pathToZ)) % mod;

        cache.set(key, res);

        return res;
    }

    let res: number = 0;
    for (let i: number = 0; i < chars.length; ++i) {
        if (chars[i] === 0) {
            continue;
        }
        const count: number = rec(i, t);
        res += (count * chars[i]) % mod;
        res %= mod;
    }

    return res;
};

/*

a -> z
122 - 97 = 25

10, 15

---

a, b, ..., z,
                a,
                b,

---


if n + t < 25
    return 1
else
    rec(0, t - 25)
    rec(1, t - 25)


---


*/

const test = () => {
    const params = [
        {
            input: { s: "jqktcurgdvlibczdsvnsg", t: 7517 },
            output: 79033769,
        },
        {
            input: { s: "cu", t: 5 },
            output: 2,
        },
        {
            input: { s: "abcyy", t: 2 },
            output: 7,
        },
        {
            input: { s: "azbk", t: 1 },
            output: 5,
        },
    ];

    params.forEach(({input, output}) => {
        const { s, t } = input;

        const result = lengthAfterTransformations(s, t);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();