'use strict';

function knapsack(items, capacity) {
    items.forEach(item => item.price = item.value / item.weight);
    items.sort((a, b) => b.price - a.price); // price decreasing
    let weightUsed = 0;
    let totalValue = 0;

    for (let i = 0; i < items.length; i++) {
        let spaceLeft = capacity - weightUsed;
        if (spaceLeft < 0.0001) return totalValue;
        let item = items[i];
        let fits = Math.min(spaceLeft, item.weight);
        weightUsed += fits;
        totalValue += item.price * fits;
    }
    return totalValue;
}

function fromStdin() {
    const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });

    let itemsCount = 0;
    let capacity = 0;
    let items = [];

    rl.on('line', line => {
        let input = line.split(' ').map(i => parseInt(i));

        if (!itemsCount) [itemsCount, capacity] = input;
        else items.push({ value: input[0], weight: input[1] });

        if (items.length == itemsCount) {
            console.log(knapsack(items, capacity).toFixed(4));
            rl.close();
        }
    });
}

function test1() {
    let capacity = 10;
    let items = [{ weight: 20, value: 20 }, { weight: 5, value: 10 }, { weight: 4, value: 20 }];
    console.log(knapsack(items, capacity))
}

function test2() {
    let capacity = 50;
    let items = [{ value: 60, weight: 20 }, { value: 100, weight: 50 }, { value: 120, weight: 30 }];
    console.log(knapsack(items, capacity))
}

function test3() {
    let capacity = 10;
    let items = [{ value: 500, weight: 30 }];
    console.log(knapsack(items, capacity).toFixed(3));
}

fromStdin();