class CustomerNode:
    def __init__(self, name):
        self.name = name
        self.next = None


class Waitlist:
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_customer = CustomerNode(name)
        new_customer.next = self.head
        self.head = new_customer

    def add_end(self, name):
        new_customer = CustomerNode(name)

        if self.head is None:
            self.head = new_customer
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_customer

    def remove_customer(self, name):
        if self.head is None:
            print("The waitlist is empty.")
            return

        if self.head.name.lower() == name.lower():
            self.head = self.head.next
            print(name, "was removed from the waitlist.")
            return

        current = self.head

        while current.next is not None:
            if current.next.name.lower() == name.lower():
                current.next = current.next.next
                print(name, "was removed from the waitlist.")
                return

            current = current.next

        print(name, "was not found on the waitlist.")

    def print_waitlist(self):
        if self.head is None:
            print("The waitlist is empty.")
            return

        current = self.head
        position = 1

        print("\nCurrent Waitlist:")

        while current is not None:
            print(f"{position}. {current.name}")
            current = current.next
            position += 1