'use strict';
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

rl.on('line', line => {
    let n = parseInt(line);
    console.log(fib(n));
    process.exit(0);
});

function fib(n) {
    let f = [0, 1, 1];
    for (let i = 3; i <= n; i++) {
        f[i] = (f[i - 2] + f[i - 1]) % 10;
    }
    return f[n];
}