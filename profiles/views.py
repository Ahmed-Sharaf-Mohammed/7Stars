import datetime
from audioop import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm
from .models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Avg, Q
from django.urls import reverse


# Create your views here.
# from third_party.views import make_messages, translate_po_file, compile_translations


@login_required()
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,  'profiles/profile.html', {'profile': profile})


@login_required()
def edite(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        print("No Profile")
        profile = None
    if request.method == 'POST':
        userform = UserForm(request.POST, request.FILES, instance=request.user)
        profileform = ProfileForm(
            request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            print("Saved")
            return redirect('profiles:profile')
        else:
            print("Error In Saved")
            print(profileform.errors)
            userform = UserForm(instance=request.user)
            profileform = ProfileForm(instance=profile)
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request, 'profiles/edit.html',
                  {
                      'userform': userform,
                      'profileform': profileform})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'profiles/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('password_change_done')


def trans (request):
    make_messages()
    translate_po_file()
    compile_translations()
    return render(request, 'profiles/tran.html')


def fallback_file_view(request):
    return render(request, 'profiles/none.html')