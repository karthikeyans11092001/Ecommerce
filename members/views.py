from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomerLoginForm,AdminUser,ProductsForm,OrderForm,OrderItemFormSet
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Products,CustomUser,Order,OrderItem
from .forms import CustomUserCreationForm
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = CustomerLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomerLoginForm()
    return render(request, 'login.html', {'form': form})

@staff_member_required
def create_profile(request):
    if request.method == 'POST':
        form = AdminUser(request.POST)
        if form.is_valid():
            form.save()
            messages
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('profile')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = AdminUser()

    return render(request, 'create_profile.html', {'form': form})

@login_required
def home(request):
    data = Products.objects.all()
    return render(request, 'home.html', {'data': data})
@login_required
def about(request):
    return render(request, 'about.html')
@login_required
def myCart(request):
    return render(request, 'myCart.html')
@login_required
def profile(request):
    profiles=CustomUser.objects.all()
    return render(request, 'profile.html',{'users':profiles})
@login_required
def logout_user(request):
    messages.success(request,'Logged out successfully!!')
    logout(request)
    return redirect('login')
@staff_member_required
def add_Product(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages
            messages.success(request, 'Item Added Successfully.')
            return redirect('addProduct')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = ProductsForm()
    data = Products.objects.all()
    return render(request, 'addProduct.html', {'form': form,'data': data,'title':'Add Product'})

@login_required
def display_product(request):
    data = Products.objects.all()
    return render(request, 'home.html', {'data': data,'title':'Home'})

@login_required
def UpdateProfile(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)
    context = {
        'user': user,
    }
    return render(request, 'edit_profile.html', context)
@login_required
def place_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST, prefix='orderitems')

        if order_form.is_valid() and formset.is_valid():
            order = order_form.save()
            formset.instance = order
            formset.save()
            return redirect('myCart')  # Redirect to a success page after successful order placement

    else:
        order_form = OrderForm()
        formset = OrderItemFormSet(prefix='orderitems')

    return render(request, 'myCart.html', {'order_form': order_form, 'formset': formset})
@login_required
def orders_view(request):
    customer_id=CustomUser.objects.filter(username=request.user.username).first()
    customer_id = customer_id.id
    orders = Order.objects.filter(customer_id=customer_id)
    return render(request, 'myCart.html', {'orders': orders})
@login_required
def view_order_products(request,id):
    order=OrderItem.objects.filter(order_id=id)
    products=Products.objects.all()
    return render(request,'my_order.html',{'order': order,'products':products})
