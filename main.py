from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime
import pandas
import collections

from jinja2 import Environment, FileSystemLoader, select_autoescape


ORGANIZATION_CREATION_YEAR = 1920


def choosing_year_prefix(age):
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


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    age = datetime.today().year - ORGANIZATION_CREATION_YEAR
    wines = pandas.read_excel('wine3.xlsx', na_values='-', keep_default_na=False).to_dict('records')

    new_wine_set = collections.defaultdict(list)
    for wine in wines:
        new_wine_set[wine['Категория']].append(wine)

    rendered_page = template.render(
        age_text=f'{age} {choosing_year_prefix(age)}',
        new_wine_set=new_wine_set
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
