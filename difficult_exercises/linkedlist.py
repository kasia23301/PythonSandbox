class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            next = self.head
            while next.next is not None:
                next = next.next
            next.next = Node(val)

    def length(self):
        counter = 0
        if self.head is not None:
            counter += 1
            next = self.head
            while next.next is not None:
                next = next.next
                counter += 1
        return counter

    def __str__(self):
        list = "["
        if self.head is not None:
            list += str(self.head.val)
            next = self.head
            while next.next is not None:
                list += ","
                list += str(next.next.val)
                next = next.next
        list += "]"
        return str(list)


if __name__ == "__main__":
    list1 = LinkedList()
    list1.append("1")
    list1.append("2")
    list1.append("3")
    list1.append("4")
    print(list1.length())
    print(list1)

