По-русски | [In english](docs_eng/README.md)
# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".


## Как использовать?
Python3 должен быть уже установлен.

Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей.
Открываем командную строку клавишами Win+R и вводим:
```commandline
pip install -r requirements.txt
```
Рекомендуется использовать virtualenv/venv для изоляции проекта.
(https://docs.python.org/3/library/venv.html)

В корневой папке скрипта должен быть файл Excel с именем "wine3.xlsx", 
в котором перечислены все товары.
Формат всех ячеек - общий. Заголовки столбцов:
```
Категория	Название	Сорт	Цена	Картинка	Акция
```
Шаблон файла с образцом заполнения прилагается.


## Запуск

- Скачайте код
- Запустите сайт командой 
```commandline
python3 main.py
```
или
```commandline
python main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цель проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
