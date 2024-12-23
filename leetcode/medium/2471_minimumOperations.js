
/*

var minimumOperations = function(root) {
    let res = 0;

    const getSwaps_0 = (arr) => {
        for (let i = 0; i < arr.length; ++i) {
            let minId = i;
            for (let j = i + 1; j < arr.length; ++j) {
                if (arr[j] < arr[minId]) {
                    minId = j;
                }
            }
            if (minId !== i) {
                const tmp = arr[i];
                arr[i] = arr[minId];
                arr[minId] = tmp;
                res += 1;
            }
        }
    };

    const getSwaps = (arr) => {
        if (arr.length < 2) return arr;

        const m = Math.floor(arr.length / 2);
        let merged = [];

        let i = 0
        let j = m;
        while (i < m && j < arr.length) {
            if (arr[i] <= arr[j]) {
                merged.push(arr[i]);
                i += 1;
            } else {
                merged.push(arr[j]);
                j += 1;
                res += 1;
            }
        }

        while (i < m) {
            merged.push(arr[i]);
            i += 1;
            res += 1;
        }

        while (j < arr.length) {
            merged.push(arr[j]);
            j += 1;
        }

        getSwaps(merged.slice(0, m));
        getSwaps(merged.slice(m, merged.length));

        return merged;
    };




    const queue = [];
    let currentLevel = 0;
    let currentNodes = [];
    if (root) {
        queue.push([root, 0]);
    }

    while (queue.length) {
        const [node, level] = queue.shift();
        if (level !== currentLevel) {
            getSwaps(currentNodes);
            currentNodes = [node.val];
            currentLevel += 1;
        } else {
            currentNodes.push(node.val);
        }
        if (node.left) {
            queue.push([node.left, level + 1]);
        }
        if (node.right) {
            queue.push([node.right, level + 1]);
        }
    }

    getSwaps(currentNodes);

    return res;
};

*/


const getSwaps_0 = (arr) => {
    let res = 0;

    for (let i = 0; i < arr.length; ++i) {
        let minId = i;
        for (let j = i + 1; j < arr.length; ++j) {
            if (arr[j] < arr[minId]) {
                minId = j;
            }
        }
        if (minId !== i) {
            const tmp = arr[i];
            arr[i] = arr[minId];
            arr[minId] = tmp;
            res += 1;
        }
    }

    console.log('getSwaps_0', arr);

    return res;
};

/*

[8, 8, 5, 6, 6, 6, 1, 6, 4, 9]

 */
const getSwaps_1 = (arr) => {
    let res = 0;
    const rec = (arr) => {
        if (arr.length < 2) return arr;

        const m = Math.floor(arr.length / 2);
        let left = [];
        let right = [];
        let middle = [];

        for (let i = 0; i < arr.length; ++i) {
            if (i === m) {
                middle.push(arr[i]);
                continue;
            };

            if (arr[i] < arr[m]) {
                if (i > m) {
                    res += 1;
                }
                left.push(arr[i]);
            } else {
                if (i < m) {
                    res += 1;
                }
                right.push(arr[i]);
            }
        }


        left = rec(left);
        left = left.concat(middle);

        right = rec(right);
        return left.concat(right);
    };

    const sorted = rec(arr);
    console.log('getSwaps', sorted, arr);

    return res;
};

const getSwaps_2 = (arr) => {
    let res = 0;
    const rec = (arr) => {
        if (arr.length < 2) return arr;

        const m = Math.floor(arr.length / 2);
        let left = rec(arr.slice(0 , m));
        let right = rec(arr.slice(m));

        const merged = [];

        let i = 0;
        let j = 0;

        while (i < m && j < right.length) {
            if (left[i] <= right[j]) {
                merged.push(left[i]);
                i += 1;
            } else {
                res += 1;

                merged.push(right[j]);
                j += 1;
            }
        }

        while (i < m) {
            merged.push(left[i]);
            i += 1;
        }

        while (j < right.length) {
            merged.push(right[j]);
            j += 1;
        }

        return merged;
    };



    const sorted = rec(arr);
    console.log('getSwaps', sorted, arr);

    return res;
};

const getSwaps = (arr) => {
    let res = 0;
    const sorted = [...arr].sort((a, b) => a - b);
    const keyByVal = arr.reduce((acc, val, key) => {
        acc[val] = key;
        return acc;
    }, {});

    for (let i = 0; i < arr.length; ++i) {
        if (arr[i] !== sorted[i]) {
            res += 1;

            const val = arr[i];
            const sortedKey = keyByVal[sorted[i]];
            arr[i] = sorted[i];
            arr[sortedKey] = val;

            keyByVal[val] = sortedKey;
            keyByVal[sorted[i]] = i;
        }
    }

    console.log('getSwaps', arr);

    return res;
};


for (let i = 0; i < 10; ++i) {
    const arr = []
    for (let j = 0; j < 10; ++j) {
        arr.push(Math.floor(Math.random() * 10));
    }
    const r0 = getSwaps_0([...arr]);
    const r = getSwaps([...arr]);

    console.log(
        (r0 === r ? 'INFO' : 'ERROR'),
        '\n arr', arr,
        '\n r0', r0,
        '\n r', r,
        '\n',
    );
}