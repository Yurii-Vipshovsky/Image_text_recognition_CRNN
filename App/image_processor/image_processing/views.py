"""from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload_image.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload_image.html')"""


from django.shortcuts import render
from .forms import UploadImageForm
from .models import ProcessedImage
import os
from django.http import HttpResponse
from django.conf import settings
from image_processing.apps import ImageProcessingConfig
from .predict import single_image_Prediction

def process_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image1 = form.cleaned_data['image']
            config = ImageProcessingConfig('image_processing', None)
            config.ready()
            model = config.model

            # Використання моделі у вашому view
            # Наприклад, виклик функції прогнозування моделі
            
            processed_image = ProcessedImage(image=image1, processed_text='SPARTAK')
            processed_image.save()
            processed_image.image.name = processed_image.image.name.split('/')[1]
            image_path = os.path.join(settings.MEDIA_ROOT,'images', processed_image.image.name)
            image_path = image_path.replace('/','\\')
            processed_image.processed_text = single_image_Prediction(model, image_path)
            return render(request, 'image_processing/processed_image.html', {'processed_image': processed_image})
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form})


def get_image(request, image_name):
    image_path = os.path.join(settings.MEDIA_ROOT,'images', image_name)
    image_path = image_path.replace('/', '\\')
    with open(image_path, 'rb') as f:
        return HttpResponse(f.read(), content_type='image/jpeg')