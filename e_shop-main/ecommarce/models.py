from unicodedata import name
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

# Create your models here.

country_choice=(
    ('eg','Egypt'),
    ('us','United state'),
    ('su','Saudi Arabia'),
    ('ue','Emarties')
)
def upload_path(instance,filename):
    return '/'.join(['image',str(instance.nick_name),filename])

class Users(models.Model):
 id=models.AutoField(auto_created=True,primary_key=True)
 name=models.CharField(max_length=100,default='')
 nick_name=models.CharField(max_length=100,default='',unique=True)
 email=models.EmailField(_('email adress'),unique=True)
 password=models.CharField(max_length=200,default='')
 phone=models.IntegerField()
 country=models.CharField(choices=country_choice,max_length=16)
 img=models.ImageField(blank=True,default='',null=True,upload_to=upload_path)
 admin=models.BooleanField(default=False,blank=True)
 customer=models.BooleanField(default=False,blank=True)
    
 def __str__(self):
  return f'id: {self.id} name: {self.name} email: {self.email} admin: {self.admin} customer: {self.customer}' 


categorize=(
    ('labtop','labtop'),
    ('PS','PS'),
    ('PS accessories','PS accessories'),
    ('PC','PC'),
    ('Mobilegaming','Mobile gaming'),
    ('Monitor','Monitor'),
    ('accessories','accessories'),
    ('memory','memory'),
    ('Tower','Tower')
)
def upload_product(instance,filename):
    return '/'.join(['image',str(instance.made_in),filename])

class Categorize(models.Model):
 id=models.AutoField(primary_key=True,auto_created=True)   
 Item=models.CharField(default='',max_length=200)

 def __str__(self):
    return f'Item: {self.Item}'

class Products(models.Model):
 id=models.AutoField(primary_key=True,auto_created=True)
 product_name=models.CharField(max_length=100,default='')
 product_image1=models.ImageField(blank=True,default='',null=True,upload_to=upload_product)
 product_image2=models.ImageField(blank=True,default='',null=True,upload_to=upload_product)
 product_image3=models.ImageField(blank=True,default='',null=True,upload_to=upload_product)
 product_image4=models.ImageField(blank=True,default='',null=True,upload_to=upload_product)
 product_image5=models.ImageField(blank=True,default='',null=True,upload_to=upload_product)
 cretedBy=models.CharField(max_length=100,blank=True,default='')
 details=models.JSONField(default="{}")
 created_at=models.DateTimeField(auto_now_add=True,blank=True)
 Rate=models.IntegerField(blank=True,null=True)
 product_categorize=models.CharField(choices=categorize,max_length=40,default='')
 product_categorize_two=models.ManyToManyField(to=Categorize,related_name='catigo')   
 made_in=models.CharField(max_length=100,default='',blank=True)
 price=models.IntegerField()

 def __str__(self):
   return f'id: {self.id} product_name= {self.product_name} createdBy= {self.cretedBy} price: {self.price}'

