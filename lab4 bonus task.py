# Запрашиваем у пользователя ввод текста, который нужно зашифровать.
text = input("Введите текст для шифрования: ")

# Запрашиваем у пользователя ввод сдвига, который будет использован для шифрования.
shift = int(input("Введите сдвиг: "))

# Инициализируем пустую строку для сохранения зашифрованного текста.
encrypted_text = ""

# Начинаем цикл, который перебирает каждый символ в исходном тексте.
for char in text:
    if char.isalpha():
        # Если символ - буква, проверяем, является ли она заглавной или строчной.
        # Затем вычисляем зашифрованный символ с использованием шифра Цезаря.
        shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
        encrypted_text += shifted_char  # Добавляем зашифрованный символ к зашифрованному тексту.
    else:
        encrypted_text += char  # Если символ не является буквой, оставляем его без изменений.

# Выводим зашифрованный текст.
print("Зашифрованный текст:", encrypted_text)

input_data = (5, 55, 10, 1, 0, 1, 55, 77, 10, 5, 5, 55, 77)
element_count = count_occurrences(input_data)

most_popular, least_popular, frequent_elements = find_popular_elements(input_data)
print_results(input_data, most_popular, least_popular, frequent_elements)
