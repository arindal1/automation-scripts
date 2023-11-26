import psutil

def find_script_process(script_name):
    for process in psutil.process_iter(['pid', 'name']):
        if script_name.lower() in process.info['name'].lower():
            return process.info['pid']
    return None

# Replace 'sys_rec.py' with the actual name of your script
script_name = 'sys_rec.py'
script_pid = find_script_process(script_name)

if script_pid is not None:
    print(f"Script {script_name} is running with PID: {script_pid}")
else:
    print(f"Script {script_name} is not currently running.")

# This script will print the PID (Process ID) of your script if it is currently running.
