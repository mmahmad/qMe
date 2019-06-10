import os

from flask import Flask, render_template, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
#     # dbuser=os.environ['postgres'],
#     # dbpass=os.environ['docker'],
#     # dbhost=os.environ['localhost'],
#     # dbname=os.environ['qMe']
#     dbuser='postgres',
#     dbpass='docker',
#     dbhost='localhost',
#     dbname='qMe'
# )

database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    # dbuser=os.environ['postgres'],
    # dbpass=os.environ['docker'],
    # dbhost=os.environ['localhost'],
    # dbname=os.environ['qMe']
    dbuser='postgres',
    dbpass='docker',
    # dbhost='localhost',
    dbhost='postgres',
    # dbhost='172.26.0.2'
    dbname='qMe'
)

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# initialize the database connection
db = SQLAlchemy(app)

# initialize database migration management
migrate = Migrate(app, db)

@app.route('/')
def hello_whale():
    return 'Hello World!'

@app.route('/guest')
def view_registered_guests():
    from models import Guest
    guests = Guest.query.all()
    return render_template('guest_list.html', guests=guests)


@app.route('/registerUser', methods=['POST'])
def regiserUser():
    failed=False
    # return render_template('guest_registration.html')
    from models import User
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    username = request.form.get('username')
    pwd = request.form.get('pwd')
    phone_number = request.form.get('phone_number')

    user = User(id=None, fname=fname, lname=lname, email=email, phone_number=phone_number, username=username, pwd=pwd)
    db.session.add(user)
    try:
        db.session.commit()
        failed=False
    except Exception as e:
        # log
        print(e)

        db.session.rollback()
        db.session.flush()
        failed=True
        return jsonify(e), 400

    if not failed:
        return jsonify({
            'fname': fname,
            'lname': lname,
            'email': email,
            'phone_number': phone_number,
            'username': username
        }), 200
    # else:
    #     return jsonify({
    #         'fname': fname,
    #         'lname': lname,
    #         'email': email,
    #         'phone_number': phone_number,
    #         'username': username
    #     }), 400


@app.route('/register', methods=['POST'])
def register_guest():
    from models import Guest
    name = request.form.get('name')
    email = request.form.get('email')

    guest = Guest(name, email)
    db.session.add(guest)
    db.session.commit()

    return render_template(
        'guest_confirmation.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')