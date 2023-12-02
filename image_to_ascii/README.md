# Image to ASCII Converter

## How to run **asciicon.py*?

1. **Save the Code:**
   Save the provided code in a file with a `.py` extension. For example, you can save it as `image_to_ascii.py`.

2. **Install Required Libraries:**
   Make sure you have the Pillow library installed. You can install it using:

   ```bash
   pip install Pillow
   ```

3. **Run the Script:**
   Open a terminal or command prompt, navigate to the directory where you saved the script, and run the script using the following command:

   ```bash
   python image_to_ascii.py input_image.jpg output.txt -w 75 -c
   ```

   Replace `input_image.jpg` with the path to your input image and `output.txt` with the desired output file path. Adjust the `-w` (width) and `-c` (color_invert) options as needed.

   Example:
   - `-w 75`: Set the width of the output image to 75 characters.
   - `-c`: Invert the colors of the image.

4. **Check Output:**
   After running the script, check the specified output file (e.g., `output.txt`) for the generated ASCII art.

---

## How to run **streamascii.py**?

Run command: `streamlit run streamascii.py` after installing Streamlit using `pip install streamlit`.
