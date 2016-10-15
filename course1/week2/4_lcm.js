'use strict';
const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });

rl.on('line', line => {
    let [a,b] = line.split(' ').map(a => parseInt(a));
    console.log(lcm(a, b));
    process.exit(0);
});

function gcd(a, b) {
    if (!b) return a;
    return gcd(b, a % b);
}

function lcm(a, b) {
    return mul(a / gcd(a, b), b);
}

function mul(a, b) {
    let a_digits = digits(a).reverse();
    let b_digits = digits(b).reverse();
    let out = [];

    for (let i = 0; i < b_digits.length; i++) {
        let carry = 0;
        let digit;
        let j = i;
        for (; j < a_digits.length + i; j++) {
            digit = (out[j] || 0) + (b_digits[i] * a_digits[j - i]) + carry;
            carry = Math.floor(digit / 10);
            out[j] = digit % 10;
        }

        if (carry) {
            digit = (out[j] || 0) + carry;
            carry = Math.floor(digit / 10);
            out[j] = digit % 10;
        }
    }

    return out.reverse().join('');
}

function digits(n) {
    return n.toString().split('').map(i => parseInt(i))
}