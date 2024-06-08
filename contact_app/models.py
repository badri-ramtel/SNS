from django.db import models
from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
STATUS_CHOICES = (
    ('R', 'Read'),
    ('U', 'Unread')
)

class FeedBack(models.Model):
    date = models.DateTimeField(auto_now_add= True)
    full_name = models.CharField(max_length= 100, null= False, blank= False)
    email = models.EmailField(max_length= 254, null= False, blank= False) 
    address = models.CharField(max_length= 200, null= False, blank= False)
    contact = models.CharField(max_length= 15, null= False, blank= False)
    feedback = models.TextField(null= False, blank= False)
    status = models.CharField(max_length= 1, choices= STATUS_CHOICES, default= "U")

    def __str__(self):
        return f'{self.full_name}- ({self.date})'
    
    class Meta:
        db_table = 'Feedback'
        verbose_name_plural = 'Feedback'
        ordering = ['-id']

class FeedbackInstruction(models.Model):
    instruct = RichTextField(null= False, blank= False)

    def __self__(self):
        return f'{self.instruct}'

    class Meta:
        db_table = 'Feedback Instruction'
        verbose_name_plural = 'Feedback Instruction'

CONDITION = (
    ('C', 'Confirmed'),
    ('U', 'Unconfirm')
)

class Member(models.Model):
    date = models.DateTimeField(auto_now_add= True)
    first_name = models.CharField(max_length= 100, null= False, blank= False)
    last_name = models.CharField(max_length= 100, null= False, blank= False)
    email = models.EmailField(max_length= 254, null= False, blank= False)
    contact = models.CharField(max_length= 15, null= False, blank= False)
    address1 = models.CharField(max_length= 200, null= False, blank= False)
    address2 = models.CharField(max_length= 200, null= True, blank= True)
    city = models.CharField(max_length= 400, null= False, blank= False)
    province = models.CharField(max_length= 400, null= False, blank= False)
    postal_code = models.CharField(max_length= 15, null= False, blank= False)
    members = (
        ("GENERAL", 'general'), 
        ("LIFETIME", 'lifetime'),
    )
    membership = models.CharField(max_length= 9, choices= members, default= 'GENERAL')
    screenshot = models.ImageField(upload_to= 'images/payments/membership/', null= False, blank= False)
    status = models.CharField(max_length= 1, choices= CONDITION, default= 'U')

    def __str__(self):
        return f'{self.first_name} {self.last_name}- ({self.date})'
    
    class Meta:
        db_table = 'Member'
        verbose_name_plural = 'Member'
        ordering = ['-id']

class MemberInstruction(models.Model):
    instruct = RichTextField(null= False, blank= False)

    def __self__(self):
        return f'{self.instruct}'

    class Meta:
        db_table = 'Member Instruction'
        verbose_name_plural = 'Member Instruction'

class Vacancy(models.Model):
    f_name = models.CharField(max_length= 200, null= False, blank= False)
    c_date = models.DateField(auto_created= False)
    image = models.ImageField(upload_to='images/vacancy/', null= True, blank= True)
    vacancy_content = RichTextField(null= True)

    def __str__(self):
        return f'{self.f_name}- ({self.c_date})'

    class Meta:
        db_table = 'Vacancy'
        verbose_name_plural = 'vacancy'
        ordering = ['-id']

class VacancyInstruction(models.Model):
    instruct = RichTextField(null= False, blank= False)

    def __self__(self):
        return f'{self.instruct}'

    class Meta:
        db_table = 'Vacancy Instruction'
        verbose_name_plural = 'Vacancy Instruction'


class Donation(models.Model):
    date = models.DateTimeField(auto_now= True, auto_created= True)
    first_name = models.CharField(max_length= 100, null= False, blank= False)
    last_name = models.CharField(max_length= 100, null= False, blank= False)
    email = models.EmailField(max_length= 254, null= False, blank= False)
    contact = models.CharField(max_length= 15, null= False, blank= False)
    address_1 = models.CharField(max_length= 200, null= False, blank= False)
    address_2 = models.CharField(max_length= 200, null= True, blank= True)
    city = models.CharField(max_length= 400, null= False, blank= False)
    state = models.CharField(max_length= 400, null= False, blank= False)
    postal_code = models.CharField(max_length= 15, null= False, blank= False)
    # country = CountryField(blank_label="select country")
    country = models.CharField(max_length=200, null= False, blank= False)
    donate = (
        ("GENERAL", 'general'), 
        ("COVID", 'covid'),
        ("EARTHQUAKE", 'earthquake'),
    )
    donation_type = models.CharField(max_length= 12, choices= donate)
    amount = models.IntegerField(null= False, blank= False)
    screenshot = models.ImageField(upload_to= 'images/payments/donation/', null= False, blank= False)
    status = models.CharField(max_length= 1, choices= CONDITION, default= 'U')

    def __str__(self):
        return f'{self.first_name} {self.last_name}- ({self.date})'
    
    class Meta:
        db_table = 'Donation'
        verbose_name_plural = 'Donation'
        ordering = ['-id']

class DonationInstruction(models.Model):
    instruct = RichTextField(null= False, blank= False)

    def __self__(self):
        return f'{self.instruct}'

    class Meta:
        db_table = 'Donation Instruction'
        verbose_name_plural = 'Donation Instruction'