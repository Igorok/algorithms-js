/**
 Do not return anything, modify arr in-place instead.
 */
function duplicateZeros(arr: number[]): void {
    const copy: number[] = [...arr];
    let shift: number = 0;

    for (let i: number = 0; i < copy.length; ++i) {
        if (i + shift < arr.length) {
            arr[i + shift] = copy[i];
        }
        if (copy[i] === 0) {
            shift += 1;
            if (i + shift < arr.length) {
                arr[i + shift] = 0;
            }
        }
    }
};

const test = () => {
    const params = [
        {
            input: {
                arr: [1,0,2,3,0,4,5,0],
            },
            output: [1,0,0,2,3,0,0,4],
        },
        {
            input: {
                arr: [1,2,3],
            },
            output: [1,2,3],
        },
    ];

    params.forEach(({input, output}) => {
        const { arr } = input;
        const prev: number[] = [...arr];
        duplicateZeros(arr);

        console.log(
            JSON.stringify(arr) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(prev),
            'output', output,
            'result', arr,
        );
    });
};

test();