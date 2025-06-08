function smallestEquivalentString(s1: string, s2: string, baseStr: string): string {
    const countChars: Map<string, number> = new Map();
    const smallestChar: Map<string, string> = new Map();
    const parents: Map<string, string> = new Map();

    const getParent = (char: string): string => {
        if (!parents.has(char)) {
            parents.set(char, char);
            smallestChar.set(char, char);
            countChars.set(char, 1);
            return char;
        }
        const parent: string = parents.get(char);
        if (parent === char) {
            return char;
        }

        const parentOfParent = getParent(parent);
        parents.set(char, parentOfParent);

        return parentOfParent;
    }

    const setParent = (char1: string, char2: string) => {
        const parent1: string = getParent(char1);
        const parent2: string = getParent(char2);

        if (parent1 === parent2) {
            return;
        }

        const smallest1: string = smallestChar.get(parent1);
        const smallest2: string = smallestChar.get(parent2);
        const smallest: string = smallest1 < smallest2 ? smallest1 : smallest2;

        const count1: number = countChars.get(parent1);
        const count2: number = countChars.get(parent2);

        const newParent: string = count1 >= count2 ? parent1 : parent2;
        parents.set(parent1, newParent);
        parents.set(parent2, newParent);

        smallestChar.set(newParent, smallest);
        countChars.set(newParent, count1 + count2);
    }

    for (let i: number = 0; i < s1.length; ++i) {
        setParent(s1[i], s2[i]);
    }

    const res: string[] = [];

    for (const char of baseStr) {
        const parent: string = getParent(char);
        const smallest: string = smallestChar.get(parent);

        res.push(smallest);
    }


    return res.join('');
};

/*

ERROR  input {"s1":"ddvexktmenioinkrgbpuhkuixocxgiwlbbdouqvrpnnrsdueot","s2":"ksvvwxspkqnfsjqikdssbrwooshgrdhpliptxhacskrwgxsskn","baseStr":"pcjfbtxshbboarojnopmxvfmctzrwrgxzispbllycynlssjtqz"} output aaaaaaaaaaaaaaaaaaaaaaaaaazaaaaazaaaaaayayaaaaaaaz result aaaaaaaaaaaaaaaaaaamaaamaazaaaaazaaaaaayayaaaaaaaz

ddvexktmenioinkrgbpuhkuixocxgiwlbbdouqvrpnnrsdueot
ksvvwxspkqnfsjqikdssbrwooshgrdhpliptxhacskrwgxsskn

pcjfbtxshbboarojnopmxvfmctzrwrgxzispbllycynlssjtqz
aaaaaaaaaaaaaaaaaaamaaamaazaaaaazaaaaaayayaaaaaaaz
aaaaaaaaaaaaaaaaaaaaaaaaaazaaaaazaaaaaayayaaaaaaaz

*/

const test = () => {
    const params = [
        {
            input: {
                s1: "ddvexktmenioinkrgbpuhkuixocxgiwlbbdouqvrpnnrsdueot",
                s2: "ksvvwxspkqnfsjqikdssbrwooshgrdhpliptxhacskrwgxsskn",
                baseStr: "pcjfbtxshbboarojnopmxvfmctzrwrgxzispbllycynlssjtqz"
            },
            output: 'aaaaaaaaaaaaaaaaaaaaaaaaaazaaaaazaaaaaayayaaaaaaaz',
        },
        {
            input: {
                s1: "leetcode", s2: "programs", baseStr: "sourcecode"
            },
            output: 'aauaaaaada',
        },
        {
            input: {
                s1: "parker", s2: "morris", baseStr: "parser",
            },
            output: 'makkek',
        },
        {
            input: {
                s1: "hello", s2: "world", baseStr: "hold"
            },
            output: 'hdld',
        },
    ];

    params.forEach(({input, output}) => {
        const { s1, s2, baseStr } = input;
        const result = smallestEquivalentString(s1, s2, baseStr);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();