from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings

# Create your views here.
def index (request):
    #form_name = request.POST['form-type']
    #if request.POST['form-type'] == u"blog-form"

    if request.method == "POST":
        
        name = request.POST.get("name")
        email = request.POST.get("email")
        city = request.POST.get("city")
        interests = request.POST.get("interests")
        #message = request.POST.get("message")
        print("These are the form Fields: ")
        print(name, email)

        #Email ourselves the submitted contact message

        subject = 'Contact Form Received'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [settings.DEFAULT_TO_EMAIL]

        context = {
            'user': name,
            'email': email,
            'city': city,
            'interests': interests,
            #'message': message
        }
        
        if request.POST.get("sendinfo"):
            contact_message = get_template('contact_message.txt').render(context)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
            #messages.success(request, "Thanks for your email, I'll be in touch with you soon! -Troy   ")
            return redirect('home')

        if request.POST.get("beta"):
            contact_message = get_template('contact_beta.txt').render(context)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
            #messages.success(request, "Thanks for your email, I'll be in touch with you soon! -Troy   ")
            return redirect('home')

        if request.POST.get("basic"):
            contact_message = get_template('basic_info.txt').render(context)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
            #messages.success(request, "Thanks for your email, I'll be in touch with you soon! -Troy   ")
            return redirect('home')

    return render(request, 'index.html' )




