# Init
Evaluation Repository

## :page_with_curl: _About_
- This is an Image Scanner built with Django
- It extracts Image texts using pytesseract

## :page_with_curl: _Installation Guide_

**1.** Fire up your favourite console & clone this repo somewhere:

__`❍ git clone https://github.com/Adminixtrator/Init.git`__

**2.** Enter this directory:

__`❍ cd ims`__ 

**3.** Install other python packages/dependencies using the requirement file:

__`❍ pip install -r requirements.txt`__

**4)** Install tesseract-ocr:

__`❍ sudo apt-get install tesseract-ocr`__

**5)** Get TESSDATA_PREFIX:

__`❍ sudo find / -name "tessdata"`__  *Copy the path*

**6)** Set TESSDATA_PREFIX:

__`❍ export TESSDATA_PREFIX=path_you_copied`__

**7)** Run the App:

__`❍ python manage.py runserver 2020`__

**8)** Open your browser and type in this URL. Upload an Image to be scanned:

__`❍ http://127.0.0.1:2020/`__

__*Happy developing!*__