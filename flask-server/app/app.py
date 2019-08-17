from datetime import datetime
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
# from models.model_merchant import model_merchant_timings


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

"""
curl -X POST \
  http://localhost:5000/api/v1/merchant/5a795a93-c851-44c4-9017-2c83234db208/timings \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 1696' \
  -H 'Content-Type: multipart/form-data; boundary=--------------------------338275155018184137878876' \
  -H 'Host: localhost:5000' \
  -H 'Postman-Token: b491c5ea-db01-4052-a58f-8ddd32239251,56b6b96d-8915-43e4-bea0-319aa84b8ac7' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F saturday_start=7:00am \
  -F saturday_end=5:00pm \
  -F sunday_start=7:00am \
  -F sunday_end=5:00pm \
  -F monday_start=7:00am \
  -F monday_end=5:00pm \
  -F tuesday_start=7:00am \
  -F tuesday_end=5:00pm \
  -F wednesday_start=7:00am \
  -F wednesday_end=5:00pm \
  -F thursday_start=7:00am \
  -F thursday_end=5:00pm \
  -F friday_start=7:00am \
  -F friday_end=5:00pm

response:
{
  "friday_end": "05:00PM",
  "friday_start": "07:00AM",
  "merchant_uuid": "5a795a93-c851-44c4-9017-2c83234db208",
  "monday_end": "05:00PM",
  "monday_start": "07:00AM",
  "saturday_end": "05:00PM",
  "saturday_start": "07:00AM",
  "sunday_end": "05:00PM",
  "sunday_start": "07:00AM",
  "thursday_end": "05:00PM",
  "thursday_start": "07:00AM",
  "tuesday_end": "05:00PM",
  "tuesday_start": "07:00AM",
  "wednesday_end": "05:00PM",
  "wednesday_start": "07:00AM"
}

#####################################################################################

curl -X PUT \
  http://localhost:5000/api/v1/merchant/5a795a93-c851-44c4-9017-2c83234db208/timings \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 292' \
  -H 'Content-Type: multipart/form-data; boundary=--------------------------965584490552121345786645' \
  -H 'Host: localhost:5000' \
  -H 'Postman-Token: d747e4c6-ca0c-4bc9-83af-02d4c1331dec,463efd3a-12ab-4ca3-91a5-b79b07791660' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F saturday_start=1:00pm \
  -F saturday_end=4:00pm

response:
{
  "merchant_uuid": "5a795a93-c851-44c4-9017-2c83234db208",
  "saturday_end": "04:00PM",
  "saturday_start": "01:00PM"
}

#####################################################################################

curl -X GET \
  http://localhost:5000/api/v1/merchant/5a795a93-c851-44c4-9017-2c83234db208/timings \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: localhost:5000' \
  -H 'Postman-Token: 53ba9c16-a1c9-4e1e-a726-48b20829f0f6,a437d8aa-0a12-44f4-ac0c-2349c2b9bacc' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache'

response:

{
  "friday_end": null,
  "friday_start": null,
  "monday_end": null,
  "monday_start": null,
  "saturday_end": "04:24AM",
  "saturday_start": "04:24AM",
  "sunday_end": null,
  "sunday_start": null,
  "thursday_end": null,
  "thursday_start": null,
  "tuesday_end": null,
  "tuesday_start": null,
  "uuid": "35cfc9c6-8336-4b10-b239-7eb1bc11091f",
  "wednesday_end": null,
  "wednesday_start": null
}

"""
@app.route('/api/v1/merchant/<merchant_uuid>/timings', methods=['POST', 'PUT', 'GET'])
def set_merchant_timings(merchant_uuid):
    saturday_start = None
    saturday_end = None
    sunday_start = None
    sunday_end = None
    monday_start = None
    monday_end = None
    tuesday_start = None
    tuesday_end = None
    wednesday_start = None
    wednesday_end = None
    thursday_start = None
    thursday_end = None
    friday_start = None
    friday_end = None

    times = {}

    if request.method == 'POST':
        # TODO
        # if request.form.get('merchant_auth_code'):
        #     merch_auth_code = request.form.get('merchant_auth_code')
            # verify this auth code is valid for this merchant. If so, proceed with POST
        if request.form.get('saturday_start'):
            # t = datetime.strptime('7:00pm', '%I:%M%p').time()
            saturday_start = datetime.strptime(request.form.get('saturday_start'), '%I:%M%p').time()
            times['saturday_start'] = saturday_start.strftime("%I:%M%p")
        if request.form.get('saturday_end'):
            saturday_end = datetime.strptime(request.form.get('saturday_end'), '%I:%M%p').time() 
            times['saturday_end'] = saturday_end.strftime("%I:%M%p")

        if request.form.get('sunday_start'):
            sunday_start = datetime.strptime(request.form.get('sunday_start'), '%I:%M%p').time()
            times['sunday_start'] = sunday_start.strftime("%I:%M%p")
        if request.form.get('sunday_end'):
            sunday_end = datetime.strptime(request.form.get('sunday_end'), '%I:%M%p').time() 
            times['sunday_end'] = sunday_end.strftime("%I:%M%p")

        if request.form.get('monday_start'):
            monday_start = datetime.strptime(request.form.get('monday_start'), '%I:%M%p').time()
            times['monday_start'] = monday_start.strftime("%I:%M%p")
        if request.form.get('monday_end'):
            monday_end = datetime.strptime(request.form.get('monday_end'), '%I:%M%p').time() 
            times['monday_end'] = monday_end.strftime("%I:%M%p")

        if request.form.get('tuesday_start'):
            tuesday_start = datetime.strptime(request.form.get('tuesday_start'), '%I:%M%p').time()
            times['tuesday_start'] = tuesday_start.strftime("%I:%M%p")
        if request.form.get('tuesday_end'):
            tuesday_end = datetime.strptime(request.form.get('tuesday_end'), '%I:%M%p').time()
            times['tuesday_end'] = tuesday_end.strftime("%I:%M%p")

        if request.form.get('wednesday_start'):
            wednesday_start = datetime.strptime(request.form.get('wednesday_start'), '%I:%M%p').time()
            times['wednesday_start'] = wednesday_start.strftime("%I:%M%p")
        if request.form.get('wednesday_end'):
            wednesday_end = datetime.strptime(request.form.get('wednesday_end'), '%I:%M%p').time() 
            times['wednesday_end'] = wednesday_end.strftime("%I:%M%p")

        if request.form.get('thursday_start'):
            thursday_start = datetime.strptime(request.form.get('thursday_start'), '%I:%M%p').time()
            times['thursday_start'] = thursday_start.strftime("%I:%M%p")
        if request.form.get('thursday_end'):
            thursday_end = datetime.strptime(request.form.get('thursday_end'), '%I:%M%p').time() 
            times['thursday_end'] = thursday_end.strftime("%I:%M%p")

        if request.form.get('friday_start'):
            friday_start = datetime.strptime(request.form.get('friday_start'), '%I:%M%p').time()
            times['friday_start'] = friday_start.strftime("%I:%M%p")
        if request.form.get('friday_end'):
            friday_end = datetime.strptime(request.form.get('friday_end'), '%I:%M%p').time()
            times['friday_end'] = friday_end.strftime("%I:%M%p")

        # m = model_merchant_timings.MerchantTimings(uuid=merchant_uuid, saturday_start=datetime.utcnow().time(), saturday_end=datetime.utcnow().time())
        m = merchant.MerchantTimings(
            uuid=merchant_uuid,
            
            saturday_start=saturday_start,
            saturday_end=saturday_end,

            sunday_start=sunday_start,
            sunday_end=sunday_end,            

            monday_start=monday_start,
            monday_end=monday_end,

            tuesday_start=tuesday_start,
            tuesday_end=tuesday_end,

            wednesday_start=wednesday_start,
            wednesday_end=wednesday_end,

            thursday_start=thursday_start,
            thursday_end=thursday_end,

            friday_start=friday_start,
            friday_end=friday_end
        )
        db.session.add(m)
        try:
            db.session.commit()
            failed = False
        except Exception as e:
            print(e)
            db.session.rollback()
            failed = True
            return jsonify(error=500, text=str(e)), 500

        if not failed:
            result = {
                'merchant_uuid': merchant_uuid
            }
            result.update(times)
            return jsonify(result), 200

    elif request.method == 'PUT':
        # TODO
        # if request.form.get('merchant_auth_code'):
        #     merch_auth_code = request.form.get('merchant_auth_code')
            # verify this auth code is valid for this merchant. If so, proceed with PUT
        times = {}
        form_keys = ['saturday_start', 'saturday_end', 'sunday_start', 'sunday_end', 'monday_start', 'monday_end', 'tuesday_start', 'tuesday_end', 'wednesday_start', 'wednesday_end', 'thursday_start', 'thursday_end', 'friday_start', 'friday_end']

        for key in form_keys:
            if request.form.get(key):
                value = request.form.get(key)
                new_time = datetime.strptime(request.form.get(key), '%I:%M%p').time()
                db.session.query(merchant.MerchantTimings).filter(merchant.MerchantTimings.uuid == merchant_uuid).update({key: new_time})
                times[key] = new_time.strftime("%I:%M%p")

        
        try:
            db.session.commit()
            failed = False
        except Exception as e:
            print(e)
            db.session.rollback()
            failed = True
            return jsonify(error=500, text=str(e)), 500

        if not failed:
            result = {
                'merchant_uuid': merchant_uuid
            }
            result.update(times)
            return jsonify(result), 200
        # raise NotImplementedError
    elif request.method == 'GET':
        props = ['saturday_start', 'saturday_end', 'sunday_start', 'sunday_end', 'monday_start', 'monday_end', 'tuesday_start', 'tuesday_end', 'wednesday_start', 'wednesday_end', 'thursday_start', 'thursday_end', 'friday_start', 'friday_end']
        try:
            # db.session.query(merchant.MerchantTimings).filter(merchant.MerchantTimings.uuid == merchant_uuid).fetch
            # timings = db.session.query(merchant.MerchantTimings).get(merchant_uuid)
            # timings = db.session.query(merchant.MerchantTimings).filter(merchant.MerchantTimings.uuid == merchant_uuid).first()
            
            merchants = db.session.query(merchant.MerchantTimings).first()

            timings = {}
            timings['uuid'] = merchants.uuid
            # for prop in props:

            if merchants.saturday_start:
                timings['saturday_start'] = merchants.saturday_start.strftime("%I:%M%p")

            if merchants.saturday_end:
                timings['saturday_end'] = merchants.saturday_end.strftime("%I:%M%p")

            if merchants.sunday_start:
                timings['sunday_start'] = merchants.sunday_start.strftime("%I:%M%p")
            
            if merchants.sunday_end:
                timings['sunday_end'] = merchants.sunday_end.strftime("%I:%M%p")

            if merchants.monday_start:
                timings['monday_start'] = merchants.monday_start.strftime("%I:%M%p")

            if merchants.monday_end:
                timings['monday_end'] = merchants.monday_end.strftime("%I:%M%p")

            if tuesday_start:
                timings['tuesday_start'] = merchants.tuesday_start.strftime("%I:%M%p")
            
            if merchants.tuesday_end:
                timings['tuesday_end'] = merchants.tuesday_end.strftime("%I:%M%p")

            if merchants.wednesday_start:
                timings['wednesday_start'] = merchants.wednesday_start.strftime("%I:%M%p")

            if merchants.wednesday_end:
                timings['wednesday_end'] = merchants.wednesday_end.strftime("%I:%M%p")

            if merchants.thursday_start:
                timings['thursday_start'] = merchants.thursday_start.strftime("%I:%M%p")
            
            if merchants.thursday_end:
                timings['thursday_end'] = merchants.thursday_end.strftime("%I:%M%p")

            if merchants.friday_start:
                timings['friday_start'] = merchants.friday_start.strftime("%I:%M%p")
            
            if merchants.friday_end:
                timings['friday_end'] = merchants.friday_end.strftime("%I:%M%p")            

            for prop in props:
                if prop not in timings:
                    timings[prop] = None
            return jsonify(timings), 200
        except Exception as e:
            print(e)
            # db.session.rollback()
            failed = True
            return jsonify(error=500, text=str(e)), 500

