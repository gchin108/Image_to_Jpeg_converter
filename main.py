import tkinter as tk
from tkinter import filedialog
from PIL import Image, UnidentifiedImageError
import os


def convert_to_jpeg():
    # Open file dialog to select an image file
    file_path = filedialog.askopenfilename()

    if file_path:
        try:
            # Open the selected image file
            with Image.open(file_path) as im:
                # Convert the image to RGB mode if it has an alpha channel
                # images with an alpha channel (such as RGBA mode) cannot be directly saved as JPEG.
                if im.mode == 'RGBA':
                    im = im.convert('RGB')

                # Convert the image to JPEG format
                file_name, _ = os.path.splitext(file_path)
                converted_file_path = f"{file_name}_mod.jpg"

                im.save(converted_file_path, "JPEG")

            # Display success message
            success_label.config(text=f"Conversion successful! Saved as {converted_file_path}")
        except UnidentifiedImageError:
            # Display error message if the image file format is not supported
            success_label.config(text="Conversion failed. Unsupported image file format.")
        except Exception as e:
            # Display the specific error message if any other exception occurs
            success_label.config(text=f"Conversion failed. Error: {str(e)}")
    else:
        # Display error message if no file is selected
        success_label.config(text="No file selected.")


# Create the main Tkinter window
window = tk.Tk()
window.title("Image to JPEG Converter")
window.config(padx=20, pady=20)
logo_image = tk.PhotoImage(file='logo.png')
canvas = tk.Canvas(width=128, height=128)
canvas.create_image(64, 64, image=logo_image)
canvas.grid(column=1, row=0)

# Create and configure the file select button
select_button = tk.Button(window, text="Select Image File", command=convert_to_jpeg)
select_button.grid(column=1, row=1)

# Create a label to display success/error messages
success_label = tk.Label(window, text="")
success_label.grid(column=1, row=2)

# Run the Tkinter event loop
window.mainloop()
