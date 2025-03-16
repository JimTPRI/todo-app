from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

todos = []

while True:
    user_action: str = input("Type add, show, edit, complete, or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:] + "\n"
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            print(f"{index +1}:{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1
            todos = functions.get_todos()
            if len(todos) > number >= 0:
                new_todo = input("Enter the todo:") + "\n"
                todos[number] = new_todo
                functions.write_todos(todos)
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) - 1
            todos = functions.get_todos()
            if len(todos) > number >= 0:
                completed = todos.pop(number)
                functions.write_todos(todos)
                print(f"Todo \"{completed.strip()}\" was removed from the list.")
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid input")

print("Bye!")
