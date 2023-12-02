const fs = require('fs');

function generatePassword() {
    // Define criteria
    const length = Math.floor(Math.random() * (14 - 9 + 1)) + 9; // Random length between 9 and 14 characters
    const uppercase = String.fromCharCode(Math.floor(Math.random() * (90 - 65 + 1)) + 65); // At least one uppercase
    const number = String.fromCharCode(Math.floor(Math.random() * (57 - 48 + 1)) + 48); // At least one number
    const specialChar = ['@', '#', '$', '%', '&', '*'][Math.floor(Math.random() * 6)]; // At least one of the specified special characters

    // Generate remaining characters
    const remainingChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*';
    let password = '';
    for (let i = 0; i < length - 3; i++) {
        password += remainingChars[Math.floor(Math.random() * remainingChars.length)];
    }

    // Shuffle and insert the required characters at random positions
    const positionUppercase = Math.floor(Math.random() * length);
    const positionNumber = Math.floor(Math.random() * (length + 1));
    const positionSpecialChar = Math.floor(Math.random() * (length + 2));

    password = password.split('');
    password.splice(positionUppercase, 0, uppercase);
    password.splice(positionNumber, 0, number);
    password.splice(positionSpecialChar, 0, specialChar);

    // Convert array back to string
    const finalPassword = password.join('');

    return finalPassword;
}

function saveToLog(password) {
    const logFilePath = 'pass_log.txt';
    fs.appendFileSync(logFilePath, password + '\n');
}

// Example usage
const password = generatePassword();
console.log('Generated Password:', password);

// Save the password to the log file
saveToLog(password);
