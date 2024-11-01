import random
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from .models import Login
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from django.contrib.auth.models import User
# Create your views here.
# @login_required(login_url='login')


def SignupPage(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')

        # Generate a unique username by checking the database
        while True:
            random_number = random.randint(0, 1000)
            uname = f"{fname}-{lname}".lower() + f"-{random_number}"
            if not User.objects.filter(username=uname).exists():
                break  # Exit the loop if the username is unique

        # Validation checks
        if not fname:
            messages.error(request, "First Name is required.")
            return render(request, 'registration/signup.html', {'form': form})

        if not lname:
            messages.error(request, "Last Name is required.")
            return render(request, 'registration/signup.html', {'form': form})

        if not pass1:
            messages.error(request, "Password is required.")
            return render(request, 'registration/signup.html', {'form': form})

        if not email:
            messages.error(request, "Email is required.")
            return render(request, 'registration/signup.html', {'form': form})

        if User.objects.filter(email=email).exists():
            messages.info(request, f"The email {email} is already registered in our system.")
            return render(request, 'registration/signup.html', {'form': form})

        # If form is valid, create and save user
        if form.is_valid():
            user = form.save(commit=False)  # Create user instance without saving yet
            user.username = uname
            user.first_name = fname
            user.last_name = lname
            user.email = email
            user.set_password(pass1)  # Set the password correctly
            user.save()

            # Log in the new user
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('profiles:edite')

        # Show form errors if validation fails
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')

    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = None
        # Check if the user entered an email or username
        if '@' in username:
            # If the input contains '@', assume it's an email address
            user = User.objects.filter(email=username).first()
        else:
            # Otherwise, assume it's a username
            user = User.objects.filter(username=username).first()
        # loop through all User objects in the Login module
        if user is not None:
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                messages.success(
                    request, "Authentication successful. You are now logged in to the website.")
                return redirect('profiles:profile')

                # username and/or password do not exist, so return an error response
            
        messages.warning(
            request, f"Authentication failed due to either an incorrect username or password, or the non-existence of a user with the username '{username}'.")
        return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')


def LogoutPage(request):
    logout(request)
    return redirect('pages:index')


# def checkExistUser(request):
#     username = request.POST['username']
#     email = request.POST['email']
#     for user in Login.objects.all():
#         if user.username == username or user.email == email:
#             # username and password exist, so return a success response
#             return True

#         # username and/or password do not exist, so return an error response
#     return False
