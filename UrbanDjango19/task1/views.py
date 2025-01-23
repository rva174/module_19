from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Game, Buyer


# Create your views here.
# users = ['user1', 'user2', 'user3']


def platform(request):
    return render(request, 'first_task/platform.html')

def games(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'first_task/games.html', context)

def cart(request):
    return render(request, 'first_task/cart.html')
def sign_up_by_html(request):
    users = Buyer.objects.all()

    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password != repeat_password:
            info['error'] = "Пароли не совпадают"
            return HttpResponse('Пароли не совпадают')
        elif age < 18:
            info['error'] = "Вы должны быть старше 18"
            return HttpResponse('Вы должны быть старше 18')
        elif username in users:
            info['error'] = "Пользователь уже существует"
            return HttpResponse('Пользователь уже существует')
        else:
            info['welcome_message'] = f"Приветствуем, {username}!"  # Приветственное сообщение

        return HttpResponse(f"Приветствуем, {username}!")

    return render(request, 'first_task/registration_page.html')


def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = "Пароли не совпадают"
                return HttpResponse('Пароли не совпадают')
            elif age < 18:
                info['error'] = "Вы должны быть старше 18"
                return HttpResponse('Вы должны быть старше 18')
            elif username in users:
                info['error'] = "Пользователь уже существует"
                return HttpResponse('Пользователь уже существует')
            else:
                info['welcome_message'] = f"Приветствуем, {username}!"
            return HttpResponse(f"Приветствуем, {username}!")
    else:
        form = UserRegister()
        info['message'] = form

    return render(request, 'first_task/registration_page.html', {'form': form})
