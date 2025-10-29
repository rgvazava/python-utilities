import psutil
import datetime

# This small script checks basic system health info like CPU, memory, and disk space.
# I made it while learning how to monitor system performance using Python.

def get_system_health():
    # Get current date and time
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get system stats
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    # Format results in a readable way
    report = f"""
    System Health Report - {now}
    --------------------------------
    CPU Usage: {cpu_usage}%
    Memory Usage: {memory.percent}% ({round(memory.used / (1024**3), 2)} GB used)
    Disk Usage: {disk.percent}% ({round(disk.free / (1024**3), 2)} GB free)
    --------------------------------
    """

    return report


def save_report(report):
    # Save results to a simple log file
    with open("system_report.txt", "a") as file:
        file.write(report)
        file.write("\n")  # add spacing between logs


if __name__ == "__main__":
    print("Checking system health...")

    # Get system stats and print them
    report = get_system_health()
    print(report)

    # Save the report to a file for later
    save_report(report)

    print("Report saved to system_report.txt")
