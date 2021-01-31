import pyqrcode 
import png 
from pyqrcode import QRCode 



s = "www.facebook.com"#only for example


url = pyqrcode.create(s) 
url.png('qr.png', scale = 10) 