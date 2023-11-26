import random
import string
import os

def generate_password():
    # Define criteria
    length = random.randint(9, 14)  # Random length between 9 and 14 characters
    uppercase = random.choice(string.ascii_uppercase)  # At least one uppercase
    number = random.choice(string.digits)  # At least one number
    special_char = random.choice('@#$%&*')  # At least one of the specified special characters

    # Generate remaining characters
    remaining_chars = string.ascii_letters + string.digits + '@#$%&*'
    password = ''.join(random.choice(remaining_chars) for _ in range(length - 3))

    # Shuffle and insert the required characters at random positions
    password_list = list(password)
    password_list.insert(random.randint(0, length - 1), uppercase)
    password_list.insert(random.randint(0, length), number)
    password_list.insert(random.randint(0, length + 1), special_char)

    # Convert the list back to a string
    final_password = ''.join(password_list)

    return final_password

def save_to_log(password):
    log_file_path = os.path.join(os.path.dirname(__file__), 'pass_log.txt')
    with open(log_file_path, 'a') as log_file:
        log_file.write(password + '\n')

# Example usage
password = generate_password()
print("Generated Password:", password)

# Save the password to the log file
save_to_log(password)
