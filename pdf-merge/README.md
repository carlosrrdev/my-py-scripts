# PDF Merger

A command-line tool that merges PDF files from a child directory into matching PDFs in a parent directory.

## Description

This script allows you to:
- Specify a child directory and a parent directory containing PDF files
- Find PDF files in the child directory that have matching filenames in the parent directory
- Merge matching PDFs by appending the child PDF to the end of the parent PDF
- Track progress and provide feedback during the merging process

## Requirements

- Python 3.6 or higher
- PyPDF library
- Rich library (for console output formatting)

## Installation

1. Ensure you have Python 3.6+ installed
2. Install the required libraries:
   ```
   pip install pypdf rich
   ```

## Usage

1. Run the script:
   ```
   python pdf-merge-cli.py
   ```
2. When prompted, enter the full path to the child directory containing your PDF files
3. When prompted, enter the full path to the parent directory containing your PDF files
4. The script will:
   - Find all PDF files in both directories
   - Identify matching filenames between the two directories
   - Merge each child PDF into its matching parent PDF
   - Provide feedback on the merging process

## Features

- **Filename Matching**: Automatically identifies PDFs with the same filename in both directories
- **PDF Merging**: Appends the content of child PDFs to the end of matching parent PDFs
- **Error Handling**: Provides clear error messages if issues occur during processing
- **Progress Tracking**: Shows progress as each PDF is processed
- **Case-Insensitive Extension Matching**: Finds PDF files regardless of whether the extension is uppercase or lowercase

