# QR Code Generator

This Python script allows you to generate QR codes from various inputs such as text, files (PDF, PNG, JPEG), and URLs. The generated QR codes can be saved locally and/or uploaded to Google Drive.

## Features

- Generate QR codes from:
  - Text input
  - Files (PDF, PNG, JPEG)
  - URLs

- Upload generated files (PDF, PNG, JPEG) to Google Drive

## Prerequisites

- Python 3.x
- `tkinter` library
- `qrcode` library
- `googleSourceCode_YT` module (for Google Drive integration)
- `requests` library (for Google Drive integration)
- `googleapiclient` library (for Google Drive integration)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/qr-code-generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd qr-code-generator
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script `qr_code_generator.py` using Python:

```bash
python qr_code_generator.py
```

The script will open a GUI window where you can select the type of input (text, file, URL) and generate QR codes accordingly.

## Google Drive Integration

To enable Google Drive integration for uploading files, make sure to provide the necessary credentials (`OAuth_Client.json`) and set up the required scopes in the `googleSourceCode_YT` module.

