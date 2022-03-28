from unicodedata import name
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

country_choice=(
    ('eg','Egypt'),
    ('us','United state'),
    ('su','Saudi Arabia'),
    ('ue','Emarties')
)
class Users(models.Model):
 id=models.AutoField(auto_created=True,primary_key=True)
 name=models.CharField(max_length=100,default='')
 nick_name=models.CharField(max_length=100,default='',unique=True)
 email=models.EmailField(_('email adress'),unique=True)
 password=models.CharField(max_length=22,default='')
 phone=models.IntegerField()
 country=models.CharField(choices=country_choice,max_length=16)
 admin=models.BooleanField(default=False,blank=True)
 customer=models.BooleanField(default=False,blank=True)

 def __str__(self):
  return f'id: {self.id} name: {self.name} email: {self.email} admin: {self.admin} customer: {self.customer}' 
