from django.shortcuts import render,redirect
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .models import stockitems
from django.contrib import messages
from django.core.mail import send_mail


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None





qr_obj=stockitems.objects.all() #making my database to object
context ={
'qr_obj':qr_obj
}




#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('app/pdf_template.html', context)
		return HttpResponse(pdf, content_type='application/pdf')




#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('app/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response




def add_items(request): #function to add stock items

	stock_info=request.POST.get('stock_info')
	quantity=request.POST.get('quantity')
	brand=request.POST.get('brand')
	barcode=request.POST.get('barcode')
	product_name=request.POST.get('product_name')

	if stock_info ==' ':
		messages.error(request,'Opps, you forgot to fill in the the stock info')
		return redirect('additems')

	if quantity==' ':
		messages.error(request,'Opps, you forgot to fill in the the quantity')
		return redirect('additems')

	if brand==' ':
		messages.error(request,'Opps, you forgot to fill in the the brand name')
		return redirect('additems')

	if barcode==' ':
		messages.error(request,'Opps, you forgot to fill in the the barcode info')
		return redirect('additems')

	if product_name==' ':
		messages.error(request,'Opps, you forgot to fill in the the product name')
		return redirect('additems')



	itemsdata=stockitems(stock_info=stock_info, quantity=quantity,brand=brand,barcode=barcode,product_name=product_name)
	itemsdata.save()

	return render(request,'app/add_stock.html')

def v_items(request):

	return render(request, 'app/view_stock.html', context)
