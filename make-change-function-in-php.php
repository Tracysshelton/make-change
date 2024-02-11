function makeChange($amount, $denominations) {
    // Sort the denominations in descending order
    rsort($denominations);
    
    // Initialize an array to store the count of each denomination
    $change = array();
    
    // Iterate through each denomination
    foreach ($denominations as $coin) {
        // Calculate how many coins of this denomination can be used
        $count = intval($amount / $coin);
        
        // Update the amount and store the count of coins used
        $amount -= $count * $coin;
        $change[$coin] = $count;
    }
    
    // Return the change
    return $change;
}

// Example usage
$amount = 87;
$denominations = array(25, 10, 5, 1);
$result = makeChange($amount, $denominations);
echo "Change for $amount cents: \n";
foreach ($result as $coin => $count) {
    echo "$count coin(s) of $coin cents\n";
}
