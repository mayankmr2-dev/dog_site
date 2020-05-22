from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # nameip = fname + ' ' + lname + '\n' + email
        # mail = subject + '\n' + message

        send_mail(
            fname + lname,
            subject + message,
            email,
            ['mayankmr2@gmail.com']
        )
        return render(request, 'home.html', {'fname': fname})

    return render(request, 'home.html')
