/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    if (x < 2) return x;

    const half = Math.ceil(x / 2);
    let sqr = 1;
    while (sqr <= half) {
        let newSqr = sqr + 1;
        let new2Sqr = sqr * 2;

        if ((newSqr ** 2) <= x) {
            sqr = newSqr;
        } else {
            return sqr;
        }

        if ((new2Sqr ** 2) <= x) {
            sqr = new2Sqr;
        }

    }
    return sqr;
};

console.log(
    mySqrt(3),
    mySqrt(4),
    mySqrt(100),
    mySqrt(10000),
    mySqrt(1085817232),
);
