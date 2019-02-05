# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User, Media
from forms import UserModelForm, AddressModelForm
from django.forms import modelformset_factory


# def all_user(request):
#     todos = User.objects.all()
#     context = {
#         'todos': todos
#     }
#
#     return render(request, 'profiles/users.html', context)
class HomeView(TemplateView):
    """ solamente renderiza el template """
    template_name = "profiles/home_view.html"


# class UsersView(TemplateView):
#     model = User
#     # template_name = "profiles/users.html"
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(UsersView, self).get_context_data(*args, **kwargs)
#         context['todos'] = User.objects.all()
#         return context
#  no lo uso xq realmente quiero una lista de usuer, lo hago abajo con 2 lineas


class UserList(ListView):
    model = User
    # template es user_list.html
    context_object_name = 'the_best_users'
    # object_list por defecto


class UserDetail(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UserDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['media_list'] = Media.objects.filter(user_id=self.kwargs['pk'])  # Media.objects.all()
        print type(context)
        return context


def new_user(request):

    MediaFormSet = modelformset_factory(Media, fields=('name', 'url'), max_num=3, extra=2)

    # media_form = MediaFormSet(queryset=Media.objects.none())

    if request.method == "POST":
        address_form = AddressModelForm(request.POST)
        user_form = UserModelForm(request.POST)
        media_form = MediaFormSet(request.POST)

        if address_form.is_valid() and user_form.is_valid() and media_form.is_valid():

            address = address_form.save()
            user = user_form.save(commit=False)
            user.address = address
            user.save()

            media = media_form.save(commit=False)

            for el in media:
                el.user_id = user
                el.save()

            messages.success(request, "Usuario '{}' creado".format(user.email))
            # return redirect(reverse('all_user_list'))
        else:
            messages.error(request, 'Verifique los campos')
    else:
        address_form = AddressModelForm()
        user_form = UserModelForm()
        media_form = MediaFormSet(queryset=Media.objects.none())
    context = {
        'user_form': user_form,
        'address_form': address_form,
        'media_form': media_form,
    }

    return render(request, "profiles/user_new3.html", context)

# def new_user(request):
#     if request.method == "POST":
#         address_form = AddressModelForm(request.POST)
#         user_form = UserModelForm(request.POST)
#
#         if address_form.is_valid() and user_form.is_valid():
#             address = address_form.save()
#             user = user_form.save(commit=False)
#             user.address = address
#             user.save()
#
#             messages.success(request, "Usuario '{}' creado".format(user.email))
#             # return redirect(reverse('all_user_list'))
#         else:
#             messages.error(request, 'Verifique los campos')
#     else:
#         address_form = AddressModelForm()
#         user_form = UserModelForm()
#
#     context = {
#         'user_form': user_form,
#         'address_form': address_form,
#     }
#
#     return render(request, "profiles/user_new2.html", context)
#

# OBSOLETO AHORA USO 2 MODEL IN 1 FORM
# def new_user1(request):
#
#     form = UserModelForm(request.POST or None)
#     context = {
#         'form': form
#     }
#
#     if form.is_valid():
#         instance = form.save(commit=False)
#         # timezone.now() no es necesario
#         instance.save()
#         context = {
#             'form': form
#     return render(request, "profiles/user_new2.html", context)
#         }
