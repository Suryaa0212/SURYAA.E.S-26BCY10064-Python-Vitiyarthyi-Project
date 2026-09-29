"""
Student Grade Management System
--------------------------------
A small menu-driven project that ties together:
  - def functions (one job each)
  - a dictionary as the main data store
  - loops, conditionals, string formatting
  - type conversion (input() always returns a string)

Data structure:
    students = {
        "101": {"name": "Sam", "marks": [80, 90, 70]},
        "102": {"name": "Asha", "marks": [95, 88, 92]},
    }
Roll number is the dictionary KEY. Each VALUE is itself a dictionary
holding the student's name and a list of marks (nested dictionaries).
"""

# The dictionary that stores every student's record.
students = {}


def add_student():
    """Ask for a roll number and name, and create a new record."""
    roll = input("Enter roll number: ").strip()

    if roll in students:
        print(f"Roll number {roll} already exists.\n")
        return

    name = input("Enter student name: ").strip()
    students[roll] = {"name": name, "marks": []}
    print(f"Added student {name} (roll {roll}).\n")


def add_marks():
    """Add one mark to an existing student's mark list."""
    roll = input("Enter roll number: ").strip()

    if roll not in students:
        print("No student with that roll number.\n")
        return

    mark_text = input("Enter a mark to add (0-100): ").strip()
    try:
        mark = float(mark_text)   # explicit type conversion: str -> float
    except ValueError:
        print("That is not a valid number.\n")
        return

    students[roll]["marks"].append(mark)
    print(f"Added mark {mark} for {students[roll]['name']}.\n")


def calculate_average(marks):
    """Return the average of a list of marks, or 0 if the list is empty."""
    if not marks:
        return 0
    return sum(marks) / len(marks)


def grade_from_average(average):
    """Convert a numeric average into a letter grade."""
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def view_student(roll):
    """Print one student's full record, including average and grade."""
    record = students[roll]
    average = calculate_average(record["marks"])
    grade = grade_from_average(average)

    print(f"Roll No : {roll}")
    print(f"Name    : {record['name']}")
    print(f"Marks   : {record['marks']}")
    print(f"Average : {average:.2f}")
    print(f"Grade   : {grade}\n")


def search_student():
    """Look up one student by roll number."""
    roll = input("Enter roll number to search: ").strip()

    if roll not in students:
        print("No student with that roll number.\n")
        return

    view_student(roll)


def view_all():
    """Print every student's record, sorted by roll number."""
    if not students:
        print("No students recorded yet.\n")
        return

    for roll in sorted(students):
        view_student(roll)


def delete_student():
    """Remove a student's record entirely."""
    roll = input("Enter roll number to delete: ").strip()

    if roll not in students:
        print("No student with that roll number.\n")
        return

    removed = students.pop(roll)
    print(f"Removed {removed['name']} (roll {roll}).\n")


def class_average():
    """Print the average of every student's average (an overall class score)."""
    if not students:
        print("No students recorded yet.\n")
        return

    averages = [calculate_average(rec["marks"]) for rec in students.values()]
    overall = sum(averages) / len(averages)
    print(f"Class average across {len(students)} student(s): {overall:.2f}\n")


def show_menu():
    """Display the menu of available actions."""
    print("=" * 40)
    print("STUDENT GRADE MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add student")
    print("2. Add a mark to a student")
    print("3. Search for a student")
    print("4. View all students")
    print("5. Delete a student")
    print("6. Show class average")
    print("7. Exit")


def main():
    """Run the menu loop until the user chooses to exit."""
    # A dictionary used to map each menu choice to the function that handles it.
    actions = {
        "1": add_student,
        "2": add_marks,
        "3": search_student,
        "4": view_all,
        "5": delete_student,
        "6": class_average,
    }

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break
        elif choice in actions:
            actions[choice]()      # call the matching function
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