"""
curl -X GET \
  'http://localhost:5000/api/v1/merchants?merchant=Walmart' \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Postman-Token: a722ad08-fb4d-4b3e-a132-09fae34ffcfe,fb2d1bd4-088f-4411-a6f1-872947447c49' \
  -H 'Referer: http://localhost:5000/api/v1/merchants?merchant=Walmart' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F merchant=Walmart

Response:

[
  {
    "merchant_address_1": "105 N Busey Avenue",
    "merchant_address_2": "Apt 104",
    "merchant_address_city": "Urbana",
    "merchant_address_country": "USA",
    "merchant_address_state": "IL",
    "merchant_address_zipcode": "61801",
    "merchant_name": "Walmart",
    "merchant_primary_email": "moaaz123@gmail.com",
    "merchant_primary_phone": "6179094234",
    "merchant_uuid": "5a795a93-c851-44c4-9017-2c83234db208"
  },
  {
    "merchant_address_1": "105 N Busey Avenue",
    "merchant_address_2": "Apt 104",
    "merchant_address_city": "Urbana",
    "merchant_address_country": "USA",
    "merchant_address_state": "IL",
    "merchant_address_zipcode": "61801",
    "merchant_name": "Walmart",
    "merchant_primary_email": "moaaz1234@gmail.com",
    "merchant_primary_phone": "6179094234",
    "merchant_uuid": "35cfc9c6-8336-4b10-b239-7eb1bc11091f"
  },
  {
    "merchant_address_1": "306 E University",
    "merchant_address_2": "",
    "merchant_address_city": "Champaign",
    "merchant_address_country": "USA",
    "merchant_address_state": "IL",
    "merchant_address_zipcode": "61820",
    "merchant_name": "Walmart",
    "merchant_primary_email": "walmart@gmail.com",
    "merchant_primary_phone": "217200255",
    "merchant_uuid": "d1e896f1-17af-4694-9245-b4f29f5c13e7"
  }
]
"""

