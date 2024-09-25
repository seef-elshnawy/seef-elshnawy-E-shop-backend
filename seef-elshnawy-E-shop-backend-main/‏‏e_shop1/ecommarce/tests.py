from django.test import TestCase
from .models import Users
# Create your tests here.

class UsersTest(TestCase):

  Users.objects.create(name='mohamed',nick_name='medo12',email='medo@gmail.com12',password=123456789,phone=1002541141,country='eg',admin=False,customer=False)
  Users.objects.create(name='hala',nick_name='hala12',email='hala@gmail.com12',password=123456789,phone=1002541141,country='eg',admin=False,customer=True)

  def customerTest(self):
   user_hala=Users.objects.get(name='hala')
   return self.assertEqual(user_hala.customer==True)