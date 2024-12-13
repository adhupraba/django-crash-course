# Setting up the project

1. Clone the project
2. Create a .venv environment using the `python -m venv .venv` command
3. Activate the environment using the `source .venv/bin/activate` command
4. Go into the `myproject` folder and install the dependencies using the `pip install -r requirements.txt` command
5. To deactivate the environment use the `deactivate` command

---

#### Note: This project uses sqlite database

The sqlite database should be present in the root of the parent `myproject` folder

---

# Running the project

> `cd` into the root `myproject` folder and run the following commands when needed

Create migration files

```sh
python manage.py makemigrations
```

Apply migrations

```sh
python manage.py migrate
```

Create a super user

```sh
python manage.py createsuperuser
```

Run the project at a default port

```sh
python manage.py runserver
```

Run the project at a custom port

```sh
python manage.py runserver 5000
```

Create a module

```sh
python manage.py startapp <module_name>
```

Collect all static files like CSS, JS from the project

```sh
python manage.py collectstatic
```
