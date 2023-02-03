from django.http import HttpResponse
from . import models
import json



def get_hash(request, url):# получение хеша длинной ссылки
    hash = models.Urls().set_url(url)
    response = {
        'hash':hash
    }
    return HttpResponse(json.dumps(response), content_type='application/json')


def get_num_click_url(request, hash_url):# получение всех кликов по ссылке
    try:
        num = models.Urls.objects.filter(hash_url=hash_url).values('clicks')
        return HttpResponse(json.dumps(num[0]), content_type='application/json')
    except:
        return HttpResponse(json.dumps({'clicks':'HASH is invalid'}), content_type='application/json')


def get_num_click_url_stats(request, hash_url):# получение всех кликов с датой
    try:
        date_list_array = models.Clicks.objects.filter(hash_url=hash_url).values('date')
        unic_date_array = []

        # Получение массива со всеми датами для хеша .
        for date in date_list_array:
            if str(date['date']) in unic_date_array:
                continue
            else:
                unic_date_array.append(str(date['date']))

        # Создание словаря со всеми датами
        count_date_click_list = dict()
        for unic_date in unic_date_array:
            count_date_click_list[unic_date] = 0

        # Заполнитель словаря по количествам входов даты('ДАТА:количество входов')
        for unic_date in unic_date_array:
            for date_list in date_list_array:
                if unic_date == str(date_list['date']):
                    count_date_click_list[unic_date] += 1
                    
        return HttpResponse(json.dumps(count_date_click_list), content_type='application/json')
    except:
        return HttpResponse(json.dumps({'date': 'HASH is invalid'}), content_type='application/json')


