function deckRevealedIncreasing(deck: number[]): number[] {
    const res: number[] = new Array(deck.length).fill(null);

    deck.sort((a, b) => b - a);

    let skip: boolean = false;
    let i: number = 0;

    while (deck.length) {
        if (res[i] === null) {
            if (!skip) {
                res[i] = deck.pop();
            }
            skip = !skip;
        }
        i = (i+1) % res.length;
    }

    return res;
};


/*
[2,13,3,11,5,17,7],

[2, 3, 5, 7, 11, 13, 17]

2, 3, 5, 7,
11, 13,
17

---

[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
[1,11,2,16,3,12,4,20,5,13,6,17,7,14,8,19,9,15,10,18]

1,2,3,4,5,6,7,8,9,10,
11,12,13,14,15,16,17,18,19,20

*/

const test = () => {
    const params = [
        {
            input: {
                deck: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            },
            output: [1,11,2,16,3,12,4,20,5,13,6,17,7,14,8,19,9,15,10,18],
        },
        {
            input: {
                deck: [17,13,11,2,3,5,7],
            },
            output: [2,13,3,11,5,17,7],
        },
        {
            input: {
                deck: [1,1000],
            },
            output: [1,1000],
        },
        {
            input: {
                deck: [1,2,3,4],
            },
            output: [1, 3, 2, 4],
        },
        {
            input: {
                deck: [1,2,3,4,5],
            },
            output: [1,5,2,4,3],
        },
    ];

    params.forEach(({input, output}) => {
        const {deck} = input;
        const result = deckRevealedIncreasing(deck);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();