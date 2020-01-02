from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests
import pytesseract as pt
from PIL import Image
from PIL import ImageFilter

# Create your views here.
#pt.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'
pt.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

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
    
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file'] 
        if allowed_file(file.name):
            try:
                extracted_text = ocr_core(file)
                if extracted_text != '':
                    extracted_text=extracted_text
                else:
                    extracted_text='Could not identify text in image.. \nPlease check image and try again..'
            except:
                extracted_text='Error occured! Please check your file and try again'
        return render(request, 'index.html', {'extracted_text': extracted_text})
    
    return render(request, 'index.html')

