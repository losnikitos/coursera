'use strict';
const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });

rl.on('line', line => {
    let [a,b] = line.split(' ').map(a => parseInt(a));
    console.log(gcd(a, b).toFixed());
    process.exit(0);
});

function gcd(a, b) {
    if (!b) return a;
    return gcd(b, a % b);
}