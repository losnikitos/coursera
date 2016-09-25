'use strict';
const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });

rl.on('line', line => {
    let m = parseInt(line);
    console.log(change(m));
    rl.close();
});

function change(m) {
    let sum = 0;
    let usedCoins = 0;
    let coins = [10, 5, 1];

    coins.forEach(coin => {
        while(sum + coin <= m) {
            sum += coin;
            usedCoins++;
        }
    });

    return usedCoins;
}