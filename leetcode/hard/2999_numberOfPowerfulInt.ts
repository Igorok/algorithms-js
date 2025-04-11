function numberOfPowerfulInt(start: number, finish: number, limit: number, s: string): number {
    const numS = Number(s);
    const strStart = String(start);
    const strFinish = String(finish);


    const getCount = (str: string) => {

        const cache = new Map();

        const rec = (id: number, restricted: boolean, acc: string) => {
            const key = `${id}_${restricted}`;
            if (id === str.length) {
                return 1;
            }
            if (cache.has(key)) {
                return cache.get(key);
            }

            const idFromEnd = str.length - id;
            if (idFromEnd <= s.length) {
                const sId = s.length - idFromEnd;
                if (Number(s[sId]) > Number(str[id]) && restricted) {
                    cache.set(key, 0);
                    return 0;
                }
                const r = restricted && Number(s[sId]) === Number(str[id]);
                const res: number = rec(id + 1, r, acc + s[sId]);
                cache.set(key, res);
                return res;
            }

            let sum: number = 0;
            const top = restricted ? Math.min(Number(str[id]), limit) : limit;
            for (let i = 0; i <= top; ++i) {
                const r = i === Number(str[id]) && restricted;
                sum += rec(id + 1, r, acc + i);
            }

            cache.set(key, sum);
            return sum;
        };

        return rec(0, true, '');
    }


    let countStart: number = 0;
    if (start >= numS) {
        countStart = getCount(strStart);
        const suffStart = strStart.slice(strStart.length - s.length);
        const inLimit = strStart.split('').every(val => Number(val) <= limit);
        if (suffStart === s && inLimit) {
            countStart -= 1;
        }
    }
    const countFinish: number = finish < numS ? 0 : getCount(strFinish);


    return countFinish - countStart;
};

/*

1159
0020
0020
0020
0020
0020
0520
1020
1120



*/

const test = () => {
    const params = [
        {
            input: {
                start: 63935267123, finish: 334359420935946, limit: 6, s: "3"
            },
            output: 340924566339,
        },
        {
            input: {
                start: 20, finish: 1159, limit: 5, s: "20"
            },
            output: 8,
        },
        {
            input: {
                start: 1, finish: 971, limit: 9, s: "17"
            },
            output: 10,
        },
        {
            input: {
                start: 1, finish: 6000, limit: 4, s: "124"
            },
            output: 5,
        },
        {
            input: {
                start: 15, finish: 215, limit: 6, s: "10"
            },
            output: 2,
        },
        {
            input: {
                start: 1, finish: 111000, limit: 9, s: "124"
            },
            output: 111,
        },


        {
            input: {
                start: 1000, finish: 2000, limit: 4, s: "3000"
            },
            output: 0,
        },
    ];

    params.forEach(({ input, output }): void => {
        const { start, finish, limit, s }: {start: number, finish: number, limit: number, s: string} = input;
        const result = numberOfPowerfulInt(start, finish, limit, s);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();