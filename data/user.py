from data.task import Task


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks: list = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def get_tasks(self) -> list:
        return self.tasks

    def __str__(self) -> str:
        return f"{self.name} ({len(self.tasks)} tasks)"
