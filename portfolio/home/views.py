from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def home(req):
    return render(req, 'index.html')


def portfolio(req, page):
    if page == 'home':
        return render(req, 'index.html')
    elif page == 'aboutme':
        return render(req, 'Aboutme.html')
    elif page == 'certifications':
        return render(req, 'Certifications.html')
    elif page == 'projects':
        return render(req, 'Projects.html')
    elif page == 'contactme':
        return render(req, 'ContactMe.html')
    else:
        # return render(req, 'index.html')
        # 👈 Fix: Return an HttpResponse
        return HttpResponse("Page not found", status=404)


def send_contact_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            subject = f'New Contact form submission from {name}'
            body = f"""
Hi Charan, You got received one submission from:
name: {name}
email: {email}
message: {message}
"""
            try:
                send_mail(subject, body, 'charanchery70@gmail.com',
                          ['narayanamjnanacharan@gmail.com'],
                          fail_silently=False,
                          )

                confirmation_subject = "Thank you for Contacting me!"
                confirmation_message = f"""Hi {name}
Thank you for reaching out! I have received your message and will get back to you as soon as possible.
                
Here is a copy of your message:
"{message}"
                
Best Regards,
Jnana Charan Narayanam
"""

                send_mail(confirmation_subject, confirmation_message,
                          'charanchery70@gmail.com',
                          [email],
                          fail_silently=False,
                          )
                messages.success(
                    request, "✅ Your message has been sent successfully!")
                return redirect('/contactme/')
            except Exception as e:
                print(f"Email error: {e}")  # ✅ Print the error in the terminal
                messages.error(request, f"❌ Failed to send email: {e}")
                return redirect('/contactme/')

    return redirect('/contactme/')
