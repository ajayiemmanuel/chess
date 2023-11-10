from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models


# Create your models here.
class Customer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    email = models.CharField (max_length = 200, null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    profile_pic = models.ImageField (default = "avater.png", null = True, blank = True)

    def __str__(self):
        return self.name

class Deposit (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    dollar = models.CharField (max_length = 200,  null = True, default = "0",)
    euro = models.CharField (max_length = 200, default = "0",)
    inr = models.CharField (max_length = 200, default = "0",)
    notification_number = models.CharField (max_length = 200, default = "1",)
    notification_message = models.CharField (max_length = 200, default = "Dear Customer, Your account has succefully been created on 29/08/2023 08:25",)
    notification_time = models.CharField (max_length = 200, default = "19 hours ago",)



    def __str__(self):
        return self.name


class Loan (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200, blank = True,  null = True)
    active_loans = models.CharField (max_length = 200,  null = True, default = "",)
    loan_id = models.CharField (max_length = 200, default = "",)
    next_payment_date = models.CharField (max_length = 200, default = "",)
    status = models.CharField (max_length = 200, default = "",)
    amount_to_pay = models.CharField (max_length = 200, default = "",)
    action = models.CharField (max_length = 200, default = "",)



    def __str__(self):
        return self.name



class Transaction (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    currency = models.CharField (max_length = 200, default = "",)
    amount = models.CharField (max_length = 200, default = "",)
    charge = models.CharField (max_length = 200, default = "",)
    grand_total = models.CharField (max_length = 200, default = "",)
    debit_credit = models.CharField (max_length = 200, default = "",)
    method = models.CharField (max_length = 200, default = "",)
    status = models.CharField (max_length = 200, default = "",)
    details = models.CharField (max_length = 200, default = "",)
    date_time = models.CharField (max_length = 200, default = "",)



    def __str__(self):
        return self.name


class Transactionone (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    currency = models.CharField (max_length = 200, default = "",)
    amount = models.CharField (max_length = 200, default = "",)
    charge = models.CharField (max_length = 200, default = "",)
    grand_total = models.CharField (max_length = 200, default = "",)
    debit_credit = models.CharField (max_length = 200, default = "",)
    method = models.CharField (max_length = 200, default = "",)
    status = models.CharField (max_length = 200, default = "",)
    details = models.CharField (max_length = 200, default = "",)
    date_time = models.CharField (max_length = 200, default = "",)



    def __str__(self):
        return self.name


class Transactiontwo (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    currency = models.CharField (max_length = 200, default = "",)
    amount = models.CharField (max_length = 200, default = "",)
    charge = models.CharField (max_length = 200, default = "",)
    grand_total = models.CharField (max_length = 200, default = "",)
    debit_credit = models.CharField (max_length = 200, default = "",)
    method = models.CharField (max_length = 200, default = "",)
    status = models.CharField (max_length = 200, default = "",)
    details = models.CharField (max_length = 200, default = "",)
    date_time = models.CharField (max_length = 200, default = "",)



    def __str__(self):
        return self.name

class Transactionthree (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    currency = models.CharField (max_length = 200, default = "",)
    amount = models.CharField (max_length = 200, default = "",)
    charge = models.CharField (max_length = 200, default = "",)
    grand_total = models.CharField (max_length = 200, default = "",)
    debit_credit = models.CharField (max_length = 200, default = "",)
    method = models.CharField (max_length = 200, default = "",)
    status = models.CharField (max_length = 200, default = "",)
    details = models.CharField (max_length = 200, default = "",)
    date_time = models.CharField (max_length = 200, default = "",)



    def __str__(self):
        return self.name

class Transactionfour (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    currency = models.CharField (max_length = 200, default = "",)
    amount = models.CharField (max_length = 200, default = "",)
    charge = models.CharField (max_length = 200, default = "",)
    grand_total = models.CharField (max_length = 200, default = "",)
    debit_credit = models.CharField (max_length = 200, default = "",)
    method = models.CharField (max_length = 200, default = "",)
    status = models.CharField (max_length = 200, default = "",)
    details = models.CharField (max_length = 200, default = "",)
    date_time = models.CharField (max_length = 200, default = "",)



    def __str__(self):
        return self.name

class Transactionfive (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    currency = models.CharField (max_length = 200, default = "",)
    amount = models.CharField (max_length = 200, default = "",)
    charge = models.CharField (max_length = 200, default = "",)
    grand_total = models.CharField (max_length = 200, default = "",)
    debit_credit = models.CharField (max_length = 200, default = "",)
    method = models.CharField (max_length = 200, default = "",)
    status = models.CharField (max_length = 200, default = "",)
    details = models.CharField (max_length = 200, default = "",)
    date_time = models.CharField (max_length = 200, default = "",)



    def __str__(self):
        return self.name


class Payment (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    receiver_account = models.CharField (max_length = 200, default = "",)
    amount = models.CharField (max_length = 200, default = "",)
    currency = models.CharField (max_length = 200, default = "USD",)
    description = models.CharField (max_length = 200, default = "",)


    def __str__(self):
        return self.name


class Redeemcard (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True, default="Amazon Gift Card")
    code = models.CharField (max_length = 200, default = "",)



    def __str__(self):
        return self.name


class Report (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    info = models.CharField (max_length = 200, default = "Welcome",)



    def __str__(self):
        return self.name

class Accountnumber (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    account = models.CharField (max_length = 200, default = "Generating Account Number...",)



    def __str__(self):
        return self.name


class Cardnumber (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    expiration = models.CharField (max_length = 200, default = "01/23",)
    cvv = models.CharField (max_length = 200, default = "323",)


    def __str__(self):
        return self.name
