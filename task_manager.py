# task_manager.py
import advance_butler_bot.slam_navigation as slam_navigation
import arm_control
import detection

def execute_task(task):
    if task == 'fetch_drink':
        print("Executing task: Fetch Drink")
        slam_navigation.navigate_to_goal('fridge')
        arm_control.grab_object()
        slam_navigation.navigate_to_goal('person')
        arm_control.release_object()
        print("Task completed: Drink delivered to person")

    # Add more tasks as needed

if __name__ == '__main__':
    task = 'fetch_drink'  # Example task, replace with actual task input
    execute_task(task)
