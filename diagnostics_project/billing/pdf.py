from reportlab.pdfgen import canvas
from django.http import HttpResponse

def generate_invoice(request, bill_id):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{bill_id}.pdf"'
    
    p = canvas.Canvas(response)
    p.drawString(100, 800, f"Invoice for Bill ID: {bill_id}")
    p.showPage()
    p.save()
    return response
