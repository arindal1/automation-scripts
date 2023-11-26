import os
import psutil
from plyer import notification
import logging
from datetime import datetime

# Set the log file location to the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_directory, 'system_monitor.log')

# Set your threshold values
CPU_THRESHOLD = 80  # Example: 80% CPU usage
MEMORY_THRESHOLD = 80  # Example: 80% memory usage
DISK_THRESHOLD = 80  # Example: 80% disk usage

# Set up logging
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('Script started.')

# Function to get CPU usage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# Function to get memory usage
def get_memory_usage():
    return psutil.virtual_memory().percent

# Function to get disk space usage
def get_disk_usage():
    return psutil.disk_usage('/').percent

# Function to show desktop notification
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification will disappear after 10 seconds
    )

# Main function
def main():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()

    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage: {cpu_usage}%')
        show_notification('High CPU Usage', f'CPU usage is {cpu_usage}%.')

    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage: {memory_usage}%')
        show_notification('High Memory Usage', f'Memory usage is {memory_usage}%.')

    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'High Disk usage: {disk_usage}%')
        show_notification('High Disk Usage', f'Disk usage is {disk_usage}%.')

    logging.info('System check completed.')

if __name__ == "__main__":
    main()
