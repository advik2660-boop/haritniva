tasks = []


def add_task(task, date):

    tasks.append({
        "task": task,
        "date": date,
        "done": False
    })


def get_tasks():
    return tasks


def complete_task(index):

    if 0 <= index < len(tasks):
        tasks[index]["done"] = True