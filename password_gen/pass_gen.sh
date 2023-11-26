#!/bin/bash

generate_password() {
    # Define criteria
    length=$(( RANDOM % 6 + 9 ))  # Random length between 9 and 14 characters
    uppercase=$(echo {A..Z} | tr -d ' ' | shuf -n 1)  # At least one uppercase
    number=$(echo {0..9} | tr -d ' ' | shuf -n 1)  # At least one number
    special_char=$(echo '@#$%&*' | grep -o . | shuf -n 1)  # At least one of the specified special characters

    # Generate remaining characters
    remaining_chars=$(echo {a..z} | tr -d ' ' && echo {A..Z} | tr -d ' ' && echo {0..9} | tr -d ' ' && echo '@#$%&*' | tr -d ' ')
    password=$(echo $remaining_chars | tr -d ' ' | fold -w 1 | shuf | tr -d '\n' | head -c $((length - 3)))

    # Combine all parts to form the final password
    final_password="$password$uppercase$number$special_char"
    echo "$final_password"
}

save_to_log() {
    log_file_path="./pass_log.txt"
    echo "$1" >> "$log_file_path"
}

# Example usage
password=$(generate_password)
echo "Generated Password: $password"

# Save the password to the log file
save_to_log "$password"
