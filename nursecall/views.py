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

    radius = 15

    draw = ImageDraw.Draw(img)
    draw.ellipse((d.x_loc-radius, d.y_loc-radius, d.x_loc+radius, d.y_loc+radius), fill='red', outline='red')

    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    
    return response

def getList(request):
    contents =''
    d = Device.objects.all()
    for eachDevice in d:
        mac_addr = eachDevice.mac_addr
        if eachDevice.owner is None:
            owner = 'None'
        else:
            owner = eachDevice.owner.name
        map_url = eachDevice.map_url
        if eachDevice.help_req == True:
            # style taken from http://designshack.net/articles/css/5-simple-and-practical-css-list-styles-you-can-copy-and-paste/
            location_url = 'http://' + get_current_site(request).domain + '/loc/' + mac_addr + '.png'
            newLine = '<li style = "padding:10px; overflow:auto;"><img src = "' + location_url +'" />'
            #newLine = '<li style = "padding:10px; overflow:auto;"><img src = "" />'
            newLine += '<h3>' + owner + '</h3>'
            newLine += '<p><a href ="' +location_url +'" style="font-size: 24px !important;">Get Location</a><br/>'
            newLine += '<div style="font-size: 20px !important; color:red">I NEED HELP!</div>'
            newLine += '<div>patient descriptions here: addr  ' + mac_addr +'</div></p>'
            newLine += '</li>'
            contents += newLine
    d = Device.objects.all()
    for eachDevice in d:
        mac_addr = eachDevice.mac_addr
        owner = eachDevice.owner.name
        map_url = eachDevice.map_url
        if eachDevice.help_req == 0:
            # style taken from http://designshack.net/articles/css/5-simple-and-practical-css-list-styles-you-can-copy-and-paste/
            location_url = 'http://' + get_current_site(request).domain + '/loc/' + mac_addr + '.png'
            newLine = '<li style = "padding:10px; overflow:auto;"><img src = "' + location_url + '" />'
            newLine += '<h3>' + owner + '</h3>'
            newLine += '<p><a href ="' +location_url +'" style="font-size: 24px !important;">Get Location</a><br/>'
            newLine += '<div>patient descriptions here: addr  ' + mac_addr +'</div></p>'
            newLine += '</li>'
            contents += newLine
    style = '<style>li:hover{background: #eee;}\ndiv{margin: 20px}\nh3{font: bold 20px/1.5 Helvetica, Verdana, sans-serif;}\nli p{font: 200 16px/1.5 Georgia, Times New Roman, serif;}\nli img{float:left;margin:0 15px 0 0;width:250px;height:200px;}</style>'
    html = '<html><meta http-equiv="Refresh" content="120"><head>'+ style +'</head><body><div style = "margin:20px;"><ul style = "list-style-type:none width:500px;">' + contents + '</ul></div></body></html>'
    return HttpResponse(html)
    pass
