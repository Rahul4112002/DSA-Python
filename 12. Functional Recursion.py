# Parameterized Recursion
def parameterized_sum(n, i=1, summation=0):
    if i > n:
        print("Sum:", summation)
        return
    parameterized_sum(n, i + 1, summation + i)

# Functional Recursion
def functional_sum(n):
    if n == 1:
        return 1
    return n + functional_sum(n - 1)

if __name__ == "__main__":
    n = int(input("Enter a number: "))

    print("\nUsing Parameterized Recursion:")
    parameterized_sum(n)

    print("\nUsing Functional Recursion:")
    print("Sum:", functional_sum(n))
