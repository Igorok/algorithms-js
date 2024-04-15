import assert from 'node:assert';
import { Sorting } from './sorting.js';

class QuickSorting extends Sorting {
    #recursiveSorting (array) {
        if (array.length < 2) {
            return array;
        }

        let left = [];
        let right = [];
        const idx = Math.floor(Math.random() * array.length);
        for (let i = 0; i < array.length; i++) {
            if (i === idx) {
                continue;
            }
            if (array[i] < array[idx]) {
                left.push(array[i]);
            } else {
                right.push(array[i]);
            }
        }

        left = this.#recursiveSorting(left);
        left.push(array[idx]);
        right = this.#recursiveSorting(right);

        return left.concat(right);
    }

    sort () {
        return this.#recursiveSorting(this.array);
    }
}

const local = new QuickSorting().sort();
const correct = new Sorting().array.sort((a, b) => a - b);

console.log(local, correct);
assert.deepEqual(local, correct);
