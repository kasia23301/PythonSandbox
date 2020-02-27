def solution_1(a):
    l = []
    for i in str(a):
        l.append(int(i))
    l.reverse()
    return l


def solution_2(a):
    l = []
    if a == 0:
        l.append(a)
        return l
    while a > 0:
        x = a % 10
        l.append(x)
        a = a // 10
    return l


if __name__ == "__main__":
    a = input("Podaj liczbe: ")
    print(solution_1(a))
    print(solution_2(int(a)))
