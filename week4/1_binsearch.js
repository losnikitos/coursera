'use strict';

function binSearch(array, item, low = 0, high = array.length - 1) {
    // console.log(array.slice(low, high));
    let mid = Math.floor(low + (high - low) / 2);
    if (low > high) return -1;
    if (item == array[mid]) return mid;
    if (item > array[mid]) return binSearch(array, item, mid + 1, high);
    if (item < array[mid]) return binSearch(array, item, low, mid - 1);
}

function fromStdin() {
    const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });
    let array = null;
    rl.on('line', line => {
        if (!array) {
            array = line.split(' ').map(i => parseInt(i)).slice(1);
            return;
        }

        let items = line.split(' ').map(i => parseInt(i)).slice(1);
        let positions = items.map(item => binSearch(array, item));

        console.log(positions.join(' '));
        rl.close();
    });
}
fromStdin();

// function test(array, items, correct) {
//     let result = items.map(item => binSearch(array, item));
//     console.log(result.toString() == correct.toString() ? 'ok' : `wrong: ${result} instead of ${correct}`);
// }

// test([1, 5, 8, 12, 13], [8, 1, 23, 1, 11], [2, 0, -1, 0, -1]);