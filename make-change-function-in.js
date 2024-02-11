function makeChange(amount, coins) {
    // Sort coins in descending order
    coins.sort((a, b) => b - a);
    
    let change = [];
    
    for (let i = 0; i < coins.length; i++) {
        while (amount >= coins[i]) {
            change.push(coins[i]);
            amount -= coins[i];
        }
    }
    
    return change;
}

// Example usage:
const amount = 47;
const coins = [25, 10, 5, 1];
console.log(makeChange(amount, coins)); // Output: [25, 10, 10, 1, 1]