@app.route('/api/v1/merchants/', methods=['GET'])
def search_merchant():
    print("merchant arg:")
    merchant_query = request.args.get('merchant')
    
    print(merchant_query)
    # location_query = request.args.get('location')

    # merchants = db.session.query(merchant.Merchant).filter(merchant.Merchant.name.match(merchant_query)).all()
    merchants = db.session.query(merchant.Merchant).filter(merchant.Merchant.name == (merchant_query)).all()
    
    merchants_list = []

    for m in merchants:
        merchants_list.append({
            'merchant_uuid': m.uuid,
            'merchant_name': m.name,
            'merchant_address_1': m.address_1,
            'merchant_address_2': m.address_2,
            'merchant_address_city': m.address_city,
            'merchant_address_state': m.address_state,
            'merchant_address_zipcode': m.address_zipcode,
            'merchant_address_country': m.address_country,
            'merchant_primary_email': m.primary_email,
            'merchant_primary_phone': m.primary_phone 
        })


    # print(merchants)
    return jsonify(merchants_list), 200


    pass

"""
curl -X POST \
  http://localhost:5000/api/v1/counter/merchant/700769e9-5a1d-4941-b24f-cf15fde640c7/register \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 361' \
  -H 'Content-Type: multipart/form-data; boundary=--------------------------494335754056866360044188' \
  -H 'Host: localhost:5000' \
  -H 'Postman-Token: 3619be59-9dfb-4614-80b2-2753f5474226,c20b4f1e-0c34-4eff-9d2c-8298894da480' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F access_id=gkqmvtrvifrkgffihlpoyttm \
  -F access_key=oqrephadtijpeofyvdakuascnsczhgubsbserngsbawypmfuhrcauouuoffjsfaz

Reponse:
{
  "counter_identifier": null,
  "counter_sequence": 0,
  "counter_uuid": "2b210baf-d29d-4293-948d-cb1cb50572cd",
  "merchant_uuid": "700769e9-5a1d-4941-b24f-cf15fde640c7"
}
"""
@app.route('/api/v1/counter/merchant/<merchant_uuid>/register', methods=['POST'])
def register_merchant_counter(merchant_uuid):

    # make sure we have access_id and access_key so that no unauthorized addition of counters
    # is possible
    if not (request.form.get('access_id') and request.form.get('access_key')):
        return jsonify("Unauthorized Access"), 401
    
    # create counter uuid
    counter_uuid = str(uuid.uuid4())


    merch_counter = merchant.MerchantCounter(counter_uuid=counter_uuid, merchant_uuid=merchant_uuid, counter_identifier=None, counter_sequence=None)

    db.session.add(merch_counter)
    try:
        db.session.commit()
        failed = False
    except Exception as e:
        print(e)
        db.session.rollback()
        failed = True
        return jsonify(error=500, text=str(e)), 500

    if not failed:
        return jsonify({
            'counter_uuid': counter_uuid,
            'merchant_uuid': merchant_uuid,
            'counter_identifier': None,
            'counter_sequence': 0,
        }), 200

