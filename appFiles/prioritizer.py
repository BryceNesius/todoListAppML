def prioritize_tasks(tasks):
    # Simple sorting based on priority (high > medium > low) 
    return sorted(tasks, key=lambda task: task.priority, reverse=True) 