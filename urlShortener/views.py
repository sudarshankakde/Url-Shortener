
from django.shortcuts import render
import pyshorteners


def home(request):
    if request.method == "POST":
        url = request.POST['url']
        sevice = request.POST['sevice']
        if sevice == "tinnyUrl":
            s = pyshorteners.Shortener()
            SURL = s.tinyurl.short(url)
        elif sevice == "dage":
            s = pyshorteners.Shortener()
            SURL = s.dagd.short(url)
        elif sevice == "clckru":
            s = pyshorteners.Shortener()
            SURL = s.clckru.short(url)
        elif sevice == "qpsru":
            s = pyshorteners.Shortener()
            SURL = s.qpsru.short(url)
        else:
            pass
        return render(request, 'home.html', {'url': url, 'surl': SURL, 'copyUrl': True})

    else:
        return render(request, 'home.html')
