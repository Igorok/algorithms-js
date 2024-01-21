import assert from 'node:assert';
import { Sorting } from './sorting.js';

class MergeSorting extends Sorting {
    #recursiveSorting (array) {
        if (array.length < 2) {
            return array;
        }

        const middle = Math.round(array.length / 2);
        const left = this.#recursiveSorting(array.slice(0, middle));
        const right = this.#recursiveSorting(array.slice(middle, array.length));

        let i = 0;
        let j = 0;
        const merged = [];
        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                merged.push(left[i]);
                i++;
            } else {
                merged.push(right[j]);
                j++
            }
        }

        while (i < left.length) {
            merged.push(left[i]);
            i++;
        }

        while (j < right.length) {
            merged.push(right[j]);
            j++;
        }


        return merged;
    }
    sort () {
        return this.#recursiveSorting(this.array);
    }
}

const local = new MergeSorting().sort();
const correct = new Sorting().array.sort((a, b) => a - b);

console.log(local, correct);
assert.deepEqual(local, correct);

