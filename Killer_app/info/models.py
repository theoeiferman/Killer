from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

#https://django-phonenumber-field.readthedocs.io/en/latest/reference.html#phonenumber_field.phonenumber.PhoneNumber


class PlayerContact(models.Model):
   surname = models.CharField(max_length=100,blank=True,null=True)
   date_created = models.DateTimeField(default=timezone.now)
   target = models.CharField(max_length=100, blank=True, null=True)
   player_email = models.EmailField(max_length=254,blank=True,null=True,default='') #default_email@example.com
   action = models.CharField(max_length=150,blank=True,null=True)
   game_name = models.CharField(max_length=100, blank=True, null=True) #this should be defined as key
   def __str__(self):
      return self.surname


class Games(models.Model):
    name = models.CharField(max_length=30,default='Game0') #this should be defined as key
    gamemode = models.CharField(max_length=100,default='default')
    started_date = models.DateTimeField(default=timezone.now)
    players = models.ManyToManyField(PlayerContact)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if the object is new (has no primary key)
            last_game = Games.objects.last()
            if last_game:
                last_game_number = int(last_game.name.split(" ")[-1])
                new_game_number = last_game_number + 1
                self.name = f'Game number {new_game_number}'
            else:
                self.name = 'Game number 1'
        super().save(*args, **kwargs)



class PlayerContactForm(forms.ModelForm):
    class Meta:
        model = PlayerContact
        fields = ['surname', 'player_email','action']
        widgets = {
            'surname': forms.TextInput(attrs={'placeholder': 'Enter pseudo'}),
            'player_email': forms.TextInput(attrs={'placeholder': 'Enter a valid email adress'}),
            'action': forms.TextInput(attrs={'placeholder': 'custom action (optional)'})
        }
    def __init__(self, *args, **kwargs):
        super(PlayerContactForm, self).__init__(*args, **kwargs)
        self.fields['action'].required = False
#To do add verification email adrres




