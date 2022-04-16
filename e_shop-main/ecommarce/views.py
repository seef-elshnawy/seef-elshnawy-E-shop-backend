from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import log,shop,newPass
from .models import Users,Products
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.hashers import check_password,make_password
# Create your views here.

@api_view(['GET'])
def getUsers(request):
  users=Users.objects.all()
  serializer=log(users,many=True)
  return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
  serializer=log(data=request.data)
  try:
   request.data['password']=make_password(request.data['password'])
  except :
    pass
  if Users.objects.filter(nick_name=request.data['nick_name']).exists():
   return HttpResponse('this nick name is already used',status=405)  
  
  if Users.objects.filter(email=request.data['email']).exists():
   return HttpResponse('this email is already used',status=405)

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
def updateUser(request,pk,*args,**kwargs):
    user=Users.objects.get(id=pk)
    serializer=log(user,data=request.data,many=False)
    if serializer.is_valid():
        serializer.save()
        return redirect('users')
    return Response(serializer.data)

@api_view(['POST'])
def Resetpassword(request,pk):
 user=Users.objects.get(id=pk)
 serializer=newPass(user,data=request.data,many=False)
 request.data['password']=make_password(request.data['password'])
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
 try: 
  user=Users.objects.get(nick_name=request.data['nick_name'])
 except Users.DoesNotExist:
     raise Http404('No user with this nick name') 
 if check_password(request.data['password'],user.password):
   serializer=log(user,many=False)
 else: 
    return HttpResponse('Password was wrong',status=405)
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
