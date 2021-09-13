from django.shortcuts import render

from .models import Music

def music_view(request, name):
  aud =  Music.objects.get(name=name)
  context = {
  "aud": aud
}  
  return render(request, 'music.html', context)

