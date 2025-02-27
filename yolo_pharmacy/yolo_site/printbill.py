import os
import pdfkit
from django.template.loader import get_template
from django.conf import settings

def generate_bill_pdf(bill):
    """Generate a PDF invoice for the given bill"""
    
    # Load HTML template and render it with bill details
    template = get_template('printbill.html')
    html_content = template.render({'bill': bill})

    # Define file path
    pdf_filename = f'bill_{bill.pk}.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'bills', pdf_filename)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    # PDF options
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
    }

    # Generate the PDF
    pdfkit.from_string(html_content, pdf_path, options=options)

    return pdf_path  # Return the path of the generated PDF
