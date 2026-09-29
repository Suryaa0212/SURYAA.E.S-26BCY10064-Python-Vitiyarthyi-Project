# Student Grade Management System

A small Python console program for recording student marks, calculating
averages and letter grades, and managing a class roster from a repeating
text menu. Every student is stored in one dictionary, keyed by roll number,
so the program stays a single, self-contained script with no external
dependencies.

## Features

- Adds a new student with a roll number and name, refusing duplicate roll
  numbers instead of overwriting an existing record.
- Adds marks to an existing student one at a time, validating that each
  entry is a real number before storing it.
- Calculates each student's average and converts it into a letter grade
  (A–F) using a fixed grading scale.
- Looks up one student by roll number, or lists every student sorted by
  roll number.
- Deletes a student's record entirely.
- Calculates the class-wide average across every student's individual
  average.
- Runs entirely offline with no third-party packages.

## Menu Options

The program is driven by a numbered menu that repeats after every action:

| Option | Action | Description |
| --- | --- | --- |
| 1 | Add student | Create a new record from a roll number and name |
| 2 | Add a mark | Append one mark to an existing student's record |
| 3 | Search for a student | Look up and display one record by roll number |
| 4 | View all students | Display every record, sorted by roll number |
| 5 | Delete a student | Remove a record entirely |
| 6 | Show class average | Average of every student's individual average |
| 7 | Exit | End the program |

## Calculations

A student's average is calculated as:

```text
average = sum(marks) / len(marks)      # 0 if the student has no marks yet
```

That average is converted to a letter grade using fixed thresholds:

```text
average >= 90  ->  A
average >= 75  ->  B
average >= 60  ->  C
average >= 40  ->  D
average <  40  ->  F
```

The class average is the average of every student's individual average,
not a single average across every mark in the class:

```text
class average = sum(each student's average) / number of students
```

## Requirements

- Python 3
- No third-party packages — the standard library is enough

## Run

From the folder containing the script, run:

```bash
python student_grade_manager.py
```

Follow the on-screen menu, entering the number of the action you want
(1–7) and then the roll number, name, or mark it asks for.

## Project Structure

The program is organized around these functional areas:

- **Data store** — a single `students` dictionary, keyed by roll number,
  holding each student's name and list of marks.
- **Record functions** — `add_student()`, `add_marks()`,
  `delete_student()`: create, extend, or remove entries in the dictionary.
- **Calculation functions** — `calculate_average()`, `grade_from_average()`:
  pure functions that work on a list of marks or a number, independent of
  the dictionary itself.
- **Reporting functions** — `view_student()`, `search_student()`,
  `view_all()`, `class_average()`: read the dictionary and print formatted
  results.
- **Menu control** — `show_menu()`, `main()`: display the options, read the
  user's choice, and dispatch to the right function through a dictionary
  of actions.

## Interpreting Results

Each student's printout shows their roll number, name, full list of
marks, average (to two decimal places), and letter grade. The class
average summarizes overall performance but can hide a wide spread between
students — a student well below the class average will not stand out in
that single number, so check individual records if you need that detail.

## Troubleshooting

- **"Roll number ... already exists"** — you tried to add a student with a
  roll number already in use; delete the existing record first if you meant
  to replace it, or use a different roll number.
- **"That is not a valid number"** — the mark you entered for option 2
  could not be converted with `float()`; re-enter it using digits only
  (for example, `82` or `82.5`).
- **"No student with that roll number"** — the roll number you entered for
  search, add-marks, or delete does not exist yet; use option 4 to see the
  roll numbers currently on record.
- **"No students recorded yet"** — you chose option 4 or 6 before adding
  any students; add at least one student first.

## Scope

This project is intended for learning core Python concepts — functions,
dictionaries, input validation, and string formatting — in one small,
working program. Records exist only in memory for the current run and are
not saved to a file, so they are lost when the program exits.
