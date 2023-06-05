from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser,Products,Order,OrderItem
from django.forms.widgets import DateInput
from django.forms import inlineformset_factory
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name','email', 'date_of_birth', 'address', 'contact', 'password1', 'password2']

    # Additional fields
    date_of_birth = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    address = forms.CharField(max_length=255)
    contact = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Enter your contact number'}))
    email=forms.EmailField(empty_value=None)
class AdminUser(CustomUserCreationForm):
    IS_STAFF_CHOICES = (
        (0, 'No'),
        (1, 'Yes'),
    )
    is_staff = forms.ChoiceField(choices=IS_STAFF_CHOICES,required=True,widget=forms.RadioSelect,initial=0)
    class Meta(CustomUserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 'address', 'contact', 'password1', 'password2', 'is_staff']

class CustomerLoginForm(AuthenticationForm):
    class Meta:
        model= AuthenticationForm
        fields=['username','password']

class ProductsForm(forms.ModelForm):
    class Meta:
        model= Products
        fields='__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer']

OrderItemFormSet = inlineformset_factory(Order, OrderItem, fields=('product', 'quantity'), extra=1)