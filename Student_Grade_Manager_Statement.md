# Project Statement

## Problem Statement

Teachers and students who track marks by hand, or with separate variables for
each student, run into the same problems as a class grows: there is no quick
way to look up one student's record, calculate an average and letter grade
consistently, or get an overall class figure without repeating the same
calculation for every entry. A single typo or a forgotten mark is easy to
miss, and nothing stops two students from accidentally sharing a roll number.

The Student Grade Management System addresses this with a small, menu-driven
command-line program that stores every student's data in one place and
performs the repetitive parts — averaging, grading, and reporting —
automatically and consistently.

## Objectives

- Design the program around a single dictionary (`students`) that holds every
  record, keyed by roll number, with each value itself a dictionary of name
  and marks.
- Build one function per action — adding a student, adding a mark, searching,
  viewing all records, deleting a record, and computing the class average —
  so each piece of logic has a single, clear responsibility.
- Convert a list of marks into a numeric average and a letter grade (A–F)
  using a fixed, documented grading scale.
- Validate input where it matters most: reject a mark that cannot be
  converted to a number, and refuse to add a student whose roll number
  already exists, rather than overwriting data or crashing.
- Provide a repeating, numbered menu for an interactive session that runs
  until the user chooses to exit.

## Scope of the Project

### Functional Scope

- **Student records:** Add a new student with a roll number and name;
  refuse duplicate roll numbers; delete an existing record.
- **Marks and grading:** Add one mark at a time to a student's record;
  calculate the average of a student's marks; convert that average into a
  letter grade using fixed thresholds (90 / 75 / 60 / 40).
- **Lookup and reporting:** Search for one student by roll number; view
  every student's record sorted by roll number; calculate the class-wide
  average across all students.
- **Interactive menu:** Present a numbered menu of all seven actions, repeat
  it after every action, and exit cleanly on the user's request.

### Non-Functional Scope

- **Performance:** All records are kept in memory, so lookups, additions,
  and deletions are effectively instantaneous for a class-sized roster.
- **Portability:** Uses only the Python standard library, so it runs on any
  system with Python 3 installed.
- **No external dependencies:** Self-contained in a single script with no
  third-party packages.
- **Usability:** Short, explicit prompts and menu text so a first-time user
  can operate the program without reading documentation.
- **Reliability:** Invalid numeric input and unknown roll numbers are caught
  and reported, instead of stopping the program with an unhandled error.

## Target Audience

- Students learning core Python concepts — functions, dictionaries, input
  validation, and string formatting — through a single working project.
- Teachers or tutors who want a lightweight way to track a small class's
  marks without setting up a spreadsheet or database.
- Anyone who wants a simple, dependency-free command-line tool for
  recording and averaging a short list of numeric records.
