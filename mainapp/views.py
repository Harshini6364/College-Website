from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailForm

def home(request):
    return render(request, "mainapp/home.html")

def colleges(request):
    college_list = ["SVEW", "VITB", "BVRIT", "VIT-AP"]
    return render(request, "mainapp/colleges.html", {"colleges": college_list})

def students(request):
    students_data = [
        {"name": "Bhashini", "branch": "CSE", "age": 20},
        {"name": "Harshini", "branch": "ECE", "age": 17},
        {"name": "Sanvitha", "branch": "IT", "age": 19},
        {"name": "Koushali", "branch": "EEE", "age": 16},
        {"name": "Viharika", "branch": "EEE", "age": 22},
    ]
    return render(request, "mainapp/students.html", {"students": students_data})

def address(request):
    return render(request, 'mainapp/address.html')

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            branch = form.cleaned_data['branch']

            branch_emails = {
                'cse': 'chavvakoushali@gmail.com',
                'ece': 'bhashinichavala@gmail.com',
                'eee': 'chintaharshini3@gmail.com',
                # 'mech': '24b01a1218@svecw.edu.in',
                # 'civil': '24b01a1217@svecw.edu.in',
            }

            receiver_email = branch_emails.get(branch)

            if receiver_email:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [receiver_email],
                    fail_silently=False,
                )

            return redirect('emailsent')
    else:
        form = EmailForm()

    return render(request, 'mainapp/contactus.html', {'form': form})

def emailsent(request):
    return HttpResponse("Email Sent Successfully")