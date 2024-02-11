def make_change(amount, coins):
    """
    Make change for a given amount using a greedy algorithm.

    Args:
    - amount: The amount for which to make change
    - coins: A list of coin denominations available

    Returns:
    - A dictionary where keys are coin denominations and values are the number of coins used
    """

    # Sort the coins in descending order
    coins.sort(reverse=True)

    # Initialize a dictionary to store the result
    change = {}

    # Iterate through each coin denomination
    for coin in coins:
        # Calculate how many coins of this denomination can be used
        num_coins = amount // coin
        # Update the amount remaining
        amount -= num_coins * coin
        # Update the change dictionary
        change[coin] = num_coins

    return change

# Example usage:
amount = 76
coins = [25, 10, 5, 1]
print("Change for", amount, "using coins", coins, ":")
print(make_change(amount, coins))
