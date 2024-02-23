# Image Pixel Sorting Tool

This tool generates multiple sorted versions of an input image using various pixel sorting parameters. It provides a command-line interface for specifying the input image and the number of output images required.

## Requirements

- Python 3.x
- PIL (Python Imaging Library)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/image-pixel-sorting.git
    ```

2. Navigate to the project directory:

    ```bash
    cd image-pixel-sorting
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script `autosort.py` with the following command-line arguments:

```bash
python autosort.py -i <input_image_path> -n <output_count>
```

- `<input_image_path>`: Path to the input image file.
- `<output_count>`: Number of output images to generate.

Example:

```bash
python autosort.py -i input_image.jpg -n 5
```

This command will generate 5 sorted images based on the input image and save them in the `generated` directory.

## Customization

You can customize the pixel sorting parameters by modifying the `randomize_params` function in the `autosort.py` script. This function randomizes values for various parameters such as angle, interval function, randomness, lower threshold, upper threshold, and sorting function.

## Image Used

![image1](images/dragon.jpg)

## Result

![image2](images/result-01.png)
