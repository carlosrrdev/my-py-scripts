#!/usr/bin/env python3
"""
Image to PDF Converter

This script converts PNG images in a specified directory to PDF files.
The images are processed to be black and white with emphasized text.

Dependencies:
- Pillow (PIL): pip install pillow
"""

import os
import glob
import sys
try:
    from PIL import Image, ImageEnhance, ImageFilter
except ImportError:
    print("Error: This script requires the Pillow library.")
    print("Please install it using: pip install pillow")
    sys.exit(1)

def get_directory_path():
    """Prompt the user for a directory path and validate it."""
    while True:
        dir_path = input("Please enter the directory path containing PNG images: ").strip()
        # Check if the path exists and is a directory
        if not os.path.exists(dir_path):
            print(f"Error: The path '{dir_path}' does not exist.")
            continue

        if not os.path.isdir(dir_path):
            print(f"Error: '{dir_path}' is not a directory.")
            continue

        return dir_path

def create_output_directory(base_dir):
    """Create an output directory for the PDF files."""
    output_dir = os.path.join(base_dir, "output")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"Created output directory: {output_dir}")
        except OSError as e:
            print(f"Error creating output directory: {e}")
            sys.exit(1)

    return output_dir

def find_png_files(directory):
    """Find all PNG files in the specified directory."""
    png_pattern = os.path.join(directory, "*.png")
    png_files = glob.glob(png_pattern)

    # Also search for uppercase extension
    png_pattern_upper = os.path.join(directory, "*.PNG")
    png_files.extend(glob.glob(png_pattern_upper))

    return png_files

def process_image(image_path):
    """Process the image to be black and white with emphasized text."""
    try:
        # Open the image
        image = Image.open(image_path)

        # Convert to grayscale
        image = image.convert('L')

        # Apply contrast enhancement to emphasize text
        contrast_enhancer = ImageEnhance.Contrast(image)
        image = contrast_enhancer.enhance(2)
        brightness_enhancer = ImageEnhance.Brightness(image)
        image = brightness_enhancer.enhance(4)
        sharpness_enhancer = ImageEnhance.Sharpness(image)
        image = sharpness_enhancer.enhance(4.0)

        # Apply slight sharpening to make text clearer
        image = image.filter(ImageFilter.SHARPEN)

        return image
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

def convert_to_pdf(image, output_path):
    """Convert the processed image to PDF."""
    try:
        # Save as PDF
        image.save(output_path, "PDF", resolution=100.0)
        return True
    except Exception as e:
        print(f"Error converting to PDF: {e}")
        return False

def main():
    print("Image to PDF Converter")
    print("======================")

    # Get directory path from user
    dir_path = get_directory_path()

    # Create output directory
    output_dir = create_output_directory(dir_path)

    # Find PNG files
    png_files = find_png_files(dir_path)

    if not png_files:
        print(f"No PNG files found in {dir_path}")
        return

    print(f"Found {len(png_files)} PNG files.")

    # Process each PNG file
    for i, png_file in enumerate(png_files, 1):
        file_name = os.path.basename(png_file)
        print(f"Processing {i}/{len(png_files)}: {file_name}")

        # Process the image
        processed_image = process_image(png_file)
        if processed_image is None:
            continue

        # Generate output PDF path
        pdf_name = os.path.splitext(file_name)[0] + ".pdf"
        pdf_path = os.path.join(output_dir, pdf_name)

        # Convert to PDF
        if convert_to_pdf(processed_image, pdf_path):
            print(f"Successfully converted {file_name} to {pdf_name}")
        else:
            print(f"Failed to convert {file_name} to PDF")

    print("\nConversion complete!")
    print(f"PDF files are saved in: {output_dir}")

if __name__ == "__main__":
    main()
