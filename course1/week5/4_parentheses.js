'use strict';

let values = [[]];

function calc(a, b, op) {
    if (op == '+') return parseInt(a) + parseInt(b);
    if (op == '-') return parseInt(a) - parseInt(b);
    if (op == '*') return parseInt(a) * parseInt(b);
}

function evaluate(expression, start = 0, end = expression.length - 1) {
    if (start == end) return { min: expression[start], max: expression[start] };
    if (values[start] && typeof values[start][end] !== 'undefined') return values[start][end];

    // let print = '';
    // for(let i = start; i<= end; i++) print += expression[i];
    // console.log('['+print+']');

    let res = {
        min: Infinity,
        max: -Infinity
    };

    for (let i = start + 1; i < end; i += 2) {
        let operation = expression[i];

        let L = evaluate(expression, start, i - 1);
        let R = evaluate(expression, i + 1, end);

        let outcomes = [
            calc(L.min, R.min, operation),
            calc(L.max, R.min, operation),
            calc(L.min, R.max, operation),
            calc(L.max, R.max, operation)
        ];

        res.min = Math.min(res.min, ...outcomes);
        res.max = Math.max(res.max, ...outcomes);
    }

    if (!values[start]) values[start] = [];
    values[start][end] = res;

    // console.log('=>', res);
    return res;
}

function fromStdin() {
    const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });
    rl.on('line', line => {
        console.log(evaluate(line).max);
        rl.close();
    });
}
fromStdin();

// function test(exp, correct) {
//     let result = evaluate(exp).max;
//     console.log(result.toString() == correct.toString() ? 'ok' : `wrong: ${result} instead of ${correct}`);
// }
//
// test('1+5', 6);
// test('5-8+7*4-8+9', 200);