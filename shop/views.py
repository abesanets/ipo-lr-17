from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    """Главная страница с ссылками на остальные страницы"""
    return HttpResponse(
        "Главная страница\n\n"
        "Доступные разделы:\n"
        "1. О магазине: http://127.0.0.1:8000/shop-info/\n"
        "2. Об авторе: http://127.0.0.1:8000/about/\n",
        content_type="text/plain; charset=utf-8"
    )


def about(request):
    """Страница об авторе"""
    return HttpResponse(
        "Страница об авторе\n\n"
        "ФИО: Бесанец Алексей Александрович\n"
        "Группа: 88ТП\n"
        "Лабораторная работа №17\n",
        content_type="text/plain; charset=utf-8"
    )


def shop_info(request):
    """Страница о магазине"""
    return HttpResponse(
        "Информация о магазине\n\n"
        "Тема лабораторной работы: Создание и базовая настройка приложений Django\n"
        "Описание: Магазин предлагает широкий ассортимент электроники -\n"
        "смартфоны, ноутбуки, планшеты, аксессуары и многое другое.\n"
        "Мы работаем для вас с 2024 года.\n",
        content_type="text/plain; charset=utf-8"
    )