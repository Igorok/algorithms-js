/**
 * @param {string} formula
 * @return {string}
 */
const countOfValues = (formula) => {
    const braces = [new Map()];

    let letter = '';
    let digit = '';

    const closeDigit = () => {
        if (letter === '') return;

        if (letter === ')') {
            let closedMap = braces[braces.length - 1];
            if (digit) {
                digit = parseInt(digit);
                closedMap.forEach((c, l) => {
                    closedMap.set(l, (c * digit));
                });
            }

            if (braces.length > 1) {
                closedMap = braces.pop();
                const usedMap = braces[braces.length - 1];

                closedMap.forEach((c, l) => {
                    let count = usedMap.has(l) ? usedMap.get(l) : 0;
                    count += c;
                    usedMap.set(l, count);
                });
            }
        } else {
            const usedMap = braces[braces.length - 1];

            let count = usedMap.has(letter) ? usedMap.get(letter) : 0;
            if (!digit) {
                count += 1;
            } else {
                count += parseInt(digit);
            }
            usedMap.set(letter, count);
        }

        letter = '';
        digit = '';
    };

    for (let i = 0; i < formula.length; ++i) {
        if (formula[i] === '(') {
            closeDigit();
            braces.push(new Map());
            continue;
        }

        if (formula[i] === ')') {
            closeDigit();
            letter = ')';
            continue;
        }

        if (/\d/.test(formula[i])) {
            digit += formula[i];
            continue;
        }

        if (/\D/.test(formula[i])) {
            if (formula[i] !== formula[i].toUpperCase()) {
                letter += formula[i];
                continue;
            }

            if (formula[i] === formula[i].toUpperCase()) {
                closeDigit();
                letter = formula[i];
            }
        }
    }

    closeDigit();

    return braces[0];
};

var countOfAtoms = function(formula) {
    if (!formula || formula.length < 2) return formula;

    const countMap = countOfValues(formula);

    const result = Array.from(countMap.entries())
        .sort((a, b) => a[0] < b[0] ? -1 : 1)
        .map(([key, num]) => {
            if (num === 1) return key;
            return key + num;
        })
        .join('');

    return result;
};



const test = () => {
    const params = [
        {
            input: '(NB3)33',
            output: 'B99N33',
        },
        {
            input: 'H',
            output: 'H',
        },
        {
            input: 'H2O',
            output: 'H2O',
        },
        {
            input: 'H234O',
            output: 'H234O',
        },
        {
            input: 'HO123',
            output: 'HO123',
        },
        {
            input: 'Mg2O',
            output: 'Mg2O',
        },
        {
            input: 'Mg(OH)2',
            output: 'H2MgO2',
        },
        {
            input: 'K4(ON(SO3)2)2',
            output: 'K4N2O14S4',
        },
    ];

    params.forEach(({input, output}) => {
        const result = countOfAtoms(input);

        console.log(
            result === output ? 'SUCCESS ' : 'ERROR ',
            'input', input,
            'output', output,
            'result', result,
        );

    });
};

test();
