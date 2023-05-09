import os
import PyPDF2

# Define the input and output file paths
input_file_path = input("Type Input File Directory with .pdf\n")
output_folder_path = input("Name of output folder\n")

print("\n")
# Define how many page you want for each PDFs
page_per_pdf = int(input("Define how many page you want for each PDFs"))

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Open the input PDF file
with open(input_file_path, "rb") as input_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(input_file)

    # Get the number of pages in the input PDF file
    num_pages = pdf_reader.getNumPages()

    # Loop through the pages in the input PDF file, four at a time
    for i in range(0, num_pages, page_per_pdf):
        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfFileWriter()

        # Loop through the next four pages
        for j in range(i, min(i+page_per_pdf, num_pages)):
            # Get the page at the current index
            page = pdf_reader.getPage(j)

            # Add the page to the PDF writer object
            pdf_writer.addPage(page)

        # Create the output PDF file name
        output_file_name = f"output_{i//page_per_pdf}.pdf"
        output_file_path = os.path.join(output_folder_path, output_file_name)

        # Write the PDF writer object to the output PDF file
        with open(output_file_path, "wb") as output_file:
            pdf_writer.write(output_file)
