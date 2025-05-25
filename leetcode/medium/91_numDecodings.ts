function numDecodings(s: string): number {
    const cache: Map<number, number> = new Map();

    const getCount = (id: number): number => {
        if (id === s.length) {
            return 1;
        }
        if (s[id] === '0') {
            return 0;
        }
        if (cache.has(id)) {
            return cache.get(id);
        }

        let res: number = getCount(id + 1);
        if (id + 1 < s.length && parseInt(s.slice(id, id+2)) < 27) {
            res += getCount(id + 2);
        }

        cache.set(id, res);

        return res;
    };

    return getCount(0);
};

const test = () => {
    const params = [
        {
            input: "12",
            output: 2,
        },
        {
            input: "226",
            output: 3,
        },
        {
            input: "06",
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const result = numDecodings(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();