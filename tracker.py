import datetime


def add_expense(expenses):
    date = datetime.datetime.now(tz=datetime.timezone.utc).date().isoformat()
    amount = int(input("Enter the amount: "))
    category = input("Enter the category: ")
    desc = input("Description: ")

    expense = {
        "Date": date,
        "Amount": amount,
        "Category": category,
        "Description": desc,
    }
    expenses.append(expense)


def list_expenses(expenses):
    print(expenses)

    
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