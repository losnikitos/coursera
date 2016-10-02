'use strict';

function qsort(a) {
    if (a.length == 0) return [];
    if (a.length == 1) return a;
    let mid = Math.floor(a.length / 2);
    let less = [];
    let more = [];
    a.forEach((item, i) => {
        if (i == mid) return;
        item <= a[mid] ? less.push(item) : more.push(item);
    });
    return qsort(less).concat(a[mid]).concat(qsort(more));
}

function test(array) {
    let result = qsort(array);
    let correct = array.sort();
    console.log(result.toString() == correct.toString() ? 'ok' : `wrong: ${result} instead of ${correct}`);
}

test([1, 5, 9, 5, 1]);
test([500, 300, 200, 13, 44, 2342, 543, 654, 23, 43, 54, 234, 543]);
