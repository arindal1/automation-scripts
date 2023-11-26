#!/bin/bash

# Set your threshold values
CPU_THRESHOLD=80  # Example: 80% CPU usage
MEMORY_THRESHOLD=80  # Example: 80% memory usage
DISK_THRESHOLD=80  # Example: 80% disk usage

# Set up logging
LOG_FILE="system_monitor.log"
echo "$(date '+%Y-%m-%d %H:%M:%S') - Script started." >> "$LOG_FILE"

# Function to get CPU usage
get_cpu_usage() {
  echo "$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)"
}

# Function to get memory usage
get_memory_usage() {
  echo "$(free | awk '/Mem/{print $3/$2*100}')"
}

# Function to get disk space usage
get_disk_usage() {
  echo "$(df -h / | awk 'NR==2{print $5}' | cut -d'%' -f1)"
}

# Function to show desktop notification
show_notification() {
  zenity --info --title="$1" --text="$2" --timeout=10
}

# Main function
main() {
  cpu_usage=$(get_cpu_usage)
  memory_usage=$(get_memory_usage)
  disk_usage=$(get_disk_usage)

  if [ "$(echo "$cpu_usage > $CPU_THRESHOLD" | bc -l)" -eq 1 ]; then
    echo "High CPU usage: $cpu_usage%"
    show_notification "High CPU Usage" "CPU usage is $cpu_usage%."
  fi

  if [ "$(echo "$memory_usage > $MEMORY_THRESHOLD" | bc -l)" -eq 1 ]; then
    echo "High Memory usage: $memory_usage%"
    show_notification "High Memory Usage" "Memory usage is $memory_usage%."
  fi

  if [ "$(echo "$disk_usage > $DISK_THRESHOLD" | bc -l)" -eq 1 ]; then
    echo "High Disk usage: $disk_usage%"
    show_notification "High Disk Usage" "Disk usage is $disk_usage%."
  fi

  echo "$(date '+%Y-%m-%d %H:%M:%S') - System check completed." >> "$LOG_FILE"
}

# Execute main function
main
