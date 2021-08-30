from django.http import HttpResponse
from django.shortcuts import redirect

def unauth_only(view_func):
  def wrapper_func(request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('/')
    else:
      return view_func(request, *args, **kwargs)
  return wrapper_func

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
      if request.user.is_staff:
        return view_func(request, *args, **kwargs)
      else:
        return redirect("/")
    return wrapper_func
