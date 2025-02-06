import pytest
import markdown_to_pdf
import os

def test_process_line():
    line = "## This is a heading"
    assert markdown_to_pdf.process_line(line) == ([("Helvetica-Bold", 16, "This is a heading")], -20)
    
    line = "- This is a bullet point"
    assert markdown_to_pdf.process_line(line) == ([("Helvetica", 12, "• This is a bullet point")], -20)
    
    line = "**This is a bold line**"
    assert markdown_to_pdf.process_line(line) == ([("Helvetica-Bold", 12, "This is a bold line")], -20)
    
    line = "*This is an italic line*"
    assert markdown_to_pdf.process_line(line) == ([("Helvetica-Oblique", 12, "This is an italic line")], -20)
    
    line = "This is a normal line"
    assert markdown_to_pdf.process_line(line) == ([("Helvetica", 12, "This is a normal line")], -20)

    line = "This is a **bold** word"
    assert markdown_to_pdf.process_line(line) == ([('Helvetica', 12, 'This is a '), ('Helvetica-Bold', 12, 'bold'), ('Helvetica', 12, ' word')], -20)

    line = "This is a *italicized* word"
    assert markdown_to_pdf.process_line(line) == ([('Helvetica', 12, 'This is a '), ('Helvetica-Oblique', 12, 'italicized'), ('Helvetica', 12, ' word')], -20)

    line = ""
    assert markdown_to_pdf.process_line(line) == (None, -10)
    
def test_render_markdown_to_pdf():
    test_md_file = "sample.txt"
    test_pdf_file = "test_output.pdf"
    markdown_to_pdf.render_markdown_to_pdf(test_md_file, test_pdf_file)
    assert os.path.exists(test_pdf_file)
    os.remove(test_pdf_file)

