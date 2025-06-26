# Image to PDF Converter

A command-line tool that converts PNG images to PDF files with text enhancement.

## Description

This script allows you to:
- Convert multiple PNG images to PDF files
- Process images to be black and white with emphasized text
- Automatically create an output directory for the PDF files
- Track progress and errors during conversion

## Requirements

- Python 3.6 or higher
- Pillow (PIL) library

## Installation

1. Ensure you have Python 3.6+ installed
2. Install the required Pillow library:
   ```
   pip install pillow
   ```

## Usage

1. Run the script:
   ```
   python image-to-pdf-cli.py
   ```
2. When prompted, enter the full path to the directory containing your PNG images
3. The script will:
   - Create an "output" subdirectory in the specified location (if it doesn't exist)
   - Find all PNG files in the specified directory
   - Process each image to enhance text readability
   - Convert each processed image to a PDF file
   - Save all PDF files in the output directory

## Features

- **Black and White Conversion**: Converts images to grayscale for better text clarity
- **Text Enhancement**: Applies contrast enhancement and sharpening to make text more readable
- **Error Handling**: Provides clear error messages if issues occur during processing
- **Progress Tracking**: Shows progress as each image is processed

## Example

```
$ python image-to-pdf-cli.py
Image to PDF Converter
======================
Please enter the directory path containing PNG images: /path/to/images
Created output directory: /path/to/images/output
Found 3 PNG files.
Processing 1/3: document1.png
Successfully converted document1.png to document1.pdf
Processing 2/3: document2.png
Successfully converted document2.png to document2.pdf
Processing 3/3: document3.png
Successfully converted document3.png to document3.pdf

Conversion complete!
PDF files are saved in: /path/to/images/output
```
