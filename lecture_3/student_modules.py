from typing import List, Dict, Callable, TypedDict


class Student(TypedDict):
    """Represents a student entry with a name and a list of grades."""
    name: str
    grades: List[int]


# A list containing all student records.
students: List[Student] = []


def add_name() -> None:
    """
    Ask the user to input a new student's name and add it to the student list.

    - Ensures the name contains only alphabetic characters.
    - Prevents adding duplicate names.
    """
    while True:
        name_student: str = input("Enter student name: ").strip().title()

        # Validate that the name contains only letters
        if not name_student.isalpha():
            print("Please enter a valid student name!")
            continue

        # Prevent duplicate student names
        if any(s["name"] == name_student for s in students):
            print("This name already exists!")
            continue

        # Add the new student
        students.append({"name": name_student, "grades": []})
        break


def add_grades() -> None:
    """
    Add one or multiple grades to an existing student.

    - Prompts the user to select a student.
    - Validates grade input (0–100).
    - Allows entering multiple grades until 'done' is typed.
    """
    if not students:
        print("No students added!")
        return

    # Find the student by name
    while True:
        name_student: str = input("Enter student name: ").strip().title()

        if name_student.isalpha():
            student: Student | None = next(
                (i for i in students if i["name"] == name_student),
                None
            )
            if not student:
                print("Student not found! Please try again!")
            else:
                break
        else:
            print("Invalid input! Please enter name.")

    # Enter grades
    while True:
        grade: str = input(
            "Enter grade (or 'done' to finish): "
        ).strip().lower()

        if grade == "done":
            break

        try:
            grade_value: int = int(grade)

            # Check grade limits
            if not (0 <= grade_value <= 100):
                print("Invalid input! Please enter a grade from 0 to 100.")
                continue

            student["grades"].append(grade_value)

        except ValueError:
            print("Invalid input! Please enter a number.")


def show_report() -> None:
    """
    Display a full report of all students and their average grades.

    - Shows each student's average.
    - Displays maximum, minimum, and overall average.
    - Handles cases where no grades exist.
    """
    average_all: List[float] = []

    if not students:
        print("No students!")
        return

    if all(len(s["grades"]) == 0 for s in students):
        print("No grade!")
        return

    # Print average grades for each student
    for student in students:
        average: float = sum(student["grades"]) / len(student["grades"])
        average_all.append(average)
        print(f"{student['name']}'s average grade is {round(average, 1)}")

    # Summary report
    print("------------------------")
    print(f"Max Average: {max(average_all):.1f}.")
    print(f"Min Average: {min(average_all):.1f}.")
    print(f"Overall Average: {sum(average_all) / len(average_all):.1f}.")


def best_student() -> None:
    """
    Determine and display the student with the highest average grade.

    - Skips students with no grades.
    - Prints the best student and their average.
    """
    if not students:
        print("No students!")
        return

    # Filter students who have at least one grade
    clean_list: List[Student] = [s for s in students if s["grades"]]

    if not clean_list:
        print("No students with grade!")
        return

    # Select the student with the highest average
    best: Student = max(
        clean_list,
        key=lambda s: sum(s["grades"]) / len(s["grades"])
    )

    avg: float = round(
        sum(best["grades"]) / len(best["grades"]),
        1
    )

    print(
        f"The student with highest average is {best['name']} "
        f"with a grade of {avg:.1f}."
    )


def main() -> None:
    """
    Main program loop.

    Displays a menu and executes user-selected operations until the user exits.
    """
    actions: Dict[str, Callable[[], None]] = {
        "1": add_name,
        "2": add_grades,
        "3": show_report,
        "4": best_student,
    }

    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit")

        try:
            choice: str = input("Enter your choice: ").strip()

            if choice == "5":
                print("Exiting program.")
                break

            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice! Please try again.")

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()
