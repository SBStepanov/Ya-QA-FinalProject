# Сергей Степанов, группа 8а-Earth
# Финальный проект

import requests
import configuration
import data

# создание нового заказа
def post_new_order():
    return requests.post(configuration.SERVER_MAIN_URL + configuration.CREATE_ORDER,
           json=data.order_body)

# получение информации о новом заказе
def get_order(track_number):
    return requests.get(configuration.SERVER_MAIN_URL + configuration.GET_ORDER_BY_TRACK,
           params={"t": track_number})
