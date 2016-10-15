'use strict';

let distances = [[]];
function getDistance(from, to) {
    if (from == -1 && to == -1) return 0;
    if (from == -1) return to + 1;
    if (to == -1) return from + 1;
    return distances[from][to] || 0;
}

function setDistance(from, to, value) {
    if (!distances[from]) distances[from] = [];
    distances[from][to] = value;
}

function editDistance(from, to) {
    from.split('').forEach((fromLetter, fromIndex) => {
        to.split('').forEach((toLetter, toIndex) => {
            let distances = [
                getDistance(fromIndex - 1, toIndex - 1) + (fromLetter == toLetter ? 0 : 1), // replace or copy
                getDistance(fromIndex - 1, toIndex) + 1, // add
                getDistance(fromIndex, toIndex - 1) + 1  // remove
            ];
            setDistance(fromIndex, toIndex, Math.min(...distances));
        })
    });

    // printDistance(from, to);
    return getDistance(from.length - 1, to.length - 1);
}

// function printDistance(from, to) {
//     console.log('    ' + to.split('').join(' '));
//     console.log('    ' + to.split('').map(a => '|').join(' '));
//     distances.forEach((dist, index) => console.log(from[index], '—', dist.join(' ')));
// }

function fromStdin() {
    const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });
    let from = undefined;
    rl.on('line', line => {
        if (!from) {
            from = line;
            return;
        }
        let to = line;
        console.log(editDistance(from, to));
        rl.close();
    });
}
fromStdin();

function test(from, to, correct) {
    let result = editDistance(from, to);
    console.log(result.toString() == correct.toString() ? 'ok' : `wrong: ${result} instead of ${correct}`);
}

test('ab', 'ab', 0);
test('short', 'ports', 3);
test('editing', 'distance', 5);
// test('edi', 'di', 1);