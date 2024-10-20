from weasyprint import HTML

def generate_pdf_report():
    input_html = 'output/report.html'
    output_pdf = 'output/report.pdf'

    try:
        # Read the HTML content from the report file
        HTML(input_html).write_pdf(output_pdf)
        print("PDF report generated successfully.")
    except Exception as e:
        print(f"Failed to generate PDF report: {e}")

if __name__ == "__main__":
    generate_pdf_report()
