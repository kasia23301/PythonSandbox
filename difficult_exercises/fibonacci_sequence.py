def fibonacci_sequence(n):
    fibonacci_numbers = []
    for i in range(0, n):
        fibonacci_len = len(fibonacci_numbers)
        if fibonacci_len < 2:
            fibonacci_numbers.append(1)
        else:
            fibonacci_numbers.append(fibonacci_numbers[fibonacci_len - 1] + fibonacci_numbers[fibonacci_len - 2])
    return fibonacci_numbers


def fibonacci_recursion(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib_list = fibonacci_recursion(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list


if __name__ == "__main__":
    print(fibonacci_sequence(100))
    print(fibonacci_recursion(10))
