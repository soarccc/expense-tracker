import datetime
import json

def add_expense(expenses):
    date = datetime.datetime.now(tz=datetime.timezone.utc).date().isoformat()
    amount = float(input("Enter the amount: "))
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

def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=2)


def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add expense\n2. List expenses\n3. Quit")
        choice = input("Choose: ")
        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()