import sys
import json
from click import command

# Глобальные списки
tasks = []
tasks_in_progress = []
tasks_done = []

DATA_FILE = "tasks.json"

def load_data():
    global tasks, tasks_in_progress, tasks_done
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            tasks[:] = data.get("tasks", [])
            tasks_in_progress[:] = data.get("tasks_in_progress", [])
            tasks_done[:] = data.get("tasks_done", [])
    except FileNotFoundError:
        tasks[:] = []
        tasks_in_progress[:] = []
        tasks_done[:] = []


def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "tasks": tasks,
            "tasks_in_progress": tasks_in_progress,
            "tasks_done": tasks_done
        }, f, ensure_ascii=False, indent=4)


def add_task(name: str):
    """
    Добавляет задание в список неотсортированных заданий.
    """
    tasks.append(name)
    print(name)
    print(f'Задание успешно добавлено! (ID:{len(tasks)-1})\n')
    save_data()

def show_tasks():
    """
    Выводит список неотсортированных заданий.
    """
    print("Список заданий, которые нужно выполнить:")
    for i, task in enumerate(tasks):
        print(f"ID {i}: {task}")
    print("\n")

def show_tasks_done():
    """
    Выводит список выполненных заданий.
    """
    print("Список выполненных заданий:")
    for i, task in enumerate(tasks_done):
        print(f"ID {i}: {task}")
    print("\n")

def show_tasks_in_progress():
    """
    Выводит список заданий в процессе выполнения.
    """
    print("Список заданий в процессе выполнения:")
    for i, task in enumerate(tasks_in_progress):
        print(f"ID {i}: {task}")
    print("\n")

def mark_in_progress(index: int):
    """
    Добавляет задачу в список взятых в выполнение.
    """
    if 0 <= index < len(tasks):
        tasks_in_progress.append(tasks.pop(index))
        print(f'Задание под индексом {index} взято на выполнение!\n')
    else:
        print("Неверный индекс!")
    save_data()

def mark_done(index: int):
    """
    Добавляет задачу в список выполненых.
    """
    if 0 <= index < len(tasks_in_progress):
        tasks_done.append(tasks_in_progress.pop(index))
        print(f'Задание под номером {index} выполнено!\n')
    else:
        print("Неверный индекс!")
    save_data()

def update_task(index: int, task: str):
    """
    Обновляет задачу в неотсортированном списке заданий по индексу.
    """
    if 0 <= index < len(tasks):
        tasks[index] = task
        print(f'Задание под номером {index} обновлено!\n')
    else:
        print("Неверный индекс!")
    save_data()

def delete_task(index: int):
    """
    Удаляет задачу по указанному индексу.
    """
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print(f'Задание под номером {index} удалено!\n')
    else:
        print("Неверный индекс!")
    save_data()

def help():
    print("""
Доступные команды:
  add "название"          — добавить задачу
  show                    — показать все задачи
  progress <индекс>       — отметить как в работе
  done <индекс>           — отметить как выполнено
  show-progress           — показать задачи в работе
  show-done               — показать выполненные
  update <индекс> "новое" — обновить задачу
  delete <индекс>         — удалить задачу
  help                    — показать помощь
""")


def main():
    load_data()
    if len(sys.argv) < 2:
        print("Используйте 'help', чтобы посмотреть команды")
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "add":
        if len(args) == 1:
            add_task(args[0])
        else:
            print("Использование: add \"название задачи\"")
    elif command == "show":
        show_tasks()
    elif command == "show-progress":
        show_tasks_in_progress()
    elif command == "show-done":
        show_tasks_done()
    elif command == "progress":
        if len(args) == 1:
            try:
                index = int(args[0])
                mark_in_progress(index)
            except ValueError:
                print("Индекс должен быть числом.")
        else:
            print("Использование: progress <индекс>")
    elif command == "done":
        if len(args) == 1:
            try:
                index = int(args[0])
                mark_done(index)
            except ValueError:
                print("Индекс должен быть числом.")
        else:
            print("Использование: done <индекс>")
    elif command == "update":
        if len(args) == 2:
            try:
                index = int(args[0])
                new_name = args[1]
                update_task(index, new_name)
            except ValueError:
                print("Индекс должен быть числом.")
        else:
            print("Использование: update <индекс> \"новое название\"")
    elif command == "delete":
        if len(args) == 1:
            try:
                index = int(args[0])
                delete_task(index)
            except ValueError:
                print("Индекс должен быть числом.")
        else:
            print("Использование: delete <индекс>")
    elif command == "help":
        help()
    else:
        print(f"Неизвестная команда: {command}")
        help()

if __name__ == "__main__":
    main()