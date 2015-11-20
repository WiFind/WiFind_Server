import urllib, cStringIO

from PIL import Image, ImageDraw

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sites.models import get_current_site

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

def getList(request):
    contents =''
    d = Device.objects.all()
    for eachDevice in d:
        mac_addr = eachDevice.mac_addr
        owner = eachDevice.owner.name
        map_url = eachDevice.map_url
        help = eachDevice.help_req
        # style taken from http://designshack.net/articles/css/5-simple-and-practical-css-list-styles-you-can-copy-and-paste/
        newLine = '<li style = "padding:10px; overflow:auto;"><img src = "http://40.media.tumblr.com/9441a09bddeafcfe4ea3a5a826195673/tumblr_nhgjoiad8H1s420s7o1_500.png" />'
        newLine += '<h3>' + owner + '</h3>'
        location_url = 'http://' + get_current_site(request).domain + '/loc/' + mac_addr + '.png'
        newLine += '<p><a href ="' +location_url +'" style="font-size: 24px !important;">Get Location</a><br/>'
        if help==True:
            newLine += '<div style="font-size: 20px !important; color:red">I NEED HELP!</div>'
        newLine += 'patient descriptions here</p>'
        newLine += '</li>'
        contents += newLine
    style = '<style>li:hover{background: #eee;}\ndiv{margin: 20px}\nh3{font: bold 20px/1.5 Helvetica, Verdana, sans-serif;}\nli p{font: 200 12px/1.5 Georgia, Times New Roman, serif;}\nli img{float:left;margin:0 15px 0 0;width:250px;height:200px;}</style>'
    html = '<html><head>'+ style +'</head><body><div style = "margin:20px;"><ul style = "list-style-type:none width:500px;">' + contents + '</ul></div></body></html>'
    return HttpResponse(html)
    pass
