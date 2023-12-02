from PIL import Image
import numpy as np
import argparse

def load_image(image_path):
    return Image.open(image_path)

def resize_image(image, width):
    aspect_ratio = image.height / image.width
    new_height = int(width * aspect_ratio)
    return image.resize((width, new_height))

def convert_to_grayscale(image):
    return image.convert("L")

def average_intensity(pixel_block):
    return np.average(np.array(pixel_block))

def generate_ascii_art(image, width, color_invert):
    ascii_chars = r"@%#*+=-:. "[:: - 1] if color_invert else r"@%#*+=-:. "[::1]
    
    with open("output.txt", "w") as f:
        for j in range(image.height):
            for i in range(image.width):
                pixel_block = image.crop((i, j, i + 1, j + 1))
                intensity = average_intensity(pixel_block)
                ascii_char = ascii_chars[int((intensity * 9) / 255)]
                f.write(ascii_char)
                print(ascii_char, end="")
            print("\n", end="")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_image', help='Path to input image')
    parser.add_argument('output_file', help='Path to output file')
    parser.add_argument('-w', '--width', help='Width of the output image', type=int, default=75)
    parser.add_argument('-c', '--color_invert', help='Invert colors of the image', action='store_true')
    args = parser.parse_args()

    input_image_path = args.input_image
    output_path = args.output_file
    width = args.width

    image = load_image(input_image_path)
    resized_image = resize_image(image, width)
    grayscale_image = convert_to_grayscale(resized_image)

    generate_ascii_art(grayscale_image, width, args.color_invert)

if __name__ == "__main__":
    main()
