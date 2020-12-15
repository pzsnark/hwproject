# from django.http import HttpResponse
# from django.shortcuts import render, redirect, reverse
# from django.contrib.auth import authenticate, login, logout
# from .forms import LoginForm

from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import reverse, redirect, render
from django.views.generic import View
from .forms import LoginForm, SignupForm

# authenticate() проверяет учетные данные пользователя и возвращает user объект в случае успеха
# login() задает пользователя в текущей сессии.


class AdLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('ads:index'), request)
            context = {
                'form': form
            }
            return render(request, self.template_name, context)
        else:
            context = {
                'form': form
            }
            return render(request, self.template_name, context)


class SignupView(View):
    template_name = 'account/signup.html'
    reg_form = SignupForm

    def get(self, request):
        context = {'form': self.reg_form}
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request):
        user_form = SignupForm(data=request.POST)
        registered = False
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.email = user_form.cleaned_data['email']
            user.save()
            registered = True
            return render(request, 'account/signup.html', {'registered': registered})
        else:
            return render(request, 'account/signup.html',
                          {'form': user_form, 'registered': registered})


def user_logout(request):
    logout(request)
    return redirect('account:login')

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:  # проверка существования пользователя
#                 if user.is_active:  # проверка активности аккаунта
#                     login(request, user)  # устанавливаем сессию
#                     return redirect('ads:index')
#                 else:
#                     return HttpResponse('Аккаунт отключен')
#             else:
#                 return render(request, 'account/login.html', {'form': form, 'login_result': 'Неверное имя '
#                                                                                             'пользователя или пароль'
#                                                               })
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})
