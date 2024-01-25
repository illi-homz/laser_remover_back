# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api import models
import json
from django.views.decorators.csrf import csrf_exempt
import environ
import os
from pathlib import Path
import requests

env = environ.Env(
    BOT_TOKEN=(str, ''),
    URL_TELEGRAM=(str, ''),
    CHAT_ID=(str, ''),
)

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

BOT_TOKEN = env('BOT_TOKEN')
URL_TELEGRAM=env('URL_TELEGRAM')
URL_MESSAGE = f'{URL_TELEGRAM}/bot{BOT_TOKEN}/sendMessage'
CHAT_ID = int(env('CHAT_ID'))

def create_telegram_msg(msg):
    return {'chat_id': CHAT_ID, 'text': msg, 'parse_mode': 'markdown'}

def create_services_msg(data):
    messegers = data['messegers']
    contacts = '' if not len(messegers) else ', '.join(messegers)
    
    msg = '*Сообщение с сайта*\n\n'
    msg += f'#Клиент: {data["name"]} {data["lastname"]}\n'
    msg += f'#Тел: {data["phone"]}\n'
    msg += f'#Услуга: {data["service"]}\n'
    # msg += f'#Контакты: телефон' + contacts
    msg += f'#Контакты: ' + contacts

    return msg

def send_event_to_telegram(data):
    message = create_services_msg(data)
    print('URL_MESSAGE', URL_MESSAGE)
    resp = requests.post(URL_MESSAGE, create_telegram_msg(message))
    print('send_event_to_telegram response', resp)

@csrf_exempt
def send_form_to_telegram(request):
    if request.method != 'POST':
        return JsonResponse({"status": "error", "code": 400, 'message': "Go away!"})

    try:
        data = json.loads(request.body)
        send_event_to_telegram(data)
    except:
        return JsonResponse({"status": "error", "code": 400, 'message': "Json parse error"})

    return JsonResponse({"status": "ok", "code": 200, 'message': "You good man!"})
