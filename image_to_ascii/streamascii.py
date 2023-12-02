import streamlit as st
from PIL import Image
import numpy as np

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
    ascii_chars = r"@%#*+=-:. "[::-1] if color_invert else r"@%#*+=-:. "[::1]
    
    ascii_art = ""
    for j in range(image.height):
        for i in range(image.width):
            pixel_block = image.crop((i, j, i + 1, j + 1))
            intensity = average_intensity(pixel_block)
            ascii_char = ascii_chars[int((intensity * 9) / 255)]
            ascii_art += ascii_char
        ascii_art += "\n"
    
    return ascii_art

def main():
    st.title("Image to ASCII Art Converter")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        width = st.slider("Select the width of the output image:", 10, 200, 75, step=1)

        color_invert = st.checkbox("Invert colors")

        image = load_image(uploaded_file)
        resized_image = resize_image(image, width)
        grayscale_image = convert_to_grayscale(resized_image)
        ascii_art = generate_ascii_art(grayscale_image, width, color_invert)

        st.text_area("ASCII Art Output:", ascii_art, height=400)
        st.text("Paste the code into Notepad to see the full image properly.")

if __name__ == "__main__":
    main()
