def fibonacci_sequence(n):
    fibonacci_numbers = []
    for i in range(0, n):
        fibonacci_len = len(fibonacci_numbers)
        if fibonacci_len < 2:
            fibonacci_numbers.append(1)
        else:
            fibonacci_numbers.append(fibonacci_numbers[fibonacci_len - 1] + fibonacci_numbers[fibonacci_len - 2])
    return fibonacci_numbers


if __name__ == "__main__":
    print(fibonacci_sequence(100))
