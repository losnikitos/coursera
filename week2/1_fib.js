'use strict';
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

rl.on('line', line => {
    let n = parseInt(line);
    console.log(fib(n).toFixed());
    process.exit(0);
});

function fib(n) {
    if (n <= 1) return n;
    if (n == 2) return 1;
    let a1 = 1;
    let a2 = 1;
    for (let i = 3; i < n; i++) {
        let _a2 = a2;
        a2 = a1 + a2;
        a1 = _a2;
    }
    return a1 + a2;
}