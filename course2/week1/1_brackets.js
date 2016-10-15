'use strict';

var open = { '[': ']', '{': '}', '(': ')' };
var close = { ']': '[', '}': '{', ')': '(' };

function check(string) {
    var stack = [];
    for (var i = 0; i < string.length; i++) {
        var char = string[i];
        if (open[char]) {
            stack.push({ char: char, position: i });
        }
        else if (close[char]) {
            var match = stack.pop();
            if (!match || match.char !== close[char]) return i + 1
        }
    }
    if (!stack.length) return 'Success';
    return stack.pop().position + 1;
}

function fromStdin() {
    var rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });
    rl.on('line', function(line) {
        console.log(check(line));
        rl.close();
    });
}
fromStdin();

// function test(string, correct) {
//     var result = check(string);
//     console.log(result.toString() == correct.toString() ? 'ok' : `wrong: ${result} instead of ${correct}`);
// }
//
// test('[]', 'Success');
// test('{}[]', 'Success');
// test('[{}]', 'Success');
// test('(())', 'Success');
// test('{aaaaa', 1);
// test('{[}', 3);
// test('foo(bar);', 'Success');
// test('foo(bar[i);', 10);