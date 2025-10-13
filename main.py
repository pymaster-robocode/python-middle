from data.user import User
from logic.task_manager import TaskManager
from helper import show_tasks


def main() -> None:
    user = User("Robocat")
    manager = TaskManager(user)

    manager.create_task("Learn python")
    manager.create_task("Complete marathon")
    manager.create_task("Hack pentagon")

    print("\nTasks:")
    show_tasks(manager.list_tasks())

    print("\nFinish second task")
    manager.mark_done(1)

    print("\nNew list:")
    show_tasks(manager.list_tasks())


if __name__ == "__main__":
    main()
