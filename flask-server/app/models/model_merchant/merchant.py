from app import db
from datetime import datetime

# class Guest(db.Model):
#     """Simple database model to track event attendees."""

#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80))
#     email = db.Column(db.String(120))

#     def __init__(self, name=None, email=None):
#         self.name = name
#         self.email = email

class Merchant(db.Model):
    """Simple database model to track event attendees."""

    __tablename__ = 'merchants'

    """
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
    """

    # id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String, primary_key=True, nullable=False)

    name = db.Column(db.String(40), nullable=False)
    address_1 = db.Column(db.String(40), nullable=False)
    address_2 = db.Column(db.String(40), nullable=True)
    address_city = db.Column(db.String(10), nullable=False)
    address_state = db.Column(db.String(10), nullable=True)
    # address_zipcode = db.Column(db.Integer(10), nullable=False)
    # address_country = db.Column(db.String(20), nullable=False)
    address_zipcode = db.Column(db.String(10), nullable=False)
    address_country = db.Column(db.String(), nullable=False)

    primary_email = db.Column(db.String(40), nullable=False)
    # primary_phone = db.Column(db.Integer(20), nullable=False)
    primary_phone = db.Column(db.Integer(), nullable=False)

    auth_code = db.Column(db.String(16), nullable=False)
    access_id = db.Column(db.String(24), nullable=False)
    access_key = db.Column(db.String(32), nullable=False)

    # lname = db.Column(db.String(25), nullable=False)
    # email = db.Column(db.String(50), nullable=False, unique=True)
    # phone_number = db.Column(db.String(20), nullable=False, unique=True)
    # username = db.Column(db.String(15), nullable=False, unique=True)
    # pwd = db.Column(db.String(50),  nullable=False)

    def __init__(self, uuid=None, name=None, address_1=None, address_2=None, address_city=None, address_state=None, address_zipcode=None, address_country=None, primary_email=None, primary_phone=None, auth_code=None, access_id=None, access_key=None):
        self.uuid = uuid
        self.name = name
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_city = address_city
        self.address_state = address_state
        self.address_zipcode = address_zipcode
        self.address_country = address_country
        self.primary_email = primary_email
        self.primary_phone = primary_phone
        self.auth_code = auth_code
        self.access_id = access_id
        self.access_key = access_key

class MerchantTimings(db.Model):
    """Database model for merchant timings"""

    __tablename__ = 'merchants_timings'

    uuid = db.Column(db.String, db.ForeignKey('merchants.uuid') , primary_key=True, nullable=False)
    
    saturday_start = db.Column(db.Time)
    saturday_end = db.Column(db.Time)

    sunday_start = db.Column(db.Time)
    sunday_end = db.Column(db.Time)

    monday_start = db.Column(db.Time)
    monday_end = db.Column(db.Time)

    tuesday_start = db.Column(db.Time)
    tuesday_end = db.Column(db.Time)

    wednesday_start = db.Column(db.Time)
    wednesday_end = db.Column(db.Time)

    thursday_start = db.Column(db.Time)
    thursday_end = db.Column(db.Time)

    friday_start = db.Column(db.Time)
    friday_end = db.Column(db.Time)

    def __init__(self, uuid, saturday_start=None, saturday_end=None, sunday_start=None, sunday_end=None, monday_start=None, monday_end=None, tuesday_start=None, tuesday_end=None, wednesday_start=None, wednesday_end=None, thursday_start=None, thursday_end=None, friday_start=None, friday_end=None):
        self.uuid = uuid
        self.saturday_start = saturday_start
        self.saturday_end = saturday_end
        self.sunday_start = sunday_start
        self.sunday_end = sunday_end
        self.monday_start = monday_start
        self.monday_end = monday_end
        self.tuesday_start = tuesday_start
        self.tuesday_end = tuesday_end
        self.wednesday_start = wednesday_start
        self.wednesday_end = wednesday_end
        self.thursday_start = thursday_start
        self.thursday_end = thursday_end
        self.friday_start = friday_start
        self.friday_end = friday_end
    

class MerchantCounter(db.Model):
    """Simple database model to track merchant counters."""

    __tablename__ = 'merchants_counters'

    counter_uuid = db.Column(db.String(), primary_key=True, nullable=False)
    merchant_uuid = db.Column(db.String(), db.ForeignKey('merchants.uuid'), nullable=False)

    counter_identifier = db.Column(db.String())
    counter_sequence = db.Column(db.Integer(), nullable=False, default=0)

    def __init__(self, counter_uuid=None, merchant_uuid=None, counter_identifier=None, counter_sequence=None):
        self.counter_uuid = counter_uuid
        self.merchant_uuid = merchant_uuid
        self.counter_identifier = counter_identifier
        self.counter_sequence = counter_sequence