from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login_user')
def index(request):
    return render(request, 'customers/index.html')
