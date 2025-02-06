import markdown
import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

"""

Functions:

    process_line(line):
        Function that processes a line of text from a Markdown file and returns the 
        processed line and the vertical offset. The function is used to convert Markdown text 
        into a format that can be used by the ReportLab library.

    render_markdown_to_pdf(markdown_file, pdf_file):
        Python script that converts a Markdown text file into a PDF document using the ReportLab library.
        The generated PDF is saved.

"""
def process_line(line):
    line = line.strip()
    if not line:
        return None, -10
    
    heading_level = line.count("#") if line.startswith("#") else 0
    if heading_level > 0:
        line = line.lstrip("#").strip()
        font_size = max(20 - (heading_level * 2), 12)
        return [("Helvetica-Bold", font_size, line)], -20
    elif line.startswith("- "):
        return[("Helvetica", 12, "• " + line[2:])], -20

    # Check for bold and italic text by spliting the line
    segments = re.findall(r"(\*\*.*?\*\*|\*.*?\*|[^*]+)", line)
    formatted_segments = []

    for segment in segments: 
        if segment.startswith("**") and segment.endswith("**"):
            formatted_segments.append(("Helvetica-Bold", 12, segment[2:-2]))
        elif segment.startswith("*") and segment.endswith("*"):
            formatted_segments.append(("Helvetica-Oblique", 12, segment[1:-1]))
        else:
            formatted_segments.append(("Helvetica", 12, segment))
    
    return formatted_segments, -20
    


def render_markdown_to_pdf(markdown_file, pdf_file):
    with open(markdown_file, "r") as file:
        text = file.readlines()
    
    pdf = canvas.Canvas(pdf_file, pagesize=letter)
    y_position = 750
    indent = 100

    for line in text:
        result, y_offset = process_line(line)
        if result is None:
            y_position = y_position + y_offset
            continue
        
        if isinstance(result, list):
            x_position = indent
            for font, size, segment in result:
                pdf.setFont(font, size)
                pdf.drawString(x_position, y_position, segment)
                x_position += pdf.stringWidth(segment, font, size) + 5

        y_position = y_position + y_offset
        # Check if we need to create a new page
        if y_position < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y_position = 750  # Reset position for new page

    pdf.save()
    print("PDF file has been generated successfully")

render_markdown_to_pdf("sample.txt", "output.pdf")

