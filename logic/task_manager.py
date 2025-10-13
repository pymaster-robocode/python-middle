from data.task import Task
from data.user import User


class TaskManager:
    def __init__(self, user: User) -> None:
        self.user = user

    def create_task(self, title: str) -> None:
        task = Task(title)
        self.user.add_task(task)

    def list_tasks(self) -> list:
        return self.user.get_tasks()

    def mark_done(self, index: int) -> None:
        try:
            self.user.tasks[index].mark_done()
        except IndexError:
            print("❌ Incorrect task index.")
