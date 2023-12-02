use rand::{thread_rng, Rng};
use std::fs::OpenOptions;
use std::io::Write;
use std::path::Path;

fn generate_password() -> String {
    // Define criteria
    let length = thread_rng().gen_range(9..=14); // Random length between 9 and 14 characters
    let uppercase = char::from(thread_rng().gen_range(b'A'..=b'Z')); // At least one uppercase
    let number = char::from(thread_rng().gen_range(b'0'..=b'9')); // At least one number
    let special_char = ['@', '#', '$', '%', '&', '*']
        .choose(&mut thread_rng())
        .unwrap(); // At least one of the specified special characters

    // Generate remaining characters
    let remaining_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*";
    let mut password: String = thread_rng()
        .sample_iter(rand::distributions::Alphanumeric)
        .take(length - 3)
        .collect();

    // Shuffle and insert the required characters at random positions
    let position_uppercase = thread_rng().gen_range(0..=length - 1);
    let position_number = thread_rng().gen_range(0..=length);
    let position_special_char = thread_rng().gen_range(0..=length + 1);

    password.insert(position_uppercase, uppercase);
    password.insert(position_number, number);
    password.insert(position_special_char, *special_char);

    password
}

fn save_to_log(password: &str) {
    let log_file_path = Path::new(env!("CARGO_MANIFEST_DIR")).join("pass_log.txt");
    let mut log_file = OpenOptions::new()
        .create(true)
        .append(true)
        .open(log_file_path)
        .expect("Unable to open log file");

    writeln!(log_file, "{}", password).expect("Unable to write to log file");
}

fn main() {
    // Example usage
    let password = generate_password();
    println!("Generated Password: {}", password);

    // Save the password to the log file
    save_to_log(&password);
}
