In english | [По-русски](../README.md)

# New Russian wine

Website of the author's wine store "New Russian wine".

## How to use?
Python 3 should already be installed.

Then use pop (or pop3, there is a conflict with Python 2) to install dependencies.
Open the command line with the Win+R keys and enter:
```command line
pip install -r requirements.txt
```
It is recommended to use virtualenv/v env for project isolation.
(https://docs.python.org/3/library/venv.html)

In the root folder of the script there should be an Excel file named "wine3.xlsx ",
which lists all the products.
The format of all cells is common. Column headers:
```
Category Name Grade Price Picture Promotion
```
A template file with a sample filling is attached.


## Launch

- Download the code
- Launch the site with the 
```commandline
python3 main.py
```
or
```
python main.py
```
- Go to the website at [http://127.0.0.1:8000 ](http://127.0.0.1:8000 ).


### Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
