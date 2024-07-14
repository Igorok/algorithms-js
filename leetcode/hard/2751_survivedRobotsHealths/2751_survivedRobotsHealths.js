/**
 * @param {number[]} positions
 * @param {number[]} healths
 * @param {string} directions
 * @return {number[]}
 */
var survivedRobotsHealths_ = function(positions, healths, directions) {
    if (positions.length < 2) return healths;

    const pos = positions.map((p, i) => {
        return {p, i, h: healths[i], d: directions[i]};
    });
    console.log('pos', pos);

    const quickCollapse = (robots) => {
        if (robots.length < 2) {
            return robots;
        }

        let left = [];
        let right = [];

        const middle = robots[0];
        let leftD = 'L';
        let rightD = 'R';

        for (let i = 1; i < robots.length; ++i) {
            if (robots[i].p < middle.p) {
                if (robots[i].d === 'R') {
                    leftD = 'R';
                }
                left.push(robots[i]);
            } else {
                if (robots[i].d === 'L') {
                    rightD = 'L';
                }
                right.push(robots[i]);
            }
        }

        left = quickCollapse(left);
        right = quickCollapse(right);

        if (directions[middle.i] === 'R') {
            leftD = 'R';
            left.push(middle);
        } else {
            rightD = 'L';
            right.unshift(middle);
        }

        if (leftD === 'R' && rightD === 'L') {
            const newLeft = [];
            while (left.length) {
                const l = left.pop();
                if (directions[l.i] == 'L') {
                    newLeft.push(l);
                    continue;
                }

                const newRight = [];
                while (right.length) {
                    const r = right.shift();
                    if (directions[r.i] == 'R') {
                        newRight.push(r);
                        continue;
                    }

                    if (healths[l.i] > healths[r.i]) {
                        healths[r.i] = 0;
                        healths[l.i] -= 1;
                        l.h = healths[l.i];
                        r.h = healths[r.i];
                        if (healths[l.i] === 0) break;
                    } else if (healths[l.i] < healths[r.i]) {
                        healths[l.i] = 0;
                        healths[r.i] -= 1;
                        l.h = healths[l.i];
                        r.h = healths[r.i];
                        if (healths[r.i] !== 0) {
                            newRight.push(r);
                        }
                        break;
                    } else {
                        healths[l.i] = 0;
                        healths[r.i] = 0;
                        l.h = healths[l.i];
                        r.h = healths[r.i];
                        break;
                    }
                }

                if (newRight.length)
                    right = newRight.concat(right);

                if (healths[l.i] !== 0) {
                    newLeft.push(l);
                }
            }
            left = left.concat(newLeft.reverse());
        }

        return left.concat(right);
    };

    let res = quickCollapse(pos);
    console.log('res', res);

    return healths.reduce((acc, val) => {
        if (!val) return acc;
        acc.push(val);
        return acc;
    }, []);
};

var survivedRobotsHealths = function(positions, healths, directions) {
    if (positions.length < 2) return healths;

    let pos = positions.map((p, i) => {
        return {p, i, h: healths[i], d: directions[i]};
    }).sort((a, b) => a.p - b.p);

    console.log('pos', pos);

    const right = [];
    while (pos.length) {
        const l = pos.pop();
        if (directions[l.i] === 'L') {
            right.push(l);
            continue;
        }

        if (directions[l.i] === 'R') {
            while (right.length) {
                const r = right.pop();

                if (healths[l.i] > healths[r.i]) {
                    healths[r.i] = 0;
                    healths[l.i] -= 1;
                    l.h = healths[l.i];
                    r.h = healths[r.i];
                    if (healths[l.i] === 0) break;
                } else if (healths[l.i] < healths[r.i]) {
                    healths[l.i] = 0;
                    healths[r.i] -= 1;
                    l.h = healths[l.i];
                    r.h = healths[r.i];
                    if (healths[r.i] !== 0) {
                        right.push(r);
                    }
                    break;
                } else {
                    healths[l.i] = 0;
                    healths[r.i] = 0;
                    l.h = healths[l.i];
                    r.h = healths[r.i];
                    break;
                }
            }
        }
    }

    return healths.filter(v => Boolean(v));
};



const test = () => {
    const params = [
        {
            input: [[5,4,3,2,1], [2,17,9,15,10], "RRRRR"],
            output: [2,17,9,15,10],
        },
        {
            input: [[3,5,2,6], [10,10,15,12], "RLRL"],
            output: [14],
        },
        {
            input: [[1,2,5,6], [10,10,11,11], "RLRL"],
            output: [],
        },
        {
            input: [[13,3], [17,2], "LR"],
            output: [16],
        },
        {
            input: [[1,36,13,18,49], [37,26,12,45,15], "RRLLR"],
            output: [26,44,15],
        },
        /*

        1 13 18 36 49
        R L  L  R  R
        37 12 45 26 15

        */
    ];

    params.forEach(({input, output}) => {
        const result = survivedRobotsHealths(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', input,
            'output', output,
            'result', result,
        );

    });
};

test();
