def calculate_min_coins(coins_list, amount):
    # Sort the list of coins in descending order
    sorted_coins = sorted(coins_list, reverse=True)

    # Initialize the result list with zeros
    result_list = [0] * len(sorted_coins)

    # Loop through each coin denomination
    for i in range(len(sorted_coins)):
        # Calculate the maximum number of coins of this denomination
        max_coins = amount // sorted_coins[i]

        # Add the maximum number of coins to the result list
        result_list[i] = max_coins

        # Update the remaining amount
        amount -= max_coins * sorted_coins[i]

    return result_list

coins_list = input("Enter the coin denominations (separated by commas): ")
coins_list = list(map(int, coins_list.split(",")))
amount = int(input("Enter the amount of change to be made: "))

# Calculate the minimum number of coins required
result_list = calculate_min_coins(coins_list, amount)

# Print the result
print("Minimum number of coins required:", result_list)
