# itw-2-django_project
# restaurant-management-system
# Restaurant management system website (Django)

### Technologies used
- MySQL
- Django Framework
- HTML & CSS
- Bootstrap

### requirements 
`Python (version >= 3.8) and Pip`

### Installation
- [Linux (Ubuntu)](#linux-installation)
- [Windows](#windows-installation)

# windows installation

- install `pipenv` to create virtual environment.

```cmd
pip install pipenv
```
- clone the repo to any directory

```cmd
git clone https://github.com/sasikiranE/restaurant-management-system.git
```

- remove the Pipfile in the project directory. (if your python version is not 3.8)

- navigate to the project directory(`restaurant-management-system/`), create and activate virtual environment using single command

```cmd
pipenv shell
```

- install the requirements

```cmd
pipenv install -r requirements.txt
```

- run the server

```cmd
python manage.py runserver
```

# linux installation

- install `pipenv` to create virtual environment.

```cmd
sudo apt install pipenv
```
- clone the repo to any directory

```cmd
git clone https://github.com/sasikiranE/restaurant-management-system.git
```

- remove the Pipfile in the project directory. (if your python version is not 3.8)

- navigate to the project directory(`restaurant-management-system/`), create and activate virtual environment using single command

```cmd
pipenv shell
```

- install the requirements

```cmd
pipenv install -r requirements.txt
```

- run the server

```cmd
python3 manage.py runserver
```