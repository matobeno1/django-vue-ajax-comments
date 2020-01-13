# Add comments dynamically
(**Warning, the code is messy and fast-written.**)

Backend is built with Django, frontend runs on Vue.js (+ Axios for ajax calls)

## How to run this?
You may need to install Pipenv or create your own virtual environment. Otherwise you can 
just start the Django dev server and see the code.
```bash
pipenv install
pipenv shell
python3 bookstore/manage.py runserver
```

For CRUD operations on books or comments login at `127.0.0.1/admin` as `root` with password `root`.

