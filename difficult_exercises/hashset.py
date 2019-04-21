class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.age, self.name))

    def __str__(self):
        return "name: " + s.name + " age: " + str(s.age)

    def length_of_beard(self):
        print('Dog')
        return -1


class Wyzel(Dog):
    def length_of_beard(self):
        print('Wyzel')
        return 10


class Sznaucer(Dog):
    def length_of_beard(self):
        print('Sznaucer')
        return 30


if __name__ == "__main__":
    s = Dog("scooby", 12)
    m = Dog("mis", 7)
    d = Dog("mis", 7)
    e = Wyzel("wy", 8)
    f = Sznaucer("sz", 9)
    dogs = set()
    dogs.add(s)
    dogs.add(m)
    dogs.add(d)
    dogs.add(e)
    dogs.add(f)
    for dog in dogs:
        print(dog.length_of_beard())
