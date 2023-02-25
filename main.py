from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime
import pandas
import collections
import argparse
import os
from environs import Env
from jinja2 import Environment, FileSystemLoader, select_autoescape


ORGANIZATION_CREATION_YEAR = 1920


def select_year_prefix(age):
    last_dig = age % 10
    if 10 < age < 20:
        year_prefix = 'лет'
    elif 1 < last_dig < 5:
        year_prefix = 'года'
    elif last_dig == 1:
        year_prefix = 'год'
    else:
        year_prefix = 'лет'
    return year_prefix


def get_wines_from_file(path):
    wines = pandas.read_excel(path, na_values='-', keep_default_na=False).to_dict('records')
    return wines


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    age = datetime.today().year - ORGANIZATION_CREATION_YEAR

    wine_parser = argparse.ArgumentParser(description='Сайт магазина авторского вина "Новое русское вино"')
    wine_parser.add_argument(
        'path',
        nargs='?',
        default=os.path.join(os.getcwd(), 'wine.xlsx'),
        help='директория с файлом wine.xlsx (по умолчанию - ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ/wine.xlsx)'
    )

    path = wine_parser.parse_args().path
    try:
        wines = get_wines_from_file(path)
    except (FileNotFoundError, ValueError) as error:
        print(f'Неверно указан путь к файлу.\nОшибка: {error}')
        environs = Env()
        try:
            environs.read_env("setup.txt", recurse=False)
            path = environs.str('PATH_TO_WINE_FILE')
            wines = get_wines_from_file(path)
        except (FileNotFoundError, ValueError) as error:
            print(f'setup.txt в корневой папке не найден или в нем не указан путь к файлу вин в PATH_TO_WINE_FILE.\n'
                  f'Ошибка: {error}')
            exit()

    print(f'Сайт запущен с файлом базы данных {path}')
    new_wine_set = collections.defaultdict(list)
    for wine in wines:
        new_wine_set[wine['Категория']].append(wine)

    rendered_page = template.render(
        age_text=f'{age} {select_year_prefix(age)}',
        new_wine_set=new_wine_set
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
