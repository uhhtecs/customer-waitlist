from waitlist import Waitlist


def main():
    waitlist = Waitlist()

    while True:
        print("\n--- Customer Waitlist ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            waitlist.add_front(name)
            print(name, "was added to the front.")

        elif choice == "2":
            name = input("Enter customer name: ")
            waitlist.add_end(name)
            print(name, "was added to the end.")

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove_customer(name)

        elif choice == "4":
            waitlist.print_waitlist()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()