from django.db import models
import datetime

class daily_challenge(models.Model):
    theme = models.CharField(max_length=50)
    quote = models.TextField()
    attribution = models.CharField(max_length=50)
    bio = models.TextField()
    challenge = models.TextField()
    sequence = models.IntegerField()

class dated_challenge(models.Model):
    date = models.DateField()
    challenge_id = models.ForeignKey(daily_challenge)

class reminder(models.Model):
    rem_freq = models.CharField(max_length=50, default="daily")
    rem_vector = models.CharField(max_length=50, default="mail")
    rem_address = models.CharField(max_length=150)
    
