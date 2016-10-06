'use strict';

let solutions = [[]];
function getSolution(item, weight) {
    if(item == -1 || weight == -1) return 0;
    if(!solutions[item]) return 0;
    return solutions[item][weight] || 0;
}

function setSolution(item, weight, value) {
    if(!solutions[item]) solutions[item] = [];
    solutions[item][weight] = value;
}

function backpack(totalWeight, items) {
    for (let weight = 0; weight <= totalWeight; weight++) {
        for (let itemIndex = 0; itemIndex < items.length; itemIndex++) {
            let itemWeight = items[itemIndex];
            let valueIfLeave = getSolution(itemIndex - 1, weight);                                   // leave
            let valueIfTake = itemWeight <= weight ? getSolution(itemIndex - 1, weight - itemWeight) + itemWeight : 0;          // take
            // console.log('рюкзак', weight, 'штуку', itemWeight, 'берем?', valueIfTake, 'не берем?', valueIfLeave);
            setSolution(itemIndex, weight, Math.max(valueIfLeave, valueIfTake));
        }
    }
    // console.log(solutions);
    return getSolution(items.length - 1, totalWeight);
}

function fromStdin() {
    const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });
    let totalWeight = 0;
    rl.on('line', line => {
        if (!totalWeight) {
            totalWeight = parseInt(line.split(' ')[0]);
            return;
        }
        let items = line.split(' ').map(item => parseInt(item));
        let res = backpack(totalWeight, items);
        console.log(res);
        rl.close();
    });
}
fromStdin();

// function test(totalWeight, items, correct) {
//     let result = backpack(totalWeight, items);
//     console.log(result.toString() == correct.toString() ? 'ok' : `wrong: ${result} instead of ${correct}`);
// }
//
// test(10, [1, 4, 8], 9);
// test(100, [10, 15, 20, 25, 50], 100);