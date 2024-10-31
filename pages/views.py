from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'pages/index.html')
