# Intelligent Tutoring System - Web App

#### Before setting up the Web App please start the API server as steps displayed [here](https://github.com/quabanc/BE-Project).

#### Basic System Prerequisites:
```
Python >= 3.6
virtualenv >= 16.0.0
```

#### Fork this repo and run these commands after cloning the project and go inside the directory:
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

You can access the web app at [http://localhost:8000](http://localhost:8000)
