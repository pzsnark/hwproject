# from django.http import HttpResponse
# from django.shortcuts import render, redirect, reverse
# from django.contrib.auth import authenticate, login, logout
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import reverse, redirect, render, get_object_or_404
from django.views.generic import View, DetailView

from ads.models import Profile, Message, User
from .forms import LoginForm, SignupForm, MessageForm

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
            Profile.objects.create(user_id=user.id, avatar='users/default.png')
            return render(request, 'account/signup.html', {'registered': registered})
        else:
            return render(request, 'account/signup.html',
                          {'form': user_form, 'registered': registered})


def user_logout(request):
    logout(request)
    return redirect('account:login')


class MessageView(DetailView):
    model = User
    template_name = 'account/message.html'
    context_object_name = 'messages'
    pk_url_kwarg = 'user_id'
    message_form = MessageForm

    def get(self, request, user_id, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['messages'] = Message.objects.all().filter(user__id=user_id).order_by('-date_pub')
        if request.user.is_authenticated:
            context['message_form'] = self.message_form
        return self.render_to_response(context)

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        form = self.message_form(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.user = user
            message.save()
            return render(request, self.template_name, context={
                'message_form': self.message_form,
                'messages': Message.objects.all().filter(user__id=user_id).order_by('-date_pub'),
            })
        else:
            return render(request, self.template_name, context={
                'message_form': form,
                'messages': user.comments.all().order_by('-date_pub'),
            })

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
