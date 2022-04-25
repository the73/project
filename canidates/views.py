from django.shortcuts import render,redirect
from django.views.generic import View, ListView, DeleteView, CreateView, TemplateView
from django.contrib.auth import authenticate, login, logout
from canidates.forms import UserRegistrationForm, LoginForm
from django.urls import reverse_lazy
from owner.models import Admin
from canidates.models import Userprofiles
from canidates.filters import LocationFilter

# Create your views here.

class CustmerHome(View):
    def get(self, request, *args, **kwargs):
        vacc = Admin.objects.all()
        filter = LocationFilter(request.GET, queryset=Admin.objects.all())
        context = {"vacc": vacc, "filter": filter}
        return render(request, "home.html", context)

class SignupView(View):
    def get(self, request):
        form = UserRegistrationForm()
        context = {"form": form}
        return render(request, "signup.html", context)

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("user created")
            return redirect("signup .html")
        else:
            context = {"form": form}
            return render(request, "signup.html", context)


class SigninView(View):
    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, "signin.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            print("here")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if request.user.is_superuser:
                    return redirect("location")
                else:
                    return redirect("custhome")

            else:
                context = {"form": form}
                return render(request, "signup.html", context)
        else:
            context = {"form": form}
            return render(request, "signin.html", context)


def sign_out(request):
    logout(request)
    return redirect("signin")

class Booked(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        vacc = Admin.objects.get(id=id)
        user = request.user
        carts = Userprofiles(user=user, item=vacc)
        carts.save()
        print('item has been added')
        return redirect('custhome')

class BookedItems(ListView):
    model = Userprofiles
    template_name = "booked.html"
    context_object_name = "items"

class RemoveBookItem(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        cart = Userprofiles.objects.get(id=id)
        cart.status = "cancelled"
        cart.save()
        return redirect("booked")