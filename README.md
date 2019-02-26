#28 февраля будет окончательный вариант для демонстрации.
После, время от времени буду доводить до совершенства и напишу нормальный README,
где изложу на английском описание принятых решенией в проектировании, выбора определенных функций и анализа имеющейся информации по async I/O  via Tornado API 

# Решение задачи описанной ниже

1)      Написать микро сервис, с функционалом:

a.       загрузить  файл, получить uuid

реализован методом POST ,в ответе формата json содержится uuid

b.       проверить наличие по uuid

реализован методом GET, Например: http://localhost:9999/check/c03570a3-c1bd-49e6-ae1a-14845bc6f5ef


200 - файл есть, 204 - файла нет

c.       скачать используя uuid

реализован методом GET , Например: http://localhost:9999/download/c03570a3-c1bd-49e6-ae1a-14845bc6f5ef


200 - response body содержит файл, 204 - файла нет

2)      реализовать этот сервис в формате multithreading или async


Осталось upload реализовать с помощью async


3)      upload, download, check - методы покрыть тестами (pytest | unittest | doctest)


Покрыл примитивными тестами , планирую довести до качественного вида 26-27 числа 



4)      завернуть в docker (ubuntu | alpine)



Dockerfile есть в репозитории, публичный образ доступен , чтобы запустить нужно выполнить  


docker pull 24031993/tornado_file_storage


docker run 24031993/tornado_file_storage


docker run -p 9999:9999 24031993/tornado_file_storage

Работоспособность можно проверить следующими командами :

1) curl http://localhost:9999

2) curl http://localhost:9999/download/57538b19-4b60-4fe3-ae42-6b9744d1bc8a

3) touch foo

4) curl -i -X POST http://localhost:9999/upload \
  -H "Content-Type: text/xml" \
  --data-binary "@./foo"
  
  



