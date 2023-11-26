# System Monitoring Script

This *python* script monitors the CPU's stats, like CPU, Memory and Disk usage, makes a log of all the info it collects when running, into a txt file `system_monitor` in the same directory.
It also sends alert notifications when the usage of certain stat crosses the specified threshold.

### Dependencies:

Here are the dependencies used in your script:

1. **psutil:**
   - Purpose: Provides an interface for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors).
   - Installation: You can install it using the following command:
     ```bash
     pip install psutil
     ```

2. **plyer:**
   - Purpose: Cross-platform library for accessing features commonly found on various operating systems, such as sending notifications.
   - Installation: You can install it using the following command:
     ```bash
     pip install plyer
     ```

Make sure to run these commands in your terminal or command prompt to install the required dependencies before running the script. If you encounter any issues during installation.

### Running the Script:

```
python sys_rec.py
```
- The above command will run the script.

The name of the process in the Task Manager will typically be the name of the Python executable (`python.exe` or `python3.exe`) along with the name of your script. If your script is named `sys_rec.py`, you would see a process named something like `python.exe sys_rec.py` or `python3.exe sys_rec.py`.

Keep in mind that the exact name may vary depending on your operating system and how you run the script. If you are using a virtual environment, the process name may include the path to the virtual environment as well.

To find the process name more precisely, you can run the script and then check the Task Manager to see the exact name under the "Processes" tab.

   - Additionally, you can use the `psutil` library to programmatically find the process name. Here's an example [find_process](find_process.py).


To stop the script, you can terminate its process. You can do this using the task manager or a similar system monitoring tool, or by using the psutil library to find and terminate the process programmatically.

   - Here's a simple example of how you can use psutil to terminate the script: [close_process](close_process.py).


### How to run the bash script?

Bash doesn't have built-in libraries like `psutil` and `plyer`, so the script uses standard Linux commands for system monitoring and the `zenity` command for desktop notifications.

Save the script and make it executable with the following command:

```bash
chmod +x system_monitor.sh
```

You can then run the script using:

```bash
./system_monitor.sh
```

> PS: This Bash script is a simplified example and may need adjustments based on your specific requirements and the platform you are running it on. Also, ensure that `zenity` is installed on your system for the desktop notifications. If it's not installed, you can usually install it using your package manager (e.g., `sudo apt-get install zenity` on Debian-based systems).
