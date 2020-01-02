from django.shortcuts import render
from django.http import HttpResponse
import requests
import pytesseract as pt
from PIL import Image
from PIL import ImageFilter

# Create your views here.
def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    '''
    img = _get_image(filename)
    img.filter(ImageFilter.SHARPEN)
    '''
    img = Image.open(filename)
    return pt.image_to_string(img)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def index(request):
    
    return render(request, 'index.html')

