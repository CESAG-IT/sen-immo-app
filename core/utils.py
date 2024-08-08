from django.core.mail import send_mail
from django.conf import settings
from django.http import BadHeaderError, HttpResponse, HttpResponseRedirect

def send_my_email(recipient, lastname ):
    print("Sending email to: " + recipient)
    subject = f"Welcome to the SEN IMMO system {lastname}"
    message = f"""
        Welcome to the SEN IMMO
        Vous avez crée une nouvelle proprieté sur SEN IMMO
        Felicitation
    """
    try:
        send_mail(subject, message,
            "no-reply@senimmo.com", [recipient], fail_silently=False)
    except BadHeaderError:
            return HttpResponse('Invalid header found.')
    return HttpResponseRedirect('/home/')