from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from random import randrange
from django.core.mail import send_mail

def home(request):
	if request.user.is_authenticated:
		if request.method=="POST":
			num = int(request.POST.get("num"))
			if num % 2==0:
				res = "even"
			else:
				res = "odd"
			return render(request,"home.html",{"msg":res})
		else:
			return render(request, "home.html")
	else:
		return redirect("ulogin")


def ulogin(request):
	if request.method=="POST":
		un=request.POST.get("un")
		pw=request.POST.get("pw")
		usr = authenticate(username=un,password=pw)
		if usr is not None:
			login(request,usr)
			return redirect("home")


		else:
			return render(request,"login.html",{"msg":"invalid un/pw "})
	else:
		return render(request,"login.html")



def usignup(request):
	if request.method =="POST":
		un =request.POST.get("un")
		try:
			usr=User.objects.get(username=un)
			return render(request,"signup.html",{"msg":"user already registered "})
		except User.DoesNotExist:
			pw=""
			text="123456789"
			for i in range(4):
				pw =pw +text[randrange(len(text))]
			print(pw)
			subject="Welcome to Kamal Clases "
			text = "ur password is " + str(pw)
			from_email = "janmesh.tester24aug22@gmail.com"
			to_email = [str(un)]
			send_mail(subject, text, from_email, to_email)
			usr = User.objects.create_user(username=un,password=pw)
			usr.save()
			return redirect("ulogin")

	else:
		return render(request,"signup.html")


def ulogout(request):
	logout(request)
	return redirect("ulogin")


def rnp(request):
	if request.method =="POST":
		un =request.POST.get("un")
		try:
			usr=User.objects.get(username=un)
			pw=""
			text="123456789"
			for i in range(4):
				pw =pw +text[randrange(len(text))]
			print(pw)
			subject="Welcome to Kamal Clases "
			text = "ur new password is " + str(pw)
			from_email = "janmesh.tester24aug22@gmail.com"
			to_email = [str(un)]
			send_mail(subject, text, from_email, to_email)
			usr.set_password(pw)
			usr.save()
			return redirect("ulogin")
		except User.DoesNotExist:
			return render(request,"rnp.html",{"msg":"user does not exist"})
			

	else:
		return render(request,"rnp.html")











			
