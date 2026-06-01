class Habit:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def status(self):
        if self.completed:
            return "Completed"
        else:
            return "Pending"


# Default habits
habits = [
    Habit("Drink 2L Water"),
    Habit("Exercise 30 Minutes"),
    Habit("Read 20 Pages"),
    Habit("Practice Coding")
]


def add_habit():
    name = input("Enter habit name: ")
    habit = Habit(name)
    habits.append(habit)
    print("Habit added successfully!")


def view_habits():
    if len(habits) == 0:
        print("No habits available.")
    else:
        print("\nYour Habits:")
        for i, habit in enumerate(habits, start=1):
            print(f"{i}. {habit.name} - {habit.status()}")


def complete_habit():
    view_habits()

    if len(habits) == 0:
        return

    choice = int(input("Enter habit number to mark completed: "))

    if 1 <= choice <= len(habits):
        habits[choice - 1].mark_completed()
        print("Habit marked as completed!")
    else:
        print("Invalid choice!")


def show_progress():
    if len(habits) == 0:
        print("No habits available.")
        return

    completed = 0

    for habit in habits:
        if habit.completed:
            completed += 1

    progress = (completed / len(habits)) * 100

    print(f"\nProgress: {progress:.2f}%")
    print(f"Completed: {completed}/{len(habits)}")

    if progress == 100:
        print("Excellent! All habits completed today! 🎉")
    elif progress >= 75:
        print("Amazing work! You're very consistent! 🔥")
    elif progress >= 50:
        print("Good progress! Keep pushing! 💪")
    elif progress > 0:
        print("Nice start! Keep building momentum! 🚀")
    else:
        print("Let's get started. Every small step counts! ✨")


def delete_habit():
    view_habits()

    if len(habits) == 0:
        return

    choice = int(input("Enter habit number to delete: "))

    if 1 <= choice <= len(habits):
        removed = habits.pop(choice - 1)
        print(f"{removed.name} deleted successfully!")
    else:
        print("Invalid choice!")


while True:
    print("\n===== SMART HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Mark Habit Completed")
    print("4. Show Progress")
    print("5. Delete Habit")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_habit()

    elif choice == 2:
        view_habits()

    elif choice == 3:
        complete_habit()

    elif choice == 4:
        show_progress()

    elif choice == 5:
        delete_habit()

    elif choice == 6:
        print("Thank you for using Smart Habit Tracker!")
        break

    else:
        print("Invalid choice! Please try again.") 