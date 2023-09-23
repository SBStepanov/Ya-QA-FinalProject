# Сергей Степанов, группа 8а-Earth
# Финальный проект

# !!! Перед запуском установить библиотеки requests и pytest !!!

import post_get_requests

# возврат трек-номера заказа
def get_track_number():
    track_number = post_get_requests.post_new_order()
    return track_number.json()["track"]

# тест: код ответа 200 -> заказ создан в БД
def test_check_new_order():
    track_number = get_track_number()
    get_response = post_get_requests.get_order(track_number)
    assert get_response.status_code == 200


