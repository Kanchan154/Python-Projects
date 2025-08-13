from fpdf import FPDF
import os

class PDFMaker(FPDF):
    def header(self):
        self.set_font("Helvetica", 'B', 18)
        self.set_text_color(40, 40, 40)
        self.cell(0, 10, self.title, ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", 'I', 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def create_pdf(filename, title, content, image_path=None):
    pdf = PDFMaker()
    pdf.title = title
    pdf.add_page()

    # Content
    pdf.set_font("Helvetica", '', 12)
    pdf.set_text_color(50, 50, 50)
    for line in content.split("\n"):
        pdf.multi_cell(0, 8, line)
        pdf.ln(1)

    # Add Image (if provided)
    if image_path and os.path.exists(image_path):
        pdf.ln(10)
        pdf.image(image_path, x=30, w=150)  # Adjust position & size as needed

    pdf.output(filename)
    print(f"✅ PDF '{filename}' Created Successfully!!")

if __name__ == "__main__":
    # User input
    title = input("Enter PDF Title: ")
    print("Enter your content (type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    content = "\n".join(lines)

    image_path = input("Enter image file path (or press Enter to skip): ").strip()
    if image_path == "":
        image_path = None

    create_pdf("custom_output.pdf", title, content, image_path)
