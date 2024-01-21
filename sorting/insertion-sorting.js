import assert from 'node:assert';
import { Sorting } from './sorting.js';

class InsertionSorting extends Sorting {
    sort () {
        for (let i = 1; i < this.array.length; i++) {
            let j = i - 1;
            const tmp = this.array[i];
            while (j >= 0 && this.array[j] > tmp) {
                this.array[j + 1] = this.array[j];
                j--;
            }
            if (j !== i-1) {
                this.array[j+1] = tmp;
            }
        }

        return this.array;
    }
}

const local = new InsertionSorting().sort();
const correct = new Sorting().array.sort((a, b) => a - b);

console.log(local, correct);
assert.deepEqual(local, correct);
