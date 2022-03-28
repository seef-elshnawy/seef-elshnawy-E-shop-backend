from rest_framework import serializers
from .models import Users

class log(serializers.ModelSerializer):
    class Meta:
      model=(Users)
      fields='__all__'