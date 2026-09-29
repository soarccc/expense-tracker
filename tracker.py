def add_expense(expenses):
    pass  # TODO

def list_expenses(expenses):
    pass  # TODO

def main():
    expenses = []
    while True:
        print("\n1. Add expense\n2. List expenses\n3. Quit")
        choice = input("Choose: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()