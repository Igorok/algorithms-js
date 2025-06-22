function minimumDeletions_0(word: string, k: number): number {
    const count: Map<string, number> = new Map();

    for (const char of word) {
        const c: number = count.get(char) || 0;
        count.set(char, c + 1);
    }

    let total: number = 0;
    const nums: number[] = [];
    count.forEach((value: number) => {
        total += value;
        nums.push(value);
    });

    nums.sort((a, b) => b - a);

    let removed: number = 0;
    let current: number = nums[0];
    for (let right: number = 1; right < nums.length; ++right) {
        const num: number = nums[right];
        let remainder: number = total - current;
        let max: number = num + k;
        let r: number = 0;
        let left: number = 0;

        while (nums[left] > max) {
            r += (nums[left] - max);
            left += 1;
        }

        if (r >= removed + remainder) {
            return removed + remainder;
        }

        current += num;
        removed = r;
    }


    return removed;
};

function minimumDeletions(word: string, k: number): number {
    const count: Map<string, number> = new Map();

    for (const char of word) {
        const c: number = count.get(char) || 0;
        count.set(char, c + 1);
    }

    let total: number = 0;
    const nums: number[] = [];
    count.forEach((value: number) => {
        total += value;
        nums.push(value);
    });

    nums.sort((a, b) => a - b);

    let res: number = Number.MAX_SAFE_INTEGER;
    let prev: number = 0;

    for (let i: number = 0; i < nums.length; ++i) {
        const num: number = nums[i];
        const max: number = num + k;
        let r: number = prev;

        for (let j: number = 0; j < nums.length; ++j) {
            if (nums[j] > max) {
                r += nums[j] - max;
            }
        }

        res = Math.min(res, r);
        prev += num;
    }


    return res;
};


/*

813

[
  59,
  54,
  53,
  52,
  50,
  50,
  46,
  45,
  44,
  43,
  43,
  43,
  43,
  42,
  42,
  36,
  35,
  33,
]


[59,54,53,52,50,50,46,45,44,43,43,43,43,42,42,36,35,33]

*/



const test = () => {
    const params = [
        {
            input: {
                word: "ykekkdhehmhhympxhgjyjsmmkxerplpeegaqwqmswpmkldlllrywjqyeqlmwyphgprsdorlllpmmwdwxsxgkwaogxgglokjykrqyhaasjjxalxwdkjexdqksayxqplwmmleevdkdqdvgelmdhkqgryrqawxeammjhpwqgvdhygyvyqahvkjrrjvgpgqxyywwdvpgelvsprqodrvewqyajwjsrmqgqmardoqjmpymmvxxqoqvhywderllksxapamejdslhwpohmeryemphplqlkddyhqgpqykdhrehxwsjvaqymykjodvodjgqahrejxlykmmaxywdgaoqvgegdggykqjwyagdohjwpdypdwlrjksqkjwrkekvxjllwkgxxmhrwmxswmyrmwldqosavkpksjxwjlldhyhhrrlrwarqkyogamxmpqyhsldhajagslmeehakrxjxpjjmjpydgkehesoygvosrhvyhrqmdhlomgmrqjrmxyvmapmspmdygkhsprqsaxsvsrkovdjprjjyworgqoakrwarjsryydpmvhvyalawsmlsdgolsxgaqhryemvkpkhqvvagmxoapmsmwkrakldlhyojqhjjghjxgksroqpoxqsorrelhqeseegpqpewxydvkvaoaldmsdpmvogaykhpxkjkwmslqjsdqowkqawxadevkswdhywrxkpvqxmgeolayqojqqwxoomyasjrqrjmoearskssppmxpgwrmsjlsrjyqrjkgwjwglxogmkqjpjkwyaqxymelsyxypqxrjvpmssoakksemjhvaxm",
                k: 2,
            },
            output: 161,
        },
        {
            input: {
                word: "yynaayyyy", k: 1,
            },
            output: 3,
        },
        {
            input: {
                word: "aabcaba", k: 0
            },
            output: 3,
        },
        {
            input: {
                word: "dabdcbdcdcd", k: 2
            },
            output: 2,
        },
        {
            input: {
                word: "aaabaaa", k: 2
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { word, k } = input;
        const result = minimumDeletions(word, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();