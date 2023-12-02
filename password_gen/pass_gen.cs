using System;
using System.IO;

class Program
{
    static void Main()
    {
        // Example usage
        string password = GeneratePassword();
        Console.WriteLine("Generated Password: " + password);

        // Save the password to the log file
        SaveToLog(password);
    }

    static string GeneratePassword()
    {
        // Define criteria
        Random random = new Random();
        int length = random.Next(9, 15);  // Random length between 9 and 14 characters
        char uppercase = (char)random.Next('A', 'Z' + 1);  // At least one uppercase
        char number = (char)random.Next('0', '9' + 1);  // At least one number
        char specialChar = "@#$%&*"[random.Next(0, 6)];  // At least one of the specified special characters

        // Generate remaining characters
        string remainingChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*";
        char[] passwordArray = new char[length - 3];
        for (int i = 0; i < length - 3; i++)
        {
            passwordArray[i] = remainingChars[random.Next(0, remainingChars.Length)];
        }

        // Shuffle and insert the required characters at random positions
        int positionUppercase = random.Next(0, length);
        int positionNumber = random.Next(0, length + 1);
        int positionSpecialChar = random.Next(0, length + 2);

        Array.Resize(ref passwordArray, length);
        passwordArray[positionUppercase] = uppercase;
        passwordArray[positionNumber] = number;
        passwordArray[positionSpecialChar] = specialChar;

        // Convert char array to string
        string finalPassword = new string(passwordArray);

        return finalPassword;
    }

    static void SaveToLog(string password)
    {
        string logFilePath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "pass_log.txt");
        using (StreamWriter logFile = new StreamWriter(logFilePath, true))
        {
            logFile.WriteLine(password);
        }
    }
}
