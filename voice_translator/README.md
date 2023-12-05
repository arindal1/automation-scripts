# Speech Recognition and Translation Program

This Python program utilizes speech recognition to detect spoken words and translates them into a user-specified language. The translation is performed using the Google Translate API.

## Requirements

Make sure to install the required dependencies before running the program. You can install them using the following command:

```bash
pip install -r requirements.txt
```

The required packages are specified in the `requirements.txt` file.

Run `translator.py`.

## Usage

1. Run the program by executing the Python script `speech_translation.py`.
2. Start speaking into the microphone.
3. To terminate the program, say 'Exit' or 'Quit'.
4. Enter the target language for translation when prompted.

## Dependencies

- `speech_recognition` for speech recognition functionality.
- `langdetect` for language detection of the input speech.
- `google_trans_new` for Google Translate API integration.
- `pyttsx3` for text-to-speech functionality.
