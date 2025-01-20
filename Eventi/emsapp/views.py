from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import ticketform, contactform


# Home view
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


# Ticket view (ticket form page)
def ticket(request):
    return render(request, 'ticket.html')


# Events view
def events(request):
    return render(request, 'events.html')


# Contact view (handles contact form submission)
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contactform.objects.create(
            name=name,
            email=email,
            message=message,
        )
        messages.success(request, "Your message has been sent successfully.")
        return redirect('contact')  # Optional: Redirect back to the contact page after success.

    return render(request, 'contact.html')


# About view
def about(request):
    return render(request, 'about.html')


# Portfolio view
def portfolio(request):
    return render(request, 'portfolio.html')


# Signup view (handles user registration)
def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password != cpassword:
            messages.error(request, "Passwords don't match. Please recheck and try again.")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'signup.html')

        user = User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, 'Account created. Please log in.')
        return redirect('login')

    return render(request, 'signup.html')


# Login view (handles user authentication)
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('home')  # Redirect to homepage after login
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'login.html')


# Ticket form submission
def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        quantity = request.POST.get('tickets')
        dropdown_option = request.POST.get('event')
        uploaded_file = request.FILES.get('paymentproof_pic')

        # Validate fields
        if not all([name, email, quantity, dropdown_option, uploaded_file]):
            return HttpResponse("All fields are required!", status=400)

        # Save the ticket form data to the database
        ticket = ticketform.objects.create(
            name=name,
            email=email,
            quantity=int(quantity),
            dropdown_option=dropdown_option,
            uploaded_file=uploaded_file,
        )

        # Pass the ticket object to the template context and render the ticket slip page
        return render(request, 'ticketslip.html', {'ticket': ticket})

    return render(request, 'ticket.html')


# Ticket slip view (display the ticket details)
def ticketslip(request):
    ticket_id = request.GET.get('ticket_id')
    try:
        ticket = ticketform.objects.get(id=ticket_id)
    except ticketform.DoesNotExist:
        messages.error(request, "Ticket not found.")
        return redirect('home')
    
    return render(request, 'ticketslip.html', {'ticket': ticket})


# Logout view
def logout_view(request):
    auth_logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')  # Redirect to login page after logout


from django.shortcuts import render
from .models import Event

def events_view(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'events.html', context)