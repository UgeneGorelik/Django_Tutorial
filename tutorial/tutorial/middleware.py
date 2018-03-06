from django.conf import settings
import re
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse

EXEMPT_URLS=[re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings,'LOGIN_EXEMPT_URL'):
    EXEMPT_URLS+=[re.compile(url for url in settings.LOGIN_URL)]

class LoginRequiredMiddleware:
    def __init__(self,get_resonse):
        self.get_response=get_resonse

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request,'user')
        path=request.path_info.lstrip('/')
        print(path)


        # if not request.user.is_authenticated:
        #     if not any(url.match(path) for url in EXEMPT_URLS):
        #         return redirect(settings.LOGIN_URL)

        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if path=='logout':
            logout(request)


        if request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated or url_is_exempt:
            return None
        else:
            return redirect(settings.LOGIN_URL)