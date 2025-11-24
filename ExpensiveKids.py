# Allow User to add expenses
expenses = []

# Initialize categories
categories = ["KIDS", "HOUSEHOLD"]

# Main program loop
running = True

while running:
    # Display menu
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View totals")
    print("4. Exit")

    choice = input("\nEnter choice: ").strip()

    # Add expense
    if choice == "1":
        description = input("\nEnter description: ").strip()

        if not description:
            print("Description cannot be empty!")
            continue

        try:
            amount = float(input("Enter amount: $").replace('$', ''))

            if amount <= 1:
                print("Amount must be positive!")
                continue
        except ValueError:
            print("Invalid amount!")
            continue

        print("\n1. KIDS")
        print("2. HOUSEHOLD")

        try:
            cat_choice = int(input("Select category (1 or 2): "))

            if cat_choice not in [1, 2]:
                print("Must be 1 or 2!")
                continue
        except ValueError:
            print("Invalid input!")
            continue

        category = categories[cat_choice - 1]

        expenses.append({
            "description": description,
            "amount": amount,
            "category": category
        })

        print(f"\nAdded: {description} - ${amount:.2f} ({category})")

    # View expenses
    elif choice == "2":
        if not expenses:
            print("\nNo expenses recorded.")
        else:
            print("\n--- ALL EXPENSES ---")
            for expense in expenses:
                print(f"{expense['description']} - ${expense['amount']:.2f} ({expense['category']})")

    # View totals
    elif choice == "3":
        if not expenses:
            print("\nNo expenses recorded.")
        else:
            print("\n--- TOTALS ---")

            kids_total = sum(e['amount'] for e in expenses if e['category'] == 'KIDS')
            household_total = sum(e['amount'] for e in expenses if e['category'] == 'HOUSEHOLD')
            total = kids_total + household_total

            print(f"KIDS: ${kids_total:.2f}")
            print(f"HOUSEHOLD: ${household_total:.2f}")
            print(f"TOTAL: ${total:.2f}")

    # Exit
    elif choice == "4":
        print("\nGoodbye!")
        running = False

    else:
        print("Invalid choice!")