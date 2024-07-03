/**
 * Minimum Difference Between Largest and Smallest Value in Three Moves
 * I want to receive a minimum difference between largest and smallest values in the array. And I can remove three values for this.
 * @param {number[]} nums
 * @return {number}
 */
var minDifference = function(nums) {
    if (!nums?.length || nums.length < 5) return 0;

    const sorted = nums.sort((a, b) => a - b);

    let min = sorted[sorted.length - 1] - sorted[0];

    // start is 0
    const sizeOfDeletions = 3;
    for (let i = 0; i <= sizeOfDeletions; ++i) {
        const start = i;
        const end = sorted.length - 1 - (sizeOfDeletions - i);
        min = Math.min(min, sorted[end] - sorted[start]);
    }

    return min;
};

/*

1 2 3 4 5 6 7 8 9

*/
console.log(
    '[1, 2, 3, 4, 5, 6, 7, 8, 9]', minDifference([1, 2, 3, 4, 5, 6, 7, 8, 9]),
    '[1,5,0,10,14]', minDifference([1,5,0,10,14]),
    '[6,6,0,1,1,4,6]', minDifference([6,6,0,1,1,4,6]),
);
