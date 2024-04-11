# Домашнее задание по теме "Регулярные выражения"
#
# Цель задания:
#
# Закрепить написание шаблонов с применением регулярных выражений.
# Написать программу-поисковик, отслеживающий верные ссылки по заданному шаблону.
#
# Задание:
#
# Разработайте функцию для извлечения информации из HTML-текста (строки Python) о ссылках на изображения (URL-адресах
# картинок). Функция должна находить все ссылки на изображения в форматах JPEG, JPG, PNG или GIF и возвращать их список.
#
# 1. Создайте функцию extract_image_links(html_text), которая принимает HTML-текст и извлекает ссылки на изображения.
# 2. Используйте регулярные выражения для поиска URL-адресов картинок с расширениями .jpg, .jpeg, .png или .gif.
# 3. Верните список всех найденных ссылок на изображения.
#
#
# Пример работы функции:
#
# sample_html = "<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'>
# <img src='https://example.com/image3.gif'>"
#
# image_links = extract_image_links(sample_html)
# if image_links:
#   for image_link in image_links:
#     print(image_link)
# else:
#   print("Нет ссылок с картинками в HTML тексте.")
#
# Вывод на консоль:
# https://example.com/image1.jpg
# http://example.com/image2.png
# https://example.com/image3.gif
#
# Примечания:
# Вам могут понадобится следующие спец. символы: / ? [] | +
# Учтите что 'http' это подстрока строки 'https'.
#
# Файл с исходным кодом прикрепите к домашнему заданию.

import re


class RegularExpressions:
    def extract_image_links(self, matched):
        image_links = r'\w{4,5}\W{3}\w{7}.\w{3}.\w{5}\d.(?:jpg|jpeg|gif|png)'
        html_text = ("<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'>"
                     " <img src='https://example.com/image3.gif'>")

        matched = re.search(image_links, html_text)
        searching_iterator = re.finditer(image_links, html_text)
        for matched in searching_iterator:
            print(f'Следующее совпадение: {matched.group()}')



regex = RegularExpressions()    # Создаем экземпляр класса
regex.extract_image_links('matched')    # Вызываем метод и выводим результат