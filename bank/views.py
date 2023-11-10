from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import CreateUserForm, CustomerForm, RedeemcardForm

from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.



def about(request):
    context = {}
    return render (request, "bank/about.html", context)


def reset(request):
    context = {}
    return render (request, "bank/reset.html", context)

@login_required (login_url = "login")
def apply_fixed(request):
    context = {}
    return render (request, "bank/apply-fixed.html", context)

@login_required (login_url = "login")
def apply_loan(request):
    context = {}
    return render (request, "bank/apply-loan.html", context)


@login_required (login_url = "login")
def automatic_methods(request):
    context = {}
    return render (request, "bank/automatic-methods.html", context)


@login_required (login_url = "login")
def calculator(request):
    context = {}
    return render (request, "bank/calculator.html", context)


@login_required (login_url = "login")
def change_password(request):
    context = {}
    return render (request, "bank/change-password.html", context)



@login_required (login_url = "login")
def closedticket(request):
    context = {}
    return render (request, "bank/closedticket.html", context)

def contact(request):
    context = {}
    return render (request, "bank/contact.html", context)


@login_required (login_url = "login")
def create_ticket(request):
    context = {}
    return render (request, "bank/create-ticket.html", context)


@login_required (login_url = "login")
def card(request):
    context = {}
    return render (request, "bank/card.html", context)


@login_required (login_url = "login")
def dashboard(request):
    context = {}
    return render (request, "bank/dashboard.html", context)


@login_required (login_url = "login")
def dps_schemes(request):
    context = {}
    return render (request, "bank/dps-schemes.html", context)


@login_required (login_url = "login")
def edit(request):
    customer = request.user.customer
    form = CustomerForm (instance = customer)

    if request.method == 'POST':
        form = CustomerForm (request.POST, request.FILES, instance = customer)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "bank/edit.html", context)

@login_required (login_url = "login")
def exchange_money(request):
    context = {}
    return render (request, "bank/exchange-money.html", context)

def faq(request):
    context = {}
    return render (request, "bank/faq.html", context)

def history(request):
    context = {}
    return render (request, "bank/history.html", context)

def index(request):
    context = {}
    return render (request, "bank/index.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect ('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get ('username')
            password = request.POST.get ('password')

            user = authenticate (request, username = username, password = password)

            if user is not None:
                login (request, user)
                return redirect ('dashboard')
            else:
                messages.info (request, 'Username OR password is incorrect')

        context = {}
    return render (request, "bank/login.html", context)

def logoutUser(request):
    logout (request)
    return redirect ('login')


@login_required (login_url = "login")
def manual_methods(request):
    context = {}
    return render (request, "bank/manual-methods.html", context)


@login_required (login_url = "login")
def manual_withdraw(request):
    context = {}
    return render (request, "bank/manual-withdraw.html", context)


@login_required (login_url = "login")
def my_loans(request):
    context = {}
    return render (request, "bank/my-loans.html", context)

@login_required (login_url = "login")
def myticket(request):
    context = {}
    return render (request, "bank/myticket.html", context)



@login_required (login_url = "login")
def payment_request(request):
    context = {}
    return render (request, "bank/payment-request.html", context)


@login_required (login_url = "login")
def payment_request(request):
    context = {}
    return render (request, "bank/payment-request.html", context)

def pin(request):
    context = {}
    return render (request, "bank/pin.html", context)
    
def plans(request):
    context = {}
    return render (request, "bank/plans.html", context)

def privacy_policy(request):
    context = {}
    return render (request, "bank/privacy-policy.html", context)



@login_required (login_url = "login")
def profile(request):
    context = {}
    return render (request, "bank/profile.html", context)



@login_required (login_url = "login")
def redeem_gift_cards(request):
    redeemcard = request.user.redeemcard
    form = RedeemcardForm (instance = redeemcard)

    if request.method == 'POST':
        form = RedeemcardForm (request.POST, request.FILES, instance = redeemcard)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "bank/redeem-gift-cards.html", context)


@unauthenticated_user
def register(request):
    form = CreateUserForm ()
    if request.method == 'POST':
        form = CreateUserForm (request.POST)
        if form.is_valid ():
            user = form.save ()
            username = form.cleaned_data.get ('username')


            messages.success (request, 'Account was created for ' + username)

            return redirect ('login')

    context = {'form': form}
    return render (request, "bank/register.html", context)



@login_required (login_url = "login")
def send_money(request):
    context = {}
    return render (request, "bank/send-money.html", context)


def services(request):
    context = {}
    return render (request, "bank/services.html", context)


def terms_condition(request):
    context = {}
    return render (request, "bank/terms-condition.html", context)

@login_required (login_url = "login")
def transactions_report(request):
    context = {}
    return render (request, "bank/transactions-report.html", context)


@login_required (login_url = "login")
def wire_transfer(request):
    context = {}
    return render (request, "bank/wire-transfer.html", context)



