try:
    from itertools import groupby  # Импортируем функцию groupby из модуля itertools

    # Исходный список кортежей (производитель, модель)
    cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Toyota', 'Yaris'),
                 ('Фиат', '500'), ('Фиат', 'Панда'), ('Тойота', 'Камри 30')]

    # Сортируем список по производителю
    sorted_cars_list = sorted(cars_list, key=lambda x: x[0])

    # Группируем данные по производителю
    grouped_cars = {key: list(group) for key, group in groupby(sorted_cars_list, key=lambda x: x[0])}

    # Выводим результат
    for manufacturer, models in grouped_cars.items():
        print(f'{manufacturer} {len(models)} -')  # Выводим название производителя и количество моделей
        for model in models:
            print(f'  - {model[1]}')  # Выводим модели, относящиеся к данному производителю

except Exception as e:
    print("Произошла ошибка:", e)  # Если возникла ошибка, выводим сообщение об ошибке
