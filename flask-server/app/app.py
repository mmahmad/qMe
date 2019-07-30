import os
import uuid
import random
import string
import hashlib

from flask import Flask, render_template, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# from app.models.model_merchant.merchant import Merchant

database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    # dbuser=os.environ['postgres'],
    # dbpass=os.environ['docker'],
    # dbhost=os.environ['localhost'],
    # dbname=os.environ['qMe']
    dbuser='postgres',
    dbpass='docker',
    dbhost='postgres',
    dbname='qMe'
)

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# import app.models.model_merchant.merchant as Merchant
from models.model_merchant import merchant
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

"""
curl -X POST \
  http://localhost:5000/api/v1/merchant/register \
  -H 'Postman-Token: 719bdb25-d0b0-4fb8-9afb-5487b830dc28' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F 'merchant_name=Aldy'\''s' \
  -F 'merchant_address_1=410 E University' \
  -F merchant_address_2= \
  -F merchant_address_city=Champaign \
  -F merchant_address_state=IL \
  -F merchant_address_zipcode=61820 \
  -F merchant_address_country=USA \
  -F merchant_primary_email=walmart5@gmail.com \
  -F merchant_primary_phone=2175422

Response:

{
  "merchant_access_id": "gkqmvtrvifrkgffihlpoyttm",
  "merchant_access_key": "oqrephadtijpeofyvdakuascnsczhgubsbserngsbawypmfuhrcauouuoffjsfaz",
  "merchant_address_1": "410 E University",
  "merchant_address_2": "",
  "merchant_address_city": "Champaign",
  "merchant_address_country": "USA",
  "merchant_address_state": "IL",
  "merchant_address_zipcode": "61820",
  "merchant_auth": "nrsbkfqgsgckwpqo",
  "merchant_name": "Aldy's",
  "merchant_primary_email": "walmart5@gmail.com",
  "merchant_primary_phone": "2175422",
  "merchant_uuid": "700769e9-5a1d-4941-b24f-cf15fde640c7"
}
"""
@app.route('/api/v1/merchant/register', methods=['POST'])
def register_merchant():
    merchant_uuid = str(uuid.uuid4())

    merchant_name = request.form.get('merchant_name')
    merchant_address_1 = request.form.get('merchant_address_1')
    merchant_address_2 = request.form.get('merchant_address_2')
    merchant_address_city = request.form.get('merchant_address_city')
    merchant_address_state = request.form.get('merchant_address_state')
    merchant_address_zipcode = request.form.get('merchant_address_zipcode')
    merchant_address_country = request.form.get('merchant_address_country')
    merchant_primary_email = request.form.get('merchant_primary_email')
    merchant_primary_phone = request.form.get('merchant_primary_phone')

    # RETURN uuid + merchant_auth + merchant_access_id + merchant_access_key + above body
    merchant_auth = generate_merchant_auth()

    merchant_access_id = generate_merchant_access_id()
    merchant_access_key = generate_merchant_access_key()

    merchant_access_id_hashed = hashlib.sha512(merchant_access_id.encode()).hexdigest() # string needs to be encoded before hashed
    merchant_access_key_hashed = hashlib.sha512(merchant_access_key.encode()).hexdigest()

    merch = merchant.Merchant(uuid=merchant_uuid, name=merchant_name, address_1=merchant_address_1, address_2=merchant_address_2, address_city=merchant_address_city, address_state=merchant_address_state, address_zipcode=merchant_address_zipcode,
                        address_country=merchant_address_country, primary_email=merchant_primary_email, primary_phone=merchant_primary_phone, auth_code=merchant_auth, access_id=merchant_access_id_hashed, access_key=merchant_access_key_hashed)

    db.session.add(merch)
    try:
        db.session.commit()
        failed = False
    # except IntegrityError as ie:
    #     print(ie)
    #     db.session.rollback()
    #     failed = True
    #     existing = db.session.query(merchant.Merchant).filter_by(primary_email=merchant_primary_email).one()
    #     return jsonify(error=500, details='* INTEGRITY FAILURE, EMAIL IN USE: {}'.format(existing), text=str(ie)), 500
    except Exception as e:
        print(e)
        db.session.rollback()
        failed = True
        return jsonify(error=500, text=str(e)), 500

    if not failed:
        return jsonify({
            'merchant_uuid': merchant_uuid,
            'merchant_auth': merchant_auth,
            'merchant_access_id': merchant_access_id,
            'merchant_access_key': merchant_access_key,
            # request body
            'merchant_name': merchant_name,
            'merchant_address_1': merchant_address_1,
            'merchant_address_2': merchant_address_2,
            'merchant_address_city': merchant_address_city,
            'merchant_address_state': merchant_address_state,
            'merchant_address_zipcode': merchant_address_zipcode,
            'merchant_address_country': merchant_address_country,
            'merchant_primary_email': merchant_primary_email,
            'merchant_primary_phone': merchant_primary_phone 
        }), 200

@app.route('/api/v1/counter/merchant/<merchant_uuid>/register', methods=['POST'])
def register_merchant_counter(merchant_uuid):
    return jsonify({
    'merchant_uuid': merchant_uuid,
    'merchant_access_id': merchant_access_id,
    'merchant_access_key': merchant_access_key
    }), 200

def generate_merchant_auth(stringLength=16):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def generate_merchant_access_id(stringLength=24):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def generate_merchant_access_key(stringLength=64):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


# @app.route('/registerUser', methods=['POST'])
# def regiserUser():
#     failed = False
#     # return render_template('guest_registration.html')
#     from app.models import User
#     from models import User
#     fname = request.form.get('fname')
#     lname = request.form.get('lname')
#     email = request.form.get('email')
#     username = request.form.get('username')
#     pwd = request.form.get('pwd')
#     phone_number = request.form.get('phone_number')

#     user = User(id=None, fname=fname, lname=lname, email=email,
#                 phone_number=phone_number, username=username, pwd=pwd)
#     db.session.add(user)
#     try:
#         db.session.commit()
#         failed = False
#     except Exception as e:
#         # log
#         print(e)

#         db.session.rollback()
#         db.session.flush()
#         failed = True
#         return jsonify(error=500, text=str(e)), 500

#     if not failed:
#         return jsonify({
#             'fname': fname,
#             'lname': lname,
#             'email': email,
#             'phone_number': phone_number,
#             'username': username
#         }), 200


# @app.route('/register', methods=['POST'])
# def register_guest():
#     from models import Guest
#     name = request.form.get('name')
#     email = request.form.get('email')

#     guest = Guest(name, email)
#     db.session.add(guest)
#     db.session.commit()

#     return render_template(
#         'guest_confirmation.html', name=name, email=email)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
