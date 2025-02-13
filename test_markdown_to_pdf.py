import pytest
import os

# testing the process_line function

def test_process_line():
    line = "##This is a heading"
    assert process_line(line) == ([("Helvetica-Bold", 16, "This is a heading")], -20)
    
    line = "- This is a bullet point"
    assert process_line(line) == ([("Helvetica", 12, "     • This is a bullet point")], -20)
    
    line = "**This is a bold line**"
    assert process_line(line) == ([("Helvetica-Bold", 12, "This is a bold line")], -20)
    
    line = "*This is an italic line*"
    assert process_line(line) == ([("Helvetica-Oblique", 12, "This is an italic line")], -20)
    
    line = "This is a normal line"
    assert process_line(line) == ([("Helvetica", 12, "This is a normal line")], -20)

    line = "This is a **bold** word"
    assert process_line(line) == ([('Helvetica', 12, 'This is a '), ('Helvetica-Bold', 12, 'bold'), ('Helvetica', 12, ' word')], -20)

    line = "This is a *italicized* word"
    assert process_line(line) == ([('Helvetica', 12, 'This is a '), ('Helvetica-Oblique', 12, 'italicized'), ('Helvetica', 12, ' word')], -20)

    line = ""
    assert process_line(line) == (None, -10)
    

# testing the render_markdown_to_pdf function

def test_render_markdown_to_pdf():
    test_md_file = "test_sample.txt"
    test_pdf_file = "test_output.pdf"

    with open(test_md_file, "w") as f:
        f.write("# Test Heading\n\n- Test list item\n**Bold text**\n*Italic text*")
        # Add enough lines to trigger a new page
        for _ in range(50):
            f.write("This is a normal line\n")

    render_markdown_to_pdf(test_md_file, test_pdf_file)

    assert os.path.exists(test_pdf_file)

    os.remove(test_md_file)
    os.remove(test_pdf_file)