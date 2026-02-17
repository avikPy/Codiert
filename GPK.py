from hwid import get_hwid as gh
from base64 import urlsafe_b64encode as b64
import image, os

def generate_key(flag):
    if not(flag):
        return b64( ''.join(list(gh())[:32] ).encode('utf-8'))

def create():image.encode_image("ineedpass.png", "./nothing.png", str(generate_key(False))[2:-1])









