import os
import re
from pygments import highlight
from pygments.lexers import CppLexer
from pygments.formatters import HtmlFormatter
from weasyprint import HTML

def extract_email(filename):
    email_match = re.search(r'([a-zA-Z0-9._%+-]+@ucr\.edu)', filename)
    return email_match.group(1) if email_match else "Email not found"

def determine_target_dir(filename, base_output_dir, target_folders_name):
    for keyword, folder_name in target_folders_name.items():
        if keyword in filename:
            # Check if the file ends with .h and append '/header' to the folder name
            if filename.endswith('.h'):
                return os.path.join(base_output_dir, folder_name, 'header')
            else:
                return os.path.join(base_output_dir, folder_name)
    return None

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def convert_code_to_html(code, student_email):
    highlighted_code = highlight(code, CppLexer(), HtmlFormatter(style='default', full=True, linenos='inline', cssclass='code'))
    css_style = '''<style>
                    .code { max-width: 90%; margin: auto; }
                   .code pre { white-space: pre-wrap; }
                   </style>'''
    email_html = f"<div style='text-align:left; margin-top:20px;'>Student NetID: <strong style='font-family: Verdana;'>{student_email.split('@')[0]}</strong></div>"
    gap = "<div style='margin-top: 3em;'></div>"
    return css_style + email_html + gap + highlighted_code

def write_pdf(html_content, output_file_path):
    HTML(string=html_content).write_pdf(output_file_path)

def convert_to_pdf(source_dir, base_output_dir, target_folders_name, file_extensions):
    skipped_files_path = os.path.join(base_output_dir, 'files_skipped.txt')
    
    with open(skipped_files_path, 'a') as skipped_files:  # Open the file in append mode
        for filename in os.listdir(source_dir):
            file_ext = os.path.splitext(filename)[1]
            if file_ext in file_extensions:
                student_email = extract_email(filename)
                target_dir = determine_target_dir(filename, base_output_dir, target_folders_name)

                if target_dir:
                    file_path = os.path.join(source_dir, filename)
                    output_file_path = os.path.join(target_dir, filename.replace(file_ext, file_extensions[file_ext]))

                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)

                    code = read_file(file_path)
                    html_content = convert_code_to_html(code, student_email)
                    write_pdf(html_content, output_file_path)

                    print(f"Converted {filename} to PDF in {target_dir}")
                else:
                    print(f"No target directory found for {filename}, skipping.")
                    skipped_files.write(filename + '\n')  # Write the skipped filename to the file


file_extensions = {".cpp": ".pdf", ".h": "_h.pdf"}

# example path and usage
source_directory = "/Users/anantmahale/Desktop/cpp2pdf/exam2"
base_output_directory = "/Users/anantmahale/Desktop/cpp2pdf/exam2"

target_folders_name = {"TeaOrder_Class_Implementation_Editor": "TeaOrder_Class_Implementation_Editor",
                       "Counting_Blank_Lines_Editor":"Counting_Blank_Lines_Editor",
                       "Counting_large_words_Editor":"Counting_large_words_Editor",
                       "copy_file_editor":"copy_file_editor"
                       }


convert_to_pdf(source_directory, base_output_directory, target_folders_name, file_extensions)
