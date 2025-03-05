import math

def find_factors(n):
    """
    This function demonstrates three different approaches to finding factors of a number.
    """

    # Approach 1: Brute Force Method (O(N))
    def brute_force(n):
        """Check all numbers from 1 to N"""
        result = []
        for i in range(1, n + 1):  # Iterate from 1 to N
            if n % i == 0:  # If i divides n completely
                result.append(i)
        return result

    # Approach 2: Optimized Method (O(N/2) ≈ O(N))
    def optimized(n):
        """Check only up to N/2, since no number > N/2 (except N) can be a factor"""
        result = []
        for i in range(1, (n // 2) + 1):  # Iterate from 1 to N/2
            if n % i == 0:
                result.append(i)
        result.append(n)  # Adding N itself (since N is always a factor)
        return result

    # Approach 3: Most Optimal Method (O(√N))
    def optimal(n):
        """Iterate only up to sqrt(N) and find both factors together"""
        result = set()  # Using a set to avoid duplicates
        for i in range(1, int(math.sqrt(n)) + 1):  # Iterate only up to sqrt(N)
            if n % i == 0:
                result.add(i)       # Add smaller factor
                result.add(n // i)  # Add corresponding larger factor
        return sorted(result)  # Sorting for clarity

    # Running all approaches
    brute_result = brute_force(n)
    optimized_result = optimized(n)
    optimal_result = optimal(n)

    # Printing results
    print(f"Factors of {n} using Brute Force (O(N)): {brute_result}")
    print(f"Factors of {n} using Optimized (O(N/2)): {optimized_result}")
    print(f"Factors of {n} using Optimal (O(√N)): {optimal_result}")

# Example Usage
num = 36  # Change this number to test different cases
find_factors(num)
