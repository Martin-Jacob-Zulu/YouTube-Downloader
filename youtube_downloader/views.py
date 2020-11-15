from django.http import Http404
from django.shortcuts import render, redirect
from .models import Guide, Jumbotron
from pytube.cli import on_progress
from pytube import YouTube
import os


url = ''


def home_view(request):
    guides = Guide.objects.all()
    jumbotron = Jumbotron.objects.all()
    context = {
        'guides': guides,
        'jumbotron': jumbotron
    }
    template = 'home.html'
    return  render(request, template, context)


def yt_download(request):

    global url
    url = request.GET.get('url')
    try:
        obj = YouTube(url, on_progress_callback=on_progress)
        resolutions = []
        strm_all = obj.streams.filter(file_extension='mp4')
        for i in strm_all:
            resolutions.append(i.resolution)
        resolutions = list(dict.fromkeys(resolutions))

        embed_link = url.replace("watch?v=", "embed/")
        path = 'D:\\'
        return render(request, 'yt_download.html', {'resolutions': resolutions, 'embd': embed_link})
    except:
        raise Http404


def download_complete(request, res):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    print(f'DIRECT : ', f'{dirs}/Downloads')
    if request.method == "POST":
        YouTube(url).streams.first().download(homedir + '/Downloads')
        return render(request, 'download_complete.html')
    else:
        raise Http404