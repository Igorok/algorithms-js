function peakIndexInMountainArray(arr: number[]): number {
    if (arr.length === 1) {
        return arr[0];
    }

    let res: number = 0;

    let left: number = 0;
    let right: number = arr.length - 1;

    while (left <= right) {
        const middle: number = Math.floor((left + right) / 2);

        if (arr[res] < arr[middle]) {
            res = middle;
        }

        if (
            (middle === 0 && arr[middle + 1] < arr[middle]) ||
            (middle === arr.length - 1 && arr[middle - 1] < arr[middle]) ||
            (middle > 0 && middle < arr.length - 1 && arr[middle] > arr[middle - 1] && arr[middle] > arr[middle + 1])
        ) {
            return middle;
        }

        if (
            arr[middle] >= arr[right] &&
            (
                (middle + 1 < arr.length - 1 && arr[middle] > arr[middle + 1]) ||
                middle === right
            )

        ) {
            right = middle - 1;
            continue;
        }

        if (
            arr[left] <= arr[middle] &&
            (
                (middle - 1 !== -1 &&  arr[middle-1] < arr[middle]) ||
                middle === left
            )
        ) {
            left = middle + 1
            continue;
        }
    }


    return res;
};


/*

1 2 3 4 5 6 7 2 1

*/

const test = () => {
    const params = [
        {
            input: {
                arr: [3,4,5,1],
            },
            output: 2,
        },
        {
            input: {
                arr: [0,1,0],
            },
            output: 1,
        },
        {
            input: {
                arr: [0,2,1,0],
            },
            output: 1,
        },
        {
            input: {
                arr: [0,10,5,2],
            },
            output: 1,
        },

    ];

    params.forEach(({input, output}) => {
        const { arr } = input;
        const result = peakIndexInMountainArray(arr);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

