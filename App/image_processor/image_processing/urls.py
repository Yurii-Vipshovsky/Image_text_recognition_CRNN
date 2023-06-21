from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('process_image/', views.process_image, name='process_image'),
    path('images/<str:image_name>', views.get_image, name='get_image'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)