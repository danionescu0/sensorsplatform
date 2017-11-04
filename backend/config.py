rabbitmq_host = 'localhost'

mongodb_uri = 'mongodb://localhost:27017/'

redis = {
    'host': 'localhost',
    'port': 6379
}

web = {
    'jwt_secret': ''
}

logging = {
    'log_file': 'log2.txt',
    'log_entries': 20000000
}

email = {
    'email': '', # sender email
    'password': '', # sender password
    'notifiedAddress': '' # receiving email
}

telestax = {
    'voice_url' : 'https://cloud.restcomm.com:443/restcomm-rvd/services/apps/api_token/start',
    'token' : '',
    'from_number' : '12345'
}