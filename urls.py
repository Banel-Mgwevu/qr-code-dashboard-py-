from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
	path('viewitems/', views.v_items, name="v_items"),
	path('additems/', views.add_items, name="additems"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
