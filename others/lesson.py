# class Osoba:
#     def __init__(self, name, surname, age, year_of_birth, stupid_level):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.year_of_birth = year_of_birth
#         self.stupid_level = stupid_level
#
#
# # def return_pair():
# #     return "Mateusz", "Bedkowski", 21, 1996, 0.9
#
#
# if __name__ == "__main__":
#     osoba1 = Osoba("Mateusz","Bedkowski", 21, 1996, 0.9)
#     osoba2 = Osoba("Kasia","Bedkowska", 17, 2001, 0.8)
#     print(osoba1.name)
#     print(osoba1.age)
#     print(osoba2.stupid_level)
class Node:
    def __init__(self, value, next__node):
        self.value = value
        self.next_node = next__node


if __name__ == "__main__":
    list_of_elements = Node(12, Node(23, Node(43, Node("moj string", None))))
    current_elem = list_of_elements
    while True:
        print(current_elem.value)
        current_elem = current_elem.next_node
        if current_elem is None:
            break
