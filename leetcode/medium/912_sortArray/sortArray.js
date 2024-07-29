const qs = (arr) => {
    if (arr.length < 2) return arr;

    const m = Math.floor(arr.length / 2);
    let left = [];
    let right = [];
    let middle = [];

    for (let i = 0; i < arr.length; ++i) {
        if (arr[i] === arr[m]) {
            middle.push(arr[i]);
        } else if (arr[i] < arr[m]) {
            left.push(arr[i]);
        } else {
            right.push(arr[i]);
        }
    }

    left = qs(left);
    right = qs(right);

    return left.concat(middle.concat(right));
};

/*

[10, 7, 8, 9, 1, 5, 9, 9, 5, 10]

*/
const partitioning = (arr, start, end) => {
    const pivot = arr[start];
    let left = start;
    let right = end;
    let i = start;

    while (i <= right) {
        if (arr[i] < pivot) {
            const tmp = arr[left];
            arr[left] = arr[i];
            arr[i] = tmp;
            left += 1;
            i += 1;
        } else if (arr[i] > pivot) {
            const tmp = arr[right];
            arr[right] = arr[i];
            arr[i] = tmp;
            right -= 1;
        } else {
            i += 1;
        }
    }

    return { left, right };
};

const qsip = (arr, start, end) => {
    if (start >= end) return;

    let { left, right } = partitioning(arr, start, end);

    qsip(arr, start, left - 1);
    qsip(arr, right + 1, end);
};

function sortArray(nums) {
    qsip(nums, 0, nums.length- 1);
    return nums;
};




const test = () => {
    const params = [
        {
            input: [4, 5, 2, 1],
            output: [1, 2, 4, 5],
        },
        {
            input: [10, 7, 8, 9, 1, 5, 9, 9, 5, 10],
            output: [1, 5, 5, 7, 8, 9, 9, 9, 10, 10],
        },
    ];
    for (let i = 0; i < 10; ++i) {
        const input = [];
        for (let j = 0; j < 100; ++j) {
            input.push(Math.round(Math.random() * 1000));
        }
        const output = [...input].sort((a, b) => a - b);
        params.push({ input, output });
    }

    params.forEach(({ input, output }) => {
        const result = sortArray(JSON.parse(JSON.stringify(input)));

        console.log(
            (JSON.stringify(output) === JSON.stringify(result)) ? 'SUCCESS' : 'ERROR',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();
