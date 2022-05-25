from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == 'POST':
        message_name = request.POST['']
    return render(request, "index.html")