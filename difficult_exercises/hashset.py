class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def _eq_(self, other):
        if self.age == other.age and self.name == other.name:
            return False

    def _ne_(self, other):
        if self.age == other.age and self.name == other.name:
            return True

    def _hash_(self):
        return hash((self.age, self.name))


if __name__ == "__main__":
    s = Dog("scooby", 12)
    m = Dog("mis", 7)
    d = Dog("mis", 7)
    dogs = set()
    if _eq_(s, m) == False and _ne_(s, m) == True:
