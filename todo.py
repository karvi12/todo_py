import sys

from click import command

# Глобальные списки
tasks = []
tasks_in_progress = []
tasks_done = []

def add_task(name: str):
    """
    Добавляет задание в список неотсортированных заданий.
    """
    tasks.append(name)
    print(name)
    print(f'Задание успешно добавлено! (ID:{len(tasks)-1})\n')

def show_tasks():
    """
    Выводит список неотсортированных заданий.
    """
    print("Список заданий, которые нужно выполнить:")
    for i, task in enumerate(tasks):
        print(f"{i}: {task}")
    print("\n")

def show_tasks_done():
    """
    Выводит список выполненных заданий.
    """
    print("Список выполненных заданий:")
    for i, task in enumerate(tasks_done):
        print(f"{i}: {task}")
    print("\n")

def show_tasks_in_progress():
    """
    Выводит список заданий в процессе выполнения.
    """
    print("Список заданий в процессе выполнения:")
    for i, task in enumerate(tasks_in_progress):
        print(f"{i}: {task}")
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

def mark_done(index: int):
    """
    Добавляет задачу в список выполненых.
    """
    if 0 <= index < len(tasks_in_progress):
        tasks_done.append(tasks_in_progress.pop(index))
        print(f'Задание под номером {index} выполнено!\n')
    else:
        print("Неверный индекс!")

def update_task(index: int, task: str):
    """
    Обновляет задачу в неотсортированном списке заданий по индексу.
    """
    if 0 <= index < len(tasks):
        tasks[index] = task
        print(f'Задание под номером {index} обновлено!\n')
    else:
        print("Неверный индекс!")

def delete_task(index: int):
    """
    Удаляет задачу по указанному индексу.
    """
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print(f'Задание под номером {index} удалено!\n')
    else:
        print("Неверный индекс!")

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
    print("Добро пожаловать в мой ToDo!")
    help()

    while True:
        user_input = input(">").strip()

        if not user_input:
            continue

        parts = user_input.split(maxsplit=1)
        command = parts[0]
        args_str = parts[1] if len(parts) > 1 else ""

        if command == "exit":
            print("Выход из программы")
            break

        elif command == "add":
            add_task(args_str)
        elif command == "show":
            show_tasks()
        elif command == "show-progress":
            show_tasks_in_progress()
        elif command == "show-done":
            show_tasks_done()
        elif command == "progress":
            try:
                index = int(args_str)
                mark_in_progress(index)
            except ValueError:
                print("Индекс должен быть числом.")
        elif command == "done":
            try:
                index = int(args_str)
                mark_done(index)
            except ValueError:
                print("Индекс должен быть числом.")
        elif command == "update":
            args = args_str.split(maxsplit=1)
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
            try:
                index = int(args_str)
                delete_task(index)
            except ValueError:
                print("Индекс должен быть числом.")
        elif command == "help":
            help()
        else:
            print(f"Неизвестная команда: {command}. Введите 'help', чтобы посмотреть список команд.")


if __name__ == "__main__":
    main()