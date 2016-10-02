'use strict';

function bestTime(data) {
    let segments = data.map(item => ({ start: item[0], end: item[1] })).sort((a, b) => a.end - b.end);
    return segments.reduce((points, segment) => {
        let current = points[points.length - 1];
        if (segment.start <= current) return points; // do nothing, segment already covered
        return points.concat(segment.end);
    }, [segments[0].end]);
}

function fromStdin() {
    const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });

    let n = 0;
    let segments = [];
    rl.on('line', line => {
        if (!n) {
            n = parseInt(line);
            return;
        }

        segments.push(line.split(' ').map(i => parseInt(i)));

        if (segments.length == n) {
            let visits = bestTime(segments);
            console.log(visits.length + '\n' + visits.join('\n'));
            rl.close();
        }
    });
}
fromStdin();

// function test(segments, correct) {
//     let result = bestTime(segments);
//     console.log(result.toString() == correct.toString() ? 'ok' : `wrong: ${result} instead of ${correct}`);
// }
// test([[1, 3], [2, 5], [3, 6]], [3]);
// test([[4, 7], [1, 3], [2, 5], [5, 6]], [3, 6]);
// test([[0, 1], [1, 2], [2, 3]], [1, 2]);
// todo: max
