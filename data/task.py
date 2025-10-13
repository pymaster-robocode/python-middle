class Task:
    def __init__(self, title: str, completed: bool = False) -> None:
        self.title = title
        self.completed = completed

    def mark_done(self) -> None:
        self.completed = True

    def __str__(self) -> str:
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"
