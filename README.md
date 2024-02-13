# Code Documentation: Introduction

This script serves the specific purpose of automating the conversion of C++ source files into PDF format for University of California, Riverside (UCR) courses. It offers syntax highlighting and integrates the student's NetID extracted from the filename, enhancing its utility for instructors and TAs in evaluating code submissions. It operates under the assumption that student emails adhere to the pattern xxx@ucr.edu, common in UCR courses.

Additionally, instructors utilizing PrairieLearn's <code>pl-file-editor</code> element may find this script beneficial for converting cpp files to pfs, facilitating the upload of files to Gradescope for grading purposes.

## Features
- A log file that lists any files that were skipped.
- Compatibility with both CPP and .h file formats.
- A dedicated folder for organizing header files.

## Prerequisites

Before you can use this script, ensure you have the following installed:
- Python 3.9.XX
- Pygments
- WeasyPrint

**Note:** WeasyPrint has specific installation requirements that might not be resolved with pip alone. Please refer to the [official WeasyPrint documentation](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation) for OS specific installation instructions.

## Usage

1. Set the `source_directory` variable to the path containing your `.cpp` files.
2. Set the `base_output_directory` variable to the path where you want the PDFs to be saved.
   - The script will create the output directory if it doesn't exist.
3. Update ```target_folders_name``` based on the keywords in file name
4. Run the script:
   ```bash
   python cpp2pdf_converter.py

## Function Descriptions

1. **extract_email(filename):** Extracts and returns the student's NetID from the given filename, assuming the email follows the pattern xxx@ucr.edu.

2. **determine_target_dir(filename, base_output_dir, target_folders_name):** Determines the target directory for the output PDF based on the filename and predefined folder names. Appends '/header' to the folder path for header files.

3. **read_file(file_path):** Reads and returns the content of a file located at file_path.

4. **convert_code_to_html(code, student_email):** Converts the given code string to syntax-highlighted HTML, including the student's NetID.

5. **write_pdf(html_content, output_file_path):** Converts the given HTML content to a PDF file at the specified output path.

6. **convert_to_pdf(source_dir, base_output_dir, target_folders_name, file_extensions):** Main function that iterates through files in the source directory, converts them to PDF if they match the specified extensions, and organizes them into target directories.


## Usage Example

To use this script, define the source directory containing the C++ files, the base output directory for the PDFs, the mapping of keywords to target folder names, and the file extensions to be converted. Then, call `convert_to_pdf` with these parameters.

```python
file_extensions = {".cpp": ".pdf", ".h": "_h.pdf"}

source_directory = "/path/to/source"
base_output_directory = "/path/to/output"

target_folders_name = {
    "Keyword1": "Folder1",
    "Keyword2": "Folder2",
    # Add more mappings as needed
}

convert_to_pdf(source_directory, base_output_directory, target_folders_name, file_extensions)

```

## Additional Notes
- Ensure that the source directory and base output directory are correctly specified.
- The script assumes that the student's email is embedded in the filename and follows the xxx@ucr.edu pattern.
- Skipped files (those without a matching target directory or unsupported extensions) are logged in files_skipped.txt in the base output directory.

## Compatibility and Tested Versions

This program has been tested and confirmed to work with the following software versions:

- **Python**: `3.9.12`
- **Pygments**: `2.11.2`
- **WeasyPrint**: `60.2`
- **MacOS**: `14.2.1`