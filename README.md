# python-api-boilerplate

as root:

    apt-get install python3 python3-pip
    pip3 (or pip) install -U pip virtualenv

then, as a user, create your virtualenv:

    virtualenv -p /usr/bin/python3 venv
    source venv/bin/activate
    pip install -r requirements.txt

to create database :

    python main.py initdb

to run a shell:

    python main.py shell

for example, in a shell, add a user:

    In [1]: from app.models.user import User

    In [2]: user = User("jean", "valjean", "toto@toto.com", "pass")

    In [3]: user.save()

    In [4]: exit

then, run the API:

    python main.py run

and in an other shell, you can curl it:

    curl http://127.0.0.1:5000/api/users | python -m json.tool

    [
        {
            "email": "toto@toto.com",
            "firstName": "jean",
            "id": 1,
            "lastName": "valjean"
        }
    ]
