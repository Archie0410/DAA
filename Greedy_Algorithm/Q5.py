def fractional_knapsack(values, weights, capacity):
    N = len(values)
    items = [[weights[i], values[i]] for i in range(N)]
    items.sort(reverse=True, key=lambda x: x[1] / x[0])
    total_value = 0.0
    current_weight = 0
    for item in items:
        weight, value = item[0], item[1]
        if current_weight + weight <= capacity:
            total_value += value
            current_weight += weight
        else:
            remaining_weight = capacity - current_weight
            total_value += value * (remaining_weight / weight)
            break
    return total_value

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(fractional_knapsack(values, weights, capacity))