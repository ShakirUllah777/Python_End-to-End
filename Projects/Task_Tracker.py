
'''
Task Tracker,
Requirements
The application should run from the command line, accept user actions and 
inputs as arguments, and store the tasks in a JSON file. The user should be able to:

Add, Update, and Delete tasks
Mark a task as in progress or done
List all tasks
List all tasks that are done
List all tasks that are not done
List all tasks that are in progress '''


tasks = []
task_status = {
    '1': 'done',
    '2': 'Not Done',
    '3': 'Inprogress'
}


def add_task(title,status):
    task = {
        'title': title,
        'status': status
    }
    tasks.append(task)
    print("Task added succesfully!")


def update_task(index, new_title, new_status):
    if 0 <= index < len(tasks):
        if new_title.strip() != "":
            tasks[index]['title'] = new_title
        tasks[index]['status'] = new_status
        print('Task Updated')
    else:
        print('Task Not Found')

def delet_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print('Task Deleted')
    else:
        print('Task Not Found!')


def list_tasks():
    for i, task in enumerate(tasks):
        print(f"{i}. {task['title']} - {task['status']}")


def done_task():
    for task in tasks:
        if task['status'] == 'Done':
            print(task)

def not_done_task():
    for task in tasks:
        if task['status'] == 'Not Done':
            print(task)

def inprogress_task():
    for task in tasks:
        if task['status'] == 'Inprogress':
            print(task)

while True:
    print("\n1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. List Tasks")
    print("5. Done Tasks")
    print("6. Not Done Tasks")
    print("7. InProgress Tasks")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter task title: ")

        print('Select Status: ')
        print('1. Done')
        print('2. Not Done')
        print('3. Inprogress')
        status_choice = input('Enter status Number: ')
        status = task_status.get(status_choice, 'Not Done')

        add_task(title, status)

    elif choice == '2':
        list_tasks()
        index = int(input('Enter task Index: '))
        new_title = input('Enter New Task: ')
        print('Select Status: ')
        print('1. Done')
        print('2. Not Done')
        print('3. Inprogress')
        status_choice = input('Enter status Number: ')
        new_status = task_status.get(status_choice, 'Not Done')
        update_task(index, new_title, new_status)

    elif choice == '3':
        list_tasks()
        index = int(input('Enter the Task Index: '))
        delet_task(index=index)

    elif choice == '4':
        list_tasks()

    elif choice == '5':
        done_task()

    elif choice == '6':
        not_done_task()

    elif choice == '7':
        inprogress_task()

    elif choice == "8":
        print('GoodBye...')
        break

    else:
        print("Invalid choice!")