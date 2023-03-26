from io import BytesIO
from django.http import HttpResponseNotFound, HttpResponse
from PIL import Image
import os


def image_view(request, path):
    image_path = os.path.join('/projects/Django/BaliAdmin/images', path)
    if os.path.exists(image_path):
        with Image.open(image_path) as img:
            img = img.convert('RGB')
            jpeg_image = BytesIO()
            img.save(jpeg_image, 'JPEG')
            response = HttpResponse(jpeg_image.getvalue(), content_type='image/jpeg')
            return response
    else:
        return HttpResponseNotFound('File not found')
