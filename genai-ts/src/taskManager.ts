interface Task {
  title: string;
  description: string;
}

export class TaskManager {
  private tasks: Task[] = [];

  /**
   * Adds a task to the task list.
   * @param title The title of the task.
   * @param description The description of the task.
   */
  addTask(title: string, description: string): void {
    this.tasks.push({ title, description });
  }

  /**
   * Lists all tasks.
   * @returns An array of tasks.
   */
  listTasks(): Task[] {
    return this.tasks;
  }
}