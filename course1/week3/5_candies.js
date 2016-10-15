'use strict';

function giveCandies(candies) {
    let rewards = [];
    let prize = 1;
    while (candies) {
        prize = candies >= 2 * prize + 1 ? prize : candies;
        rewards.push(prize);
        candies -= prize;
        prize++;
    }
    return rewards
}

// function giveCandies(candies) {
//     let rewards = [];
//     let gave = 0;
//     for (let i = 1; i <= candies; i++) {
//         if (gave + i > candies) {
//             rewards[rewards.length - 1] += candies - gave;
//             return rewards;
//         }
//         rewards.push(i);
//         gave += i;
//     }
//     return rewards;
// }

function fromStdin() {
    const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });
    rl.on('line', line => {
        let kids = parseInt(line);
        let candies = giveCandies(kids);
        console.log(candies.length + '\n' + candies.join('\n'));
        rl.close();
    })
}
fromStdin();

// function test(kids, correct) {
//     let result = giveCandies(kids);
//     console.log(result.toString() == correct.toString() ? 'ok' : `wrong: ${result} instead of ${correct}`);
// }
//
// test(6, [1, 2, 3]);
// test(8, [1, 2, 5]);
// test(2, [2]);
// test(100, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 22]);
