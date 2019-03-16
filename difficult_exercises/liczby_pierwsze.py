def has_not_divider(i):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            return False
    return True


def sito(n):
    """Sito Eratostenesa - liczby pierwsze"""
    L = [0] + n * [1]
    p = 2
    q = p * p
    while q <= n:
        if L[p] == 1:  # liczba pierwsza
            i = q
            while i <= n:  # wyrzucam p*p, p*(p+1), p*(p+2),...
                L[i] = 0
                i = i + p
        p = p + 1
        q = p * p
    M = []
    for i in range(1, n + 1):
        if L[i] == 1:
            M.append(i)
    return M


if __name__ == "__main__":
    n = 100
    result = []
    for i in range(2, n):
        if has_not_divider(i):
            result.append(i)
    print(result)
    print(sito(50))
