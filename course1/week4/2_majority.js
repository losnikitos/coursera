'use strict';

function majority(array, low = 0, high = array.length - 1) {
    if (high <= low) return {
        size: 1,
        elem: array[low]
    };
    let mid = low + Math.floor((high - low) / 2);
    let half = Math.floor((high - low + 1) / 2);

    let L = majority(array, low, mid);
    let R = majority(array, mid + 1, high);

    if (L && R && L.elem == R.elem) {
        return {
            size: L.size + R.size,
            elem: L.elem
        };
    }

    if (R) {
        for (let i = low; i <= mid; i++)
            (array[i] == R.elem) && R.size++;
        if (R.size > half) return R;
    }

    if (L) {
        for (let i = mid + 1; i <= high; i++)
            (array[i] == L.elem) && L.size++;

        if (L.size > half) return L;
    }

    return null;
}

function fromStdin() {
    const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });
    let n = 0;
    rl.on('line', line => {
        if (!n) {
            n = parseInt(line);
            return;
        }
        let array = line.split(' ').map(i => parseInt(i));
        console.log(majority(array) ? 1 : 0);
        rl.close();
    });
}
fromStdin();

function test(array, correct) {
    let result = majority(array) ? 1 : 0;
    console.log(result.toString() == correct.toString() ? 'ok' : `wrong: ${result} instead of ${correct}`);
}

test([10, 20, 5, 30, 5, 40, 5, 5, 5, 60], 0);
test([2, 3, 9, 2, 2], 1);
test([1, 2, 3, 4], 0);
test([1, 2, 3, 1], 0);
test([5, 1, 5, 2, 5, 3, 5], 1);
test([1, 1, 1, 1, 1, 1], 1);
test([1, 1, 1, 2, 2, 2], 0);
test([1, 2, 1, 2, 1, 2], 0);
test([1, 1, 1, 1, 5, 5, 5, 5, 5], 1);
test([512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772], 0);
