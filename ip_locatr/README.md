
# IP Geolocation Tool

This command-line tool retrieves geolocation information for a given IP address using the ip-api.com API. It provides details such as the country, region, city, latitude, longitude, timezone, ISP, and organization associated with the IP address.

## Requirements

- Python 3.x
- requests library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/ip-geolocation-tool.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ip-geolocation-tool
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script `script.py` with the following command-line arguments:

```bash
python script.py [ip_address]
```

- `[ip_address]` (optional): Specify the IP address for which you want to retrieve geolocation information. If not provided, the geolocation information for the user's IP address will be retrieved.

Example:

```bash
python script.py 8.8.8.8
```

This command will retrieve geolocation information for the IP address `8.8.8.8`.

If no IP address is provided, the tool will retrieve geolocation information for the user's IP address by default.

## API Usage

This tool utilizes the ip-api.com API to retrieve geolocation information. You can find more details about the API and its usage [here](http://ip-api.com/docs/api:json).
