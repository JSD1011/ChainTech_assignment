from django.shortcuts import render,redirect
from .forms import UserSubmissionForm
from .models import UserSubmission

from django.utils import timezone
import random

def index(request):
    current_time = timezone.now()
    random_quote = random.choice([
        "Life is what happens when you're busy making other plans.",
        "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "The way to get started is to quit talking and begin doing."
    ])
    return render(request, 'index.html', {
        'current_time': current_time,
        'random_quote': random_quote,
    })
def form_page(request):
    if request.method == 'POST':
        form = UserSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
            form = UserSubmissionForm()

    return render(request,'form_page.html',{'form':form})
def thank_you(request):
    return render(request,'thank_you.html')
    # return redirect('index')

def view_submissions(request):
    submissions = UserSubmission.objects.all()
    return render(request,'view_submissions.html',{'submissions':submissions})

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')