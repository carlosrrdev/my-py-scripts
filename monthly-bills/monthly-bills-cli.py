#!/usr/bin/env python3

import os
import platform
import subprocess
import datetime


def get_desktop_path():
    """Return the path to the user's desktop."""
    return os.path.join(os.path.expanduser("~"), "Desktop")


def open_file(file_path):
    """Open the file with the default application based on OS."""
    if platform.system() == 'Darwin':  # macOS
        subprocess.call(('open', file_path))
    elif platform.system() == 'Windows':  # Windows
        os.startfile(file_path)
    else:
        subprocess.call(('xdg-open', file_path))


def main():
    bills = {}

    print("Enter bills and their amounts (enter 'done' when finished):")
    while True:
        bill_name = input("Enter bill name (or 'done' to finish): ")
        if bill_name.lower() == 'done':
            break

        while True:
            try:
                bill_amount = float(input(f"Enter amount for {bill_name}: $"))
                if bill_amount <= 0:
                    print("Amount must be greater than 0. Please try again.")
                    continue
                bills[bill_name] = bill_amount
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")

    if not bills:
        print("No bills entered. Exiting.")
        return

    people = []
    print("\nEnter names of people (enter 'done' when finished):")
    while True:
        person_name = input("Enter person's name (or 'done' to finish): ")
        if person_name.lower() == 'done':
            break
        people.append(person_name)

    if not people:
        print("No people entered. Exiting.")
        return

    contributions = {person: {} for person in people}

    print("\nAssign people to bills:")
    for bill_name, bill_amount in bills.items():
        print(f"\nBill: {bill_name} (${bill_amount:.2f})")
        contributors = []

        for person in people:
            while True:
                response = input(f"Is {person} contributing to {bill_name}? (yes/no): ").lower()
                if response in ['yes', 'y', 'no', 'n']:
                    if response in ['yes', 'y']:
                        contributors.append(person)
                    break
                else:
                    print("Please enter 'yes' or 'no'.")

        if contributors:
            share = bill_amount / len(contributors)
            for person in contributors:
                contributions[person][bill_name] = share
        else:
            print(f"No one is contributing to {bill_name}.")

    totals = {person: sum(bills.values()) for person, bills in contributions.items()}

    report = []
    current_month = datetime.datetime.now().strftime("%B")
    report.append(f"BILL SPLITTING REPORT - {current_month}")
    report.append("=" * 50)

    report.append("\nBILLS:")
    for bill_name, amount in bills.items():
        report.append(f"{bill_name}: ${amount:.2f}")

    report.append("\nCONTRIBUTIONS PER PERSON:")
    for person, person_bills in contributions.items():
        report.append(f"\n{person}:")
        if person_bills:
            for bill_name, amount in person_bills.items():
                report.append(f"  {bill_name}: ${amount:.2f}")
            report.append(f"TOTAL: ${totals[person]:.2f}")
        else:
            report.append("No contributions")

    desktop_path = get_desktop_path()
    file_path = os.path.join(desktop_path, f"bill_{current_month}.txt")

    with open(file_path, 'w') as f:
        f.write('\n'.join(report))

    print(f"\nReport saved to {file_path}")

    open_file(file_path)


if __name__ == "__main__":
    main()
