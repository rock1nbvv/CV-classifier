# Fuzzy CV classifier

### To run the app, follow these instructions:

1. Activate virtual environment and install dependencies for Python in the backend folder:\
   `python3 -m venv env`
   `source env/bin/activate`
   `python3 -m pip install -r requirements.txt`

2. Create DB with the schema (you can skip this step since we have already pushed db in repo):\
   `export FLASK_APP=app`
   `flask shell`
   `from app import db`
   `from models import Rating`
   `db.create_all()`\
   Make sure db.sqlite is created in the backend folder

3. Run backend:
   `flask run`

4. Install npm packages in the frontend folder:
   `npm install`

5. Run frontend:
   `npm run serve`
   
