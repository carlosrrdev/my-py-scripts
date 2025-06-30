#!/usr/bin/env python3
"""
PDF Merger

This script prompts the user to enter two paths: a child path and a parent path.
It then finds all PDF files in the child path and, if a filename matches a PDF in the parent path,
merges the child PDF into the parent PDF.

Dependencies:
- PyPDF: pip install PyPDF
- rich: pip install rich
"""

import os
import sys
import glob
from rich.console import Console
from rich.panel import Panel
from rich import print

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print("Error: This script requires the PyPDF library.")
    print("Please install it using: pip install pypdf")
    sys.exit(1)

console = Console()


def clear_console():
    """Clear the console screen."""
    console.clear()


def get_directory_path(prompt_message):
    """Prompt the user for a directory path and validate it."""
    while True:
        dir_path = input(prompt_message).strip()
        # Check if the path exists and is a directory
        if not os.path.exists(dir_path):
            console.print(f"Error: The path '{dir_path}' does not exist.", style="bold red")
            continue

        if not os.path.isdir(dir_path):
            console.print(f"Error: '{dir_path}' is not a directory.", style="bold red")
            continue

        return dir_path


def find_pdf_files(directory):
    """Find all PDF files in the specified directory."""
    pdf_pattern = os.path.join(directory, "*.pdf")
    pdf_files = glob.glob(pdf_pattern)

    # Also search for uppercase extension
    pdf_pattern_upper = os.path.join(directory, "*.PDF")
    pdf_files.extend(glob.glob(pdf_pattern_upper))

    return pdf_files


def merge_pdfs(child_pdf_path, parent_pdf_path):
    """Merge the child PDF into the parent PDF."""
    try:
        # Read the parent PDF
        parent_pdf = PdfReader(parent_pdf_path)

        # Read the child PDF
        child_pdf = PdfReader(child_pdf_path)

        # Create a PDF writer
        pdf_writer = PdfWriter()

        # Add all pages from the parent PDF
        for page in parent_pdf.pages:
            pdf_writer.add_page(page)

        # Add all pages from the child PDF
        for page in child_pdf.pages:
            pdf_writer.add_page(page)

        # Write the merged PDF back to the parent path
        with open(parent_pdf_path, "wb") as output_file:
            pdf_writer.write(output_file)

        return True
    except Exception as e:
        console.print(f"Error merging PDFs: {e}", style="bold red")
        return False


def main():
    clear_console()

    print(Panel("PDF Merger", style="bold blue"))
    console.print("This script merges PDFs from a child directory into matching PDFs in a parent directory.",
                  style="cyan")

    console.print()
    # Get directory paths from the user
    child_dir = get_directory_path("Please enter the child directory path containing PDFs: ")
    parent_dir = get_directory_path("Please enter the parent directory path containing PDFs: ")

    # Find PDF files in both directories
    child_pdfs = find_pdf_files(child_dir)
    parent_pdfs = find_pdf_files(parent_dir)

    if not child_pdfs:
        console.print(f"No PDF files found in child directory: {child_dir}", style="bold yellow")
        return

    if not parent_pdfs:
        console.print(f"No PDF files found in parent directory: {parent_dir}", style="bold yellow")
        return

    console.print(f"\nFound {len(child_pdfs)} PDF files in child directory.", style="violet")
    console.print(f"Found {len(parent_pdfs)} PDF files in parent directory.", style="purple")

    # Create dictionaries of filenames for easier matching
    parent_pdf_dict = {os.path.basename(pdf): pdf for pdf in parent_pdfs}

    # Counter for successful merges
    merge_count = 0

    # Process each child PDF file
    for child_pdf in child_pdfs:
        child_filename = os.path.basename(child_pdf)

        # Check if there's a matching filename in the parent directory
        if child_filename in parent_pdf_dict:
            parent_pdf = parent_pdf_dict[child_filename]
            console.print(f"\nMatch found: {child_filename}")

            # Merge the PDFs
            if merge_pdfs(child_pdf, parent_pdf):
                console.print(f"> Successfully merged {child_filename}", style="underline green")
                merge_count += 1
            else:
                console.print(f"Failed to merge {child_filename}", style="bold red")
        else:
            console.print(f"No match found for: {child_filename}", style="yellow")

    # Print summary
    if merge_count > 0:
        # console.print(f"\Successfully merged {merge_count} PDF files.", style="bold green")
        console.print()
        print(Panel(f"Successfully merged {merge_count} PDF files.", style="bold purple", title="Summary",
                    title_align="left", padding=(1, 1)))
    else:
        console.print("\nNo PDFs were merged.", style="bold yellow")


if __name__ == "__main__":
    main()
