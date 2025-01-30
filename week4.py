import csv
import os
from datetime import datetime

# Define task categories
tasks = {
    "Morning": ["Review internship tasks", "Code a feature/solve a bug", "Write documentation"],
    "Afternoon": ["Continue coding/debugging/testing", "Attend team meetings", "Work on trading strategies"],
    "Evening": ["Learn new concepts", "Work on Women Safety Analytics project", "Track trading performance"],
    "Night": ["Participate in hackathons", "Review the day’s progress", "Relax & unwind"]
}

# File to store tasks
csv_file = "daily_task_tracker.csv"

# Check if file exists, if not create it
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Time", "Task", "Status"])  # Header row

# Function to log task status
def log_task():
    date_today = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")
    
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        
        print(f"\n--- DAILY TASK TRACKER ---\nDate: {date_today}\n")

        for category, task_list in tasks.items():
            print(f"\n[{category} Tasks]")
            for task in task_list:
                status = input(f"  - {task} (Y for Done / N for Pending): ").strip().upper()
                while status not in ["Y", "N"]:
                    print("Invalid input! Please enter 'Y' for Done or 'N' for Pending.")
                    status = input(f"  - {task} (Y for Done / N for Pending): ").strip().upper()
                writer.writerow([date_today, time_now, task, "Completed" if status == "Y" else "Pending"])

    print("\nTasks recorded successfully!\n")

# Run the task logger
log_task()
