import psutil

def stop_script(script_name):
    for process in psutil.process_iter(['pid', 'name']):
        if script_name.lower() in process.info['name'].lower():
            pid = process.info['pid']
            psutil.Process(pid).terminate()
            print(f'Script {script_name} (PID: {pid}) terminated.')

# Replace 'sys_rec.py' with the actual name of your script
stop_script('sys_rec.py')

# Keep in mind that forcibly terminating a script may result in incomplete execution of tasks or data corruption, so it's generally preferable to allow the script to finish its current task before terminating it.
