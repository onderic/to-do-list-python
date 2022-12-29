class Task:
  def __init__(self, description, priority):
    self.description = description
    self.priority = priority

  def __str__(self):
    return f"{self.description} (priority: {self.priority})"

class HighPriorityTask(Task):
  def __init__(self, description):
    super().__init__(description, "high")

class MediumPriorityTask(Task):
  def __init__(self, description):
    super().__init__(description, "medium")

class LowPriorityTask(Task):
  def __init__(self, description):
    super().__init__(description, "low")

class TaskFactory:
  def create_task(self, description, priority):
    if priority == "high":
      return HighPriorityTask(description)
    elif priority == "medium":
      return MediumPriorityTask(description)
    elif priority == "low":
      return LowPriorityTask(description)

class TodoList:
  def __init__(self):
    self.tasks = []
    self.factory = TaskFactory()

  def add_task(self, description, priority):
    task = self.factory.create_task(description, priority)
    self.tasks.append(task)

  def remove_task(self, index):
    del self.tasks[index]

  def view_tasks(self):
    for i, task in enumerate(self.tasks):
      print(f"{i+1}. {task}")

# Create a to-do list
todo_list = TodoList()

# Add some tasks
todo_list.add_task("Buy groceries", "high")
todo_list.add_task("Take out the trash", "medium")
todo_list.add_task("Watch a movie", "low")

# View the tasks
todo_list.view_tasks()

# Remove a task
todo_list.remove_task(0)

# View the tasks again
todo_list.view_tasks()
