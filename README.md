# Initialisation

1. First clone the repo to your local system. `git clone https://github.com/ollie-byrne99/Lap_4_Server.git`

2. Next you must install pipenv to your PC, to initiate a virtual python environment to manage the necessary packages for this application `pip install pipenv`

3. Next, once inside the server folder, you must install all the required packages to your environment. Run `pipenv install -r requirements.txt`.

4. You also need to create a .env file in your directory. The contents of this should be as follows:

    i. FLASK_APP=app 
    ii. FLASK_DEBUG=1
    iii. DB_URL='postgresql://'
    iv. JWT_SECRET_KEY='x'

You must input your own postrges SQL database into DB_URL. Elephant SQL for cloud storage is a good choice.
JWT_SECRET_KEY can be set to any string. This must be kept secret.

# Usage

1. To seed the database input `pipenv run seed-db`

2. To launch the server input  `pipenv run dev`

3. Access the server at http://localhost:5000/


waitress==2.1.2
pipenv run pip freeze > requirements.txt
