from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .forms import QueryForm, CustomUserCreationForm
# Create your views here.
from .tokens import token_generator


def token_email(user, current_site, path, email_subject, template_name, to_email, ):
    message = render_to_string(template_name=template_name, context={
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
        'path': path
    }).strip()

    email = EmailMessage(subject=email_subject, body=message, to=[to_email], from_email="ugneuronet@gmail.com", )
    email.content_subtype = "html"
    email.send(fail_silently=False)


def index(request):
    if request.method == 'GET':
        form = QueryForm()
    else:
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.save()
        else:
            args = {'form': form}
            return render(request, 'authentication/index.html', args)

    args = {'form': form}

    return render(request, "authentication/index.html", args)


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.email_verified = True
            user.save()
            return redirect('login')
        else:
            args = {'form': form}
            return render(request, 'authentication/signup.html', args)
    else:
        form = CustomUserCreationForm()

    args = {'form': form}
    return render(request, "authentication/signup.html", args)


def user_login(request):
    if request.method == 'POST':
        next_page = request.POST.get('next')
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in")
                if next_page:
                    return HttpResponseRedirect(next_page)
                else:
                    #return redirect("/dashboard/")
                    return redirect("dashboard/")
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")
    else:
        form = AuthenticationForm()
    args = {'form': form}
    return render(request, "authentication/signin.html", args)


def forgot_password(request):
    return render(request, "authentication/forgot-password.html")


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")
