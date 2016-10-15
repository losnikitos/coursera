'use strict';

/** BIG NUMBERS */

function Big(n) {
    if (typeof n == 'object') {
        this.sign = n.sign;
        this.digits = n.digits;
    } else {
        this.sign = n < 0 ? -1 : 1;
        this.digits = (n * this.sign).toString().split('').map(i => parseInt(i)).reverse();
    }
}

Big.prototype.mul = function (other) {
    let a = this;
    let b = typeof other == 'number' ? new Big(other) : other;

    let out = new Big({ sign: a.sign * b.sign, digits: [] });

    for (let i = 0; i < b.digits.length; i++) {
        let carry = 0;
        let digit;
        let j = i;
        for (; j < a.digits.length + i; j++) {
            digit = (out.digits[j] || 0) + (b.digits[i] * a.digits[j - i]) + carry;
            carry = Math.floor(digit / 10);
            out.digits[j] = digit % 10;
        }

        if (carry) {
            digit = (out.digits[j] || 0) + carry;
            carry = Math.floor(digit / 10);
            out.digits[j] = digit % 10;
        }
    }

    return out;
};

Big.prototype.abs = function () {
    return new Big({ sign: 1, digits: this.digits })
};

Big.prototype.gte = function (other) {
    let a = this;
    let b = typeof other == 'number' ? new Big(other) : other;
    if (a.digits.length !== b.digits.length) return a.sign * a.digits.length > b.sign * b.digits.length;
    return a.sign * a.digits.slice(-1)[0] >= b.sign * b.digits.slice(-1)[0]; // compare last digits
};

Big.prototype.add = function (other) {
    let a = this;
    let b = typeof other == 'number' ? new Big(other) : other;

    if (a.sign * b.sign == -1 && b.abs().gte(a.abs())) {
        [a, b] = [b, a]; // now a >= b
    }

    let out = new Big({ sign: a.sign, digits: [] });
    let carry = 0;

    for (let i = 0; i < b.digits.length || i < a.digits.length; i++) {
        let digit = (a.digits[i] || 0) + (a.sign * b.sign) * (b.digits[i] || 0) + carry;
        if (digit >= 10) {
            carry = 1;
            digit -= 10;
        } else if (digit < 0) {
            carry = -1;
            digit += 10
        } else {
            carry = 0;
        }

        out.digits.push(digit);
    }

    if (carry == 1) out.digits.push(carry);

    return out;
};

Big.prototype.toString = function () {
    return (this.sign == -1 ? '-' : '') + this.digits.reverse().join('');
};

/** BIG NUMBERS */

function placeAds(ads, slots) {
    ads.sort().reverse();
    slots.sort().reverse();

    let sum = new Big(0);
    for (let i = 0; i < ads.length; i++) {
        sum = sum.add(new Big(ads[i]).mul(slots[i])); // sum += ads[i] * slots[i];
    }
    return sum.toString();
}

function fromStdin() {
    const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });

    let data = [];
    rl.on('line', line => {
        data.push(line.split(' ').map(i => parseInt(i)));
        if (data.length == 3) {
            let [n, ads, slots] = data;
            console.log(placeAds(ads, slots));
            rl.close();
        }
    });
}

// function test(ads, slots, correct) {
//     let result = placeAds(ads, slots);
//     console.log(result == correct ? 'ok' : `wrong: ${result} instead of ${correct}`);
// }
//
// test([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 55);
// test([23], [39], 897);
// test([1, 3, -5], [-2, 4, 1], 23);
//
// let max = [];
// for (let i = 0; i < 1000; i++) max.push(100000);
// test(max, max, 10000000000000);

fromStdin();

