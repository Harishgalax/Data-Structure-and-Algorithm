def fractional_knapsack(items, capacity):
    # Sort items based on value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    current_capacity = capacity

    for item in items:
        if current_capacity >= item[1]:
            # If the whole item can be added to the knapsack
            total_value += item[0]
            current_capacity -= item[1]
        else:
            # Add a fraction of the item to fill the knapsack
            fraction = current_capacity / item[1]
            total_value += item[0] * fraction
            break

    return total_value

# Example usage:
items1 = [[60, 10], [100, 20], [120, 30]]
capacity1 = 50
result1 = fractional_knapsack(items1, capacity1)
print("Output 1:", result1)

items2 = [[500, 30]]
capacity2 = 10
result2 = fractional_knapsack(items2, capacity2)
print("Output 2:", result2)
