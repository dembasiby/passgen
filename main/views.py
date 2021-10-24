from django.shortcuts import render
from django.views.generic import TemplateView
import random

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


def generate_password(request):
    password_list = list('abcdefghijklmnopqrstuvwxyz')
    final_password = ''

    password_length = request.GET.get('password_length')
    contain_uppercase = request.GET.get('contain_uppercase')
    contain_numbers = request.GET.get('have_numbers')
    contain_special_chars = request.GET.get('contain_special_characters')

    if contain_numbers:
        password_list.extend(list('0123456789'))
    if contain_special_chars:
        password_list.extend('@#/\\{}!~&*%+-?=$()[]|')
    if contain_uppercase:
        password_list.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    random.shuffle(password_list)

    while len(final_password) < int(password_length):
        final_password += random.choice(password_list)

    return render(request, 'password.html', {'password': final_password})
