from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# the format of writing the code
# def Form(request):
#     if request.method == 'POST':
#         send_mail(subject, message, configured email, receiver, fail_silently)
#     context = {}
#     return render(request, 'app/index.html', context)


# real code
def Form(request):
    if request.method == 'POST':
        message = request.POST['message']
        send_mail('Django Contact Form', message, settings.EMAIL_HOST_USER, ['njokugeraldchinedum@gmail.com'], fail_silently=False)
    context = {}
    return render(request, 'app/index.html', context)