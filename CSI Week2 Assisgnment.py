#Aryan Roy
#CSI Week 2 Assisgnment
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__ (self):
        self.head = None

    def add_node(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            print("Head added:", value)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new
            print("Node added:", value)

    def print_list(self):
        if self.head is None:
            print("List is Empty")
            return
        temp = self.head
        print("List:", end=" ")
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete_nth_node(self, n):
        if self.head is None:
            print("Error: List is empty")
            return

        if n <= 0:
            print("Invalid index")
            return

        if n == 1:
            print("Deleted:", self.head.data)
            self.head = self.head.next
            return

        count = 1
        temp = self.head
        prev = None
        while temp is not None and count < n:
            prev = temp
            temp = temp.next
            count += 1

        if temp is None:
            print("Index out of range")
            return

        print("Deleted:", temp.data)
        prev.next = temp.next


ll = Linkedlist()

while True:
    print("\n1. Add node")
    print("2. Print list")
    print("3. Delete nth node")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        try:
            val = int(input("Enter value to add: "))
            ll.add_node(val)
        except ValueError:
            print("Please enter a valid integer.")

    elif choice == '2':
        ll.print_list()

    elif choice == '3':
        try:
            pos = int(input("Enter index to delete (starting from 1): "))
            ll.delete_nth_node(pos)
        except ValueError:
            print("Please enter a valid integer.")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")
