try:
    # Sample Input
    tuple_A = (1, 2, 3, 4, 5, 6, 7)
    tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)

    # Находим среднюю позицию для обоих кортежей
    midpoint_A = len(tuple_A) // 2
    midpoint_B = len(tuple_B) // 2

    # Сцепляем первую половину кортежа A с второй половиной кортежа B
    final_tuple = tuple_A[:midpoint_A] + tuple_B[midpoint_B:]

    # Выводим объединенный кортеж
    print(final_tuple)

except ValueError:
    print("Ввод неверный")  # Если возникнет ошибка типа ValueError, выводим сообщение об ошибке
