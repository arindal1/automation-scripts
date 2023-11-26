# Password Generator

This script defines a function `generate_password` that creates a random password based on your criteria. It uses the `random` module to generate random characters and positions.
The password is constructed by ensuring at least one uppercase letter, one number, and one special character is included. The final password is then shuffled to make it more secure.

- The script also makes a log file [pass_log.txt](pass_log.txt) that stores all the generated passwords so that the user can use them however and whenever.

```
python pass_gen.py
```
Run the python script using the above command.


Make file `pass_gen.sh` executable with the following command:

```bash
chmod +x system_monitor.sh
```

- You can then run the script using:

```bash
./system_monitor.sh
```

In this Bash script:

- `generate_password` function is responsible for creating a random password based on the specified criteria.
- `save_to_log` function appends the generated password to the `pass_log.txt` file.
- The script then generates a password, prints it to the console, and saves it to the log file.

Note: This Bash script uses `fold`, `shuf`, and other shell commands to achieve the password generation. The exact commands might vary based on your system's utilities.
