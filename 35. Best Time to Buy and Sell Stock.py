def max_profit_brute_force(prices):
    """
    Brute Force Approach: O(n^2) Time, O(1) Space
    This approach checks every possible pair of buy and sell days.
    """
    max_profit = 0
    n = len(prices)

    for i in range(n):
        for j in range(i + 1, n):  # Ensure j > i (buy before sell)
            if prices[j] > prices[i]:  
                max_profit = max(prices[j] - prices[i], max_profit)  

    return max_profit

def max_profit_optimized(prices):
    """
    Optimized Approach: O(n) Time, O(1) Space
    Uses a single pass to keep track of the minimum price and maximum profit.
    """
    max_profit = 0
    min_price = float("inf")

    for price in prices:
        min_price = min(min_price, price)  # Track lowest price seen so far
        max_profit = max(max_profit, price - min_price)  # Max profit if selling today

    return max_profit

# Example Usage
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

print("Brute Force Output for prices1:", max_profit_brute_force(prices1))  # Expected: 5
print("Optimized Output for prices1:", max_profit_optimized(prices1))  # Expected: 5

print("Brute Force Output for prices2:", max_profit_brute_force(prices2))  # Expected: 0
print("Optimized Output for prices2:", max_profit_optimized(prices2))  # Expected: 0
