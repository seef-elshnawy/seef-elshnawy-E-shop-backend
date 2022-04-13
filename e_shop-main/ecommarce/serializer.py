from dataclasses import fields
from rest_framework import serializers
from .models import Users,Products

class log(serializers.ModelSerializer):
    def create(request,*args,**kwargs):
      request.data._mutable= True
    class Meta:
      model=(Users)
      fields='__all__'

class shop(serializers.ModelSerializer):
  class Meta:
    model=(Products)
    fields='__all__'
