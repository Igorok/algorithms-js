
/*
Need to move 3 discs from A to C
1/ move 1st disc to c
2/ move 2nd disc to b
3/ move 1st disc to b
4/ move 3rd disc to c
5/ move 1st disc to a
6/ move 2nd disc to c
7/ move 1st disc to c

1/ move n-1 disc from the from peg to the unused peg
2/ move n-1 disc from the unused peg to the to peg
*/

const from = 1;
const unused = 2;
const to = 3;
let movements = 0;

/*

need to move 3 discs from a 1 to a 3 peg
move 2 disc from 1 to 2
    move disc 1 from 1 to 3
    move disc 1 from 3 to 2
move 2 disc from 2 to 3
    move disc

*/
const hanoiTowers = (num, from, to) => {
    if (num === 1) {
        console.log(`Move disc ${num} from ${from} to ${to}`);
        ++movements;
        return;
    }
    const u = 6 - from - to;
    // move n-1 disc from the from peg to the unused peg
    hanoiTowers(num - 1, from, u);
    console.log(`Move disc ${num} from ${from} to ${to}`);
    ++movements;
    // move n-1 disc from the unused peg to the to peg
    hanoiTowers(num - 1, u, to);
};

hanoiTowers(3, from, to);
console.log('movements', movements);

// movements = 0;
// hanoiTowers(6, from, to);
// console.log('movements', movements);
