from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from .models import *
from django.contrib.auth.models import User


class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CustomerForm (ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class DepositForm (ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'
        exclude = ['user']
        

class LoanForm (ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'
        exclude = ['user']

class TransactionForm (ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        exclude = ['user']

class TransactiononeForm (ModelForm):
    class Meta:
        model = Transactiontwo
        fields = '__all__'
        exclude = ['user']


class TransactiontwoForm (ModelForm):
    class Meta:
        model = Transactiontwo
        fields = '__all__'
        exclude = ['user']


class TransactionthreeForm (ModelForm):
    class Meta:
        model = Transactionthree
        fields = '__all__'
        exclude = ['user']

class TransactionfourForm (ModelForm):
    class Meta:
        model = Transactionfour
        fields = '__all__'
        exclude = ['user']

class TransactionfiveForm (ModelForm):
    class Meta:
        model = Transactionfive
        fields = '__all__'
        exclude = ['user']

class TransactionfiveForm (ModelForm):
    class Meta:
        model = Transactionfive
        fields = '__all__'
        exclude = ['user']


class RedeemcardForm (ModelForm):
    class Meta:
        model = Redeemcard
        fields = '__all__'
        exclude = ['user']

class ReportForm (ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        exclude = ['user']

class AccountForm (ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        exclude = ['user']


class CardnumberForm (ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        exclude = ['user']