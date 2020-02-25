from django.shortcuts import render

# Create your views here.
from . import forms
from emailapp.models import Student
import django
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def StudentRegistration(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.address='bangalore'
            save_it.save()
            send_mail(' REGISTERED',
                      'congrats you are noe registered',
                      settings.EMAIL_HOST_USER,
                      [save_it.email], fail_silently=False)
            return HttpResponseRedirect('/mail/')
    return render(request,'emailapp/forms.html',{'form':form})


def mail(request):
    return render(request,'emailapp/email.html')

