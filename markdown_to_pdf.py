
"""

Functions:
    render_markdown_to_pdf(markdown_file, pdf_file):
        Python script that converts a Markdown text file into a PDF document using the ReportLab library.
        The generated PDF is saved.

"""

import markdown
import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def render_markdown_to_pdf(markdown_file, pdf_file):
    with open(markdown_file, "r") as file:
        text = file.readlines()
    
    pdf = canvas.Canvas(pdf_file, pagesize=letter)
    
    y_position = 750
    indent = 100


    for line in text:
        line = line.strip()
        
        if not line:
            y_position -= 10
            continue
        
        heading_level = line.count("#") if line.startswith("#") else 0
        if heading_level > 0:
            line = line.lstrip("#").strip()
            font_size = max(20 - (heading_level * 2), 12)
            pdf.setFont("Helvetica-Bold", font_size)
        elif line.startswith("- "):
            pdf.setFont("Helvetica", 12)
            line = "• " + line[2:]
        elif "**" in line:
            line = re.sub(r"\*\*(.*?)\*\*", r"\1", line)
            pdf.setFont("Helvetica-Bold", 12)
        elif "*" in line:
            line = re.sub(r"\*(.*?)\*", r"\1", line)
            pdf.setFont("Helvetica-Oblique", 12)
        else:
            pdf.setFont("Helvetica", 12)

        pdf.drawString(indent, y_position, line)
        y_position -= 20

        # Check if we need to create a new page
        if y_position < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y_position = 750  # Reset position for new page

    pdf.save()
    print("PDF file has been generated successfully")



markdown_file = "sample.txt"
pdf_file = "output.pdf"
render_markdown_to_pdf(markdown_file, pdf_file)