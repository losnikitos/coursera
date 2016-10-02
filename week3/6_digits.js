'use strict';

function compare(num_a, num_b) {
    let a = num_a.toString() + num_b.toString();
    let b = num_b.toString() + num_a.toString();

    return parseInt(b) - parseInt(a);
}

// let digits = n => n.toString().split('').map(i => parseInt(i));

// function compare(num_a, num_b) {
//     let a = digits(num_a);
//     let b = digits(num_b);
//
//     for (let i = 0; i < Math.max(a.length, b.length); i++) {
//         a[i] = a[i] == undefined ? a[i - 1] : a[i];
//         b[i] = b[i] == undefined ? b[i - 1] : b[i];
//     }
//
//     return  parseInt(b.join('')) - parseInt(a.join(''));
// }

function biggestNumber(numbers) {
    // console.log(numbers.sort(compare));
    return numbers.sort(compare).join('');
}

function fromStdin() {
    const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });
    let n = 0;
    rl.on('line', line => {
        if (!n) {
            n = parseInt(line);
            return;
        }
        let numbers = line.split(' ').map(i => parseInt(i));
        console.log(biggestNumber(numbers));
        rl.close();
    })
}
fromStdin();

// function test(number, correct) {
//     let result = biggestNumber(number);
//     console.log(result.toString() == correct.toString() ? 'ok' : `wrong: ${result} instead of ${correct}`);
// }

// test([85, 858], 85885);
// test([232, 23], 23232);
// test([202, 20], 20220);
// test([10,100,1], 110100);
// test([9,2,200,100,110,8,1,1], 98220011110100);
// 232 < 23 but 202 > 20

// let max = [];
// for (var i = 1; i < 100; i++) max.push(i);
// test(max, 0);

// test([21, 2], 221);
// test([9, 4, 6, 1, 9], 99641);
// test([23, 39, 92], 923923);
// test([91, 9, 5], 9915);
// test([95, 9, 2], 9952);
// test([0, 0, 3], 300);
// test([29, 25, 2, 9, 1], 9292521);
// test([25, 52, 2, 5], 552252);
// test([1, 10], 110);
// test([190, 1], 1901);
//
// test([5, 54, 56], 56554);
//
// test([2, 8, 2, 3, 6, 4, 1, 1, 10, 6, 3, 3, 6, 1, 3, 8, 4, 6,
//         1, 10, 8, 4, 10, 4, 1, 3, 2, 3, 2, 6, 1, 5, 2, 9, 8, 5,
//         10, 8, 7, 9, 6, 4, 2, 6, 3, 8, 8, 9, 8, 2, 9, 10, 3, 10,
//         7, 5, 7, 1, 7, 5, 1, 4, 7, 6, 1, 10, 5, 4, 8, 4, 2, 7, 8,
//         1, 1, 7, 4, 1, 1, 9, 8, 6, 5, 9, 9, 3, 7, 6, 3, 10, 8, 10,
//         7, 2, 5, 1, 1, 9, 9, 5],
//    '9999999998888888888887777777776666666666555555554444444443333333333222222222111111111111111101010101010101010');