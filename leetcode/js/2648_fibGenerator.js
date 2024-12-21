/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let i = 0;
    const values = [0, 1];
    while (true) {
        i += 1;
        if (i < 2) {
            yield i - 1;
        } else {
            values.push(values[i-1] + values[i-2]);
            yield values[i-1];
        }
    }
};
const gen = fibGenerator();
let i = 0;
for (const v of gen) {
    console.log(v);
    if (i === 10) break;
    i += 1;
}