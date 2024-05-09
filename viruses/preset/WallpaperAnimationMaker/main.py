import os
import zipfile
import tkinter as tk
from tkinter import filedialog

def create_animation_zip(frames, animation_name, output_dir):
    print("Creating ZIP file...")
    zip_file_path = os.path.join(output_dir, f"{animation_name}.zip")
    try:
        with zipfile.ZipFile(zip_file_path, "w") as zipf:
            # Write each frame to the ZIP file
            for frame_number, (frame_name, frame_data) in enumerate(frames.items(), start=1):
                frame_folder = f'frames/{frame_number}/'
                zipf.writestr(f"{frame_folder}frame.png", frame_data)
                zipf.writestr(f"{frame_folder}metadata/type.txt", os.path.splitext(frame_name)[1])

            # Create frames.txt
            zipf.writestr("frames.txt", str(len(frames)))

        print(f"Animation ZIP file '{zip_file_path}' created successfully.")
        print(f"ZIP file location: {os.path.abspath(zip_file_path)}")
    except Exception as e:
        print(f"Error creating ZIP file: {e}")

def select_images():
    root = tk.Tk()
    root.withdraw()
    root.update()  # Ensure the window is updated before showing the dialog
    print("Opening file dialog...")
    image_files = filedialog.askopenfilenames(title="Select image files", filetypes=(("Image files", "*.png;*.jpg"), ("All files", "*.*")))
    print("File dialog closed.")
    return image_files

def select_output_dir():
    root = tk.Tk()
    root.withdraw()
    output_dir = filedialog.askdirectory(title="Select output directory")
    return output_dir

def main():
    frames = {}
    image_files = select_images()
    if not image_files:
        print("No image files selected. Exiting.")
        return

    for image_file in image_files:
        with open(image_file, "rb") as f:
            frames[os.path.basename(image_file)] = f.read()

    animation_name = input("Enter the name for the animation: ")
    output_dir = select_output_dir()

    create_animation_zip(frames, animation_name, output_dir)

if __name__ == "__main__":
    main()
