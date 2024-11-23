from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
    path('category/<val>', views.CategoryTitle.as_view(), name='category-title'),
    path('product/<int:pid>', views.ProductDetails.as_view(), name='product-details'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
