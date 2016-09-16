'use strict';
const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });

rl.on('line', line => {
    console.log(line.split(' ').map(a => parseInt(a)).reduce((a, b) => a + b));
    process.exit(0);
});