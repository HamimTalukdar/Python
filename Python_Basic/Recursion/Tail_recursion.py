def factorial_tail_recursive(n, acc=1):
    # Base case
    if n == 0 or n == 1:
        return acc
    # Tail-recursive case
    else:
        return factorial_tail_recursive(n - 1, n * acc)

result = factorial_tail_recursive(5)
print(result)  # Output: 120
