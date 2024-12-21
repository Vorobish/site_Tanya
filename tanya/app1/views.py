import datetime

from django.shortcuts import render
from app1.models import SignUp


def base(request):
    '''
        Главная страница
    '''
    header = 'Главная страница'
    content = 'Рады Вас видеть'
    text = ''
    with open("C:/Users/nasty/Desktop/Таня/pythonProjectTanya/tanya/static/text_home_page_small",
              encoding="utf-8") as small:
        header = small.read()
    with open("C:/Users/nasty/Desktop/Таня/pythonProjectTanya/tanya/static/text_home_page_big",
              encoding="utf-8") as big:
        text = big.read()
    context = {
        'header': header,
        'content': content,
        'text': text,
    }
    return render(request, 'base.html', context)


def about(request):
    '''
        Обо мне
    '''
    header = 'Обо мне'
    content = 'инфо обо мне'
    text = ''
    # with open("C:/Users/nasty/Desktop/Таня/pythonProjectTanya/tanya/static/text_about_small",
    #           encoding="utf-8") as small:
    #     header = small.read()
    # with open("C:/Users/nasty/Desktop/Таня/pythonProjectTanya/tanya/static/text_about_big",
    #           encoding="utf-8") as big:
    #     text = big.read()
    context = {
        'header': header,
        'content': content,
        'text': text,
    }
    return render(request, 'about.html', context)


def contacts(request):
    '''
        Контакты и форма записи на консультацию
    '''
    messages = ''
    if request.method == 'POST':
        if 'register' in request.POST:
            name = str(request.POST.get('name'))
            phone = str(request.POST.get('phone'))
            email = str(request.POST.get('email'))
            comment = str(request.POST.get('comment'))
            if len(name) > 2 and len(phone) > 4:
                SignUp.objects.create(name=name,
                                      phone=phone,
                                      email=email,
                                      comment=comment)
                messages = 'Запись зарегистрирована'
            else:
                messages = 'Запись не зарегистрирована'
    # header = 'Контакты'
    content = 'Запишитесь на консультацию'
    # with open("C:/Users/nasty/Desktop/Таня/pythonProjectTanya/tanya/static/text_contacts",
    #           encoding="utf-8") as small:
    #     header = small.read()
    context = {
        # 'header': header,
        'content': content,
        'messages': messages,
    }
    return render(request, 'contacts.html', context)








