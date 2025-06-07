import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def generate_pdf(date_str):
    buffer = io.BytesIO()

    # Create PDF
    c = canvas.Canvas(buffer, pagesize=letter)
    c.drawString(100, 750, f"Daily Summary for {date_str}")

    # Create chart image using matplotlib
    chart_io = io.BytesIO()
    plt.figure(figsize=(4, 3))
    plt.plot([1, 2, 3], [4, 6, 5])
    plt.title("Sample Chart")
    plt.savefig(chart_io, format='png')
    chart_io.seek(0)

    # Draw chart on PDF
    c.drawImage(chart_io, 100, 500, width=300, height=200)
    c.save()

    buffer.seek(0)
    return buffer
