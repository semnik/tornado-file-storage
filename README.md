# Решение задачи описанной ниже

1)      Написать микро сервис, с функционалом:

a.       загрузить  файл, получить uuid

реализован методом PUT ,в ответе формата json содержится uuid

b.       проверить наличие по uuid

реализован методом HEAD, uuid передается переменной file_uuid в Headers
200 - файл есть, 204 - файла нет

c.       скачать используя uuid

реализован методом GET , uuid передается переменной file_uuid в Headers 
200 - response body содержит файл, 204 - файла нет

2)      реализовать этот сервис в формате multithreading или async

3)      upload, download, check - методы покрыть тестами (pytest | unittest | doctest)
не сделано, планирую дорабатывать на следующих выходных 

4)      завернуть в docker (ubuntu | alpine)
Dockerfile есть в репозитории, публичный образ доступен , чтобы запустить нужно выполнить  
docker pull 24031993/tornado_file_storage
docker run 24031993/tornado_file_storage