@app.route('/api/v1/counter/merchant/<merchant_uuid>/<counter_uuid>/updateSequence', methods=['PUT'])
def update_sequence(merchant_uuid, counter_uuid):
    
    merchant_auth = request.cookies.get('merchant_auth')
    if not merchant_auth:
        return jsonify("Unauthorized Access"), 401
    
    # TODO: Confirm that the merchant_uuid and merchant_auth are for the same merchants

    # Get current sequence # FIXIT: Currently assumes just one counter per merchant. For > 1 counters, get max sequence then increment it.
    current_counter = db.session.query(merchant.MerchantCounter).filter(merchant.MerchantCounter.merchant_uuid == merchant_uuid and merchant.MerchantCounter.counter_uuid == counter_uuid).first()
    db.session.query(merchant.MerchantCounter).filter(merchant.MerchantCounter.merchant_uuid == merchant_uuid and merchant.MerchantCounter.counter_uuid == counter_uuid).update({'counter_sequence': current_counter.counter_sequence + 1})

    try:
        db.session.commit()
        failed = False
    except Exception as e:
        print(e)
        db.session.rollback()
        failed = True
        return jsonify(error=500, text=str(e)), 500

    if not failed:
        current_counter = db.session.query(merchant.MerchantCounter).filter(merchant.MerchantCounter.merchant_uuid == merchant_uuid and merchant.MerchantCounter.counter_uuid == counter_uuid).first()
        result = {
            'new_sequence': current_counter.counter_sequence
        }
        return jsonify(result), 200


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
