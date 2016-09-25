'use strict';

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

function testAdd(a, b) {
    let correct = a + b;
    let res = new Big(a).add(b).toString();
    console.log(res == correct ? 'ok' : `wrong ${a}+${b} should be ${correct}, not ${res}`);
}

function testGte(a, b) {
    let correct = a >= b;
    let res = new Big(a).gte(b);
    console.log(res == correct ? 'ok' : `wrong ${a}>=${b} should be ${correct}, not ${res}`);
}

testAdd(2, 3);
testAdd(33, -55);
testAdd(10, -5);
testAdd(5, -5);
testAdd(-5, 300);
testAdd(-5, -300);
testAdd(0, 40);

testGte(1, 2);
testGte(2, 1);
testGte(-5, -10);
testGte(-5, -5);
testGte(-10, -5);
testGte(-8, 8);
testGte(8, -8);
testGte(8, 0);
testGte(0, 0);
