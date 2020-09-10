from django.db import models
from django.contrib.auth.models import User

class Prispevok(models.Model):
    obsah=models.CharField(max_length=10000)
    uzivatel = models.ForeignKey(User,on_delete=models.CASCADE,related_name='prispevky')
    
    vznikol = models.DateTimeField(auto_now_add=True)
