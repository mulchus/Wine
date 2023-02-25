In english | [По-русски](../README.md)

# New Russian wine

Website of the author's wine store "New Russian wine".

## How to use?
Python should already be installed.

It is recommended to use virtualenv/v env for project isolation.
(https://docs.python.org/3/library/venv.html)

Then use pop (or pop3, there is a conflict with Python 2) to install dependencies.
Open the command line with the Win+R keys and enter:
```command line
pip install -r requirements.txt
```


In the root folder of the script there should be an Excel file named "wine.xlsx",
which lists all the products.
The format of all cells is common. Column headers:
```
Category Name Grade Price Picture Promotion
```
A template file with a sample filling is attached.

The file may be located in a different path.

The path is set in the command line of the script startup. If the script is run without a database path,
the file is searched by default ``wine.xlsx`` in the root directory with the script.
If it is not there, the path is taken from the settings in the file setup.txt , example:
``
PATH_TO_WINE_FILE='e:\Python\Wine\wine.xlsx '
``

## Launch

- Download the code
- Launch the site with the 
```commandline
python main.py [path to database.xlsx]
```
- Go to the website at [http://127.0.0.1:8000 ](http://127.0.0.1:8000 ).


### Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
