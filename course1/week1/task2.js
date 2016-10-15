'use strict';
const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });

rl.on('line', line => {
    let data = line.split(' ').map(a => parseInt(a));
    if (data.length == 1) return;
    let top = topTwo(data);
    console.log(top[0] * top[1]);
    process.exit(0);
});

function topTwo(array) {
    let data = array.slice(2);
    let initial = [array[0], array[1]].sort().reverse();
    // top[0] самый большой, top[1] второй
    return data.reduce((top, item) => {
        if (item < top[1]) return top;
        if (item > top[0]) return [item, top[0]]; // самый большой
        return [top[0], item]; // второй
    }, initial);
}
