from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsers


# class CustomUsersCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = get_user_model()
#         fields = UserCreationForm.Meta.fields
#
#
# class CustomUsersChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()
#         fields = UserChangeForm.Meta.fields
