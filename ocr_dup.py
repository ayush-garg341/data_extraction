import cv2
import pytesseract
import PIL
from PIL import Image
import numpy
import urllib
import urllib.request
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
# filename = 'C:\pdftotext\code and files\ctc_2.png'
def return_text(url):
    file_name = r'C:Users\Admin\PycharmProjects\web_apis\test.png'
    headers = { 'User-Agent' : 'Mozilla / 5.0 (Windows NT 6.1; WOW64; rv: 23.0) Gecko / 20100101 Firefox / 23.0' } 
    req = urllib.request.Request (url = url, headers = headers)
    with urllib.request.urlopen(req) as response, open(file_name, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
    #data = urllib.request.urlretrieve(url, file_name)
    basewidth = 400
    img = Image.open(file_name)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    text = pytesseract.image_to_string(img)
    return text