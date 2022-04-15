from dataclasses import fields
from rest_framework import serializers
from .models import Users,Products

class log(serializers.ModelSerializer):
    class Meta:
      model=(Users)
      fields=['name','nick_name','email','phone','country','img','admin','customer']

class shop(serializers.ModelSerializer):
  class Meta:
    model=(Products)
    fields='__all__'
    
class newPass(serializers.ModelSerializer):
  class Meta:
    model=(Users)
    fields=['password']
