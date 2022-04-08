from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import log,shop
from .models import Users,Products
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
# Create your views here.

@api_view(['GET'])
def getUsers(request):
  users=Users.objects.all()
  serializer=log(users,many=True)
  return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
  serializer=log(data=request.data)
  if serializer.is_valid():
    subject=f'message from {request.data["name"]}'
    message=render_to_string("ecommarce/index.html",{'Name':request.data['name']})
    sender=request.data['email']
    recipients='elshnawyseef675@gmail.com'

    email=EmailMessage(
     subject,
     message,
     recipients,
     [sender]
    )
    try:
       #send_mail(subject,message,sender,recipients,fail_silently=True)
       print(f'send email success {request.data["email"]}')
       serializer.save() 
       email.fail_silently=False
       email.send()
    except: 
       return Response('faild to send email') 
    return redirect('users')
  return Response(serializer.data)

@api_view(['POST'])
def updateUser(request,pk):
 user=Users.objects.get(id=pk)
 serializer=log(user,data=request.data,many=False)
 if serializer.is_valid():
     serializer.save()
     return redirect('users')
 return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request,pk):
  user=Users.objects.filter(id=pk)
  user.delete()
  return Response('delete sucsess')

@api_view(['POST'])
def Login(request):
 user=Users.objects.get(nick_name=request.data['nick_name'])
 if user.password==request.data['password']:
  serializer=log(user,many=False)
 else:
    return HttpResponse(None)
 return Response(serializer.data)


@api_view(['GET'])
def getProducts(request):
  products=Products.objects.all()
  serializer=shop(products,many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,pk):
  products=Products.objects.get(id=pk)
  serializer=shop(products,many=False)
  return Response(serializer.data)


@api_view(['POST'])
def addProducts(request):
   serializer=shop(data=request.data)
   if serializer.is_valid():
     serializer.save()
     return redirect('products')

   return Response(serializer.data)


@api_view(['POST'])
def updateProduct(request,pk):
  product=Products.objects.get(id=pk)
  serializer=shop(product,data=request.data,many=False)
  if serializer.is_valid():
    serializer.save()
    return redirect('products')
  return Response(serializer.data)
 

@api_view(['DELETE'])
def deleteProduct(request,pk):
  product=Products.objects.filter(id=pk)
  product.delete()
  return HttpResponse('delete product succsesss')
