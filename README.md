# Решение задачи описанной ниже

1)      Написать микро сервис, с функционалом:

a.       загрузить  файл, получить uuid

реализован методом PUT ,в ответе формата json содержится uuid

b.       проверить наличие по uuid

реализован методом HEAD, uuid передается переменной file_uuid в Headers

c.       скачать используя uuid

реализован методом GET , uuid передается переменной file_uuid в Headers 

2)      реализовать этот сервис в формате multithreading или async

3)      upload, download, check - методы покрыть тестами (pytest | unittest | doctest)
не сделано
4)      завернуть в docker (ubuntu | alpine)
Dockerfile публичный образ доступен  


Плюсом будет:

-   соответствие PEP 8

-   документирование кода

