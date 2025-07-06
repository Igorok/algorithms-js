function possibleStringCount_0(word: string, k: number): number {
    const mod: number = 7 + 10**9;

    let groups: number[] = [];
    let l: number = 1;
    for (let i: number = 1; i < word.length; ++i) {
        if (word[i] !== word[i-1]) {
            groups.push(l);
            l = 1;
        } else {
            l += 1;
        }
    }
    groups.push(l);

    let total: number = 1;
    for (const l of groups) {
        total = (total * l) % mod;
    }

    if (groups.length >= k) {
        return total;
    }

    let prevComb: number[] = new Array(k).fill(0); // array with combinations for every length of string
    for (let i: number = 1; i <= Math.min(k-1, groups[0]); ++i) {
        prevComb[i] = 1;
    }

    for (let group: number = 1; group < groups.length; ++ group) {
        let currentComb: number[] = new Array(k).fill(0); // current combinations for every length

        // traverse from minimum length: group + 1
        // to max length: k
        for (let length: number = (group + 1); length < k; ++length) {

            // count used chars
            for (let used: number = 1; used <= groups[group]; ++used) {
                const prevId: number = length - used;
                if (prevId < 1) {
                    continue;
                }

                // accumulate all combinations for length
                currentComb[length] += prevComb[prevId];
            }
        }

        prevComb = currentComb;
    }

    // all combinations with length less than k
    let smallCombinations = 0;
    for (const comb of prevComb) {
        smallCombinations += comb;
    }


    return total - smallCombinations;
};


function possibleStringCount(word: string, k: number): number {
    const mod: number = 7 + 10**9;

    let groups: number[] = [];
    let l: number = 1;
    for (let i: number = 1; i < word.length; ++i) {
        if (word[i] !== word[i-1]) {
            groups.push(l);
            l = 1;
        } else {
            l += 1;
        }
    }
    groups.push(l);

    let total: number = 1;
    for (const l of groups) {
        total = (total * l) % mod;
    }

    if (groups.length >= k) {
        return total;
    }

    let prevComb: number[] = new Array(k).fill(0); // array with combinations for every length of string
    for (let i: number = 1; i <= Math.min(k-1, groups[0]); ++i) {
        prevComb[i] = 1;
    }

    let sumArray: number[] = new Array(k).fill(0);

    for (let group: number = 1; group < groups.length; ++ group) {
        let currentComb: number[] = new Array(k).fill(0); // current combinations for every length

        // I calculate sum of all previous cominations in one array
        for (let length: number = 1; length < k; ++length) {
            sumArray[length] = (sumArray[length - 1] + prevComb[length]) % mod;
        }

        for (let length: number = (group + 1); length < k; ++length) {
            // I should use the sum of previous groups[group] combinations
            currentComb[length] = sumArray[length - 1];
            // I can take all previous combinations  and remove length -1 - groups[group] cominations
            if (length - 1 - groups[group] > 0) {
                currentComb[length] = (mod + currentComb[length] - sumArray[length - 1 - groups[group]]) % mod;
            }
        }


        prevComb = currentComb;
    }

    // all combinations with length less than k
    let smallCombinations = 0;
    for (const comb of prevComb) {
        smallCombinations = (smallCombinations + comb) % mod;
    }


    return (total - smallCombinations + mod) % mod;
};




/*

word: "aabbccdd", k: 7,

12345678
aabbccdd

2 2 2 2


---

word: "aaabbb", k: 3,

abbb
abb
aabbb
aabb
aab
aaabbb
aaabb
aaab

---

word: "aaabbb", k: 3,

3, 2





*/

const test = () => {
    const params = [
        {
            input: {
                word: "aabbccdd", k: 7,
            },
            output: 5,
        },
        {
            input: {
                word: "aabbccdd", k: 8,
            },
            output: 1,
        },
        {
            input: {
                word: "aaabbb", k: 3,
            },
            output: 8,
        },
        {
            input: {
                word: "wwwwwwwbbbbssssssssvvoooooooqqqqqqqqqvvvvvooooooocccccppppkkkkkkjnddddddbbb", k: 50,
            },
            output: 497563975,
        },
    ];

    params.forEach(({ input, output }) => {
        const { word, k } = input;
        const result = possibleStringCount(word, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output)
                ? "SUCCESS "
                : "ERROR ",
            "input",
            JSON.stringify(input),
            "output",
            output,
            "result",
            result,
        );
    });
};

test();
