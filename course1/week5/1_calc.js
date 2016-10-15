'use strict';

let cache = [{ val: 0, op: 0 }, { val: 1, op: 0 }];

function min(a, b, c) {
    if (!b) return a;
    if (c) return min(min(a, b), c);
    return a.val <= b.val ? a : b;
}

function calc(n) {
    for (let i = 2; i <= n; i++) {
        let ways = [{ op: 1, val: cache[i - 1].val + 1 }];
        if (i % 2 == 0) ways.push({ op: 2, val: cache[i / 2].val + 1 });
        if (i % 3 == 0) ways.push({ op: 3, val: cache[i / 3].val + 1 });
        cache[i] = min(...ways);
    }
    return cache[n];
}

// function calc(n) {
//     console.log(n);
//     if (cache[n]) return cache[n];
//     let ways = [{ op: 1, val: calc(n - 1).val + 1 }];
//     if (n % 2 == 0) ways.push({ op: 2, val: calc(n / 2).val + 1 });
//     if (n % 3 == 0) ways.push({ op: 3, val: calc(n / 3).val + 1 });
//     cache[n] = min(ways);
//     return cache[n];
// }

function backtrace(n) {
    let res = [n];
    let index = n;
    while (cache[index].op) {
        let op = cache[index].op;
        if (op == 1) index--;
        if (op == 2) index /= 2;
        if (op == 3) index /= 3;
        res.push(index);
    }
    return res.reverse();
}

function fromStdin() {
    const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });
    rl.on('line', line => {
        let n = parseInt(line);
        calc(n);
        let res = backtrace(n);
        console.log(res.length-1);
        console.log(res.join(' '));
        rl.close();
    });
}
fromStdin();

// function test(n, correct) {
//     calc(n);
//     let result = backtrace(n);
//     console.log(result.toString() == correct.toString() ? 'ok' : `wrong: ${result} instead of ${correct}`);
// }
// test(1, [1]);
// test(5, [1, 3, 4, 5]);
// test(96234, [1, 3, 9, 10, 11, 33, 99, 297, 891, 2673, 8019, 16038, 16039, 48117, 96234]); //1,3,9,10,11,22,66,198,594,1782,5346,16038,16039,32078,96234
// test(36, [1, 3, 9, 18, 36]);