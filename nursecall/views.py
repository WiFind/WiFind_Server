import urllib, cStringIO

from PIL import Image, ImageDraw

from django.shortcuts import render
from django.http import HttpResponse

from .models import Device

# Create your views here.

def render_image(request, mac_addr):
    d = Device.objects.get(mac_addr=mac_addr)
    
    file = cStringIO.StringIO(urllib.urlopen(d.map_url).read())
    img = Image.open(file)

    radius = 5

    draw = ImageDraw.Draw(img)
    draw.ellipse((d.x_loc-radius, d.y_loc-radius, d.x_loc+radius, d.y_loc+radius), fill='blue', outline='blue')

    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    
    return response
