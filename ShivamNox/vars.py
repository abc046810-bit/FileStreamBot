# (c) Smarty MS
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '38498066'))  #Required
    API_HASH = str(getenv('API_HASH', 'c9696114751feacdeb1b4487f5839a1a')) #Required
    BOT_TOKEN = str(getenv('BOT_TOKEN', '8767304208:AAEcVsNkRi1UB68BqrVy3iz8hmi9RIms17U')) #Required
    name = str(getenv('name', 'FileStreamBot')) #Optional
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60')) #Leave as it is.
    WORKERS = int(getenv('WORKERS', '4')) #Leave as it is.
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1004376324695')) #Required
    PORT = int(getenv('PORT', '8000')) #Leave as it is.
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0')) #Leave as it is.
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "120"))  # 02 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "8909902924").split())  #Required
    NO_PORT = bool(getenv('NO_PORT', False)) #Leave as it is.
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'SmartBoy_ApnaMS')) #Required
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #Your app name or Leave as it is.
    else:
        ON_HEROKU = False
        
    FQDN = str(getenv('FQDN', 'filestreambot-pro-waiu.onrender.com')) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL = getenv('HAS_SSL', 'True').lower() == 'true'
    
    # URL from ENV or Default based on SSL (same pattern as other variables)
    if HAS_SSL:
        URL = str(getenv('SERVER_URL', "https://{}/".format(FQDN)))
    else:
        URL = str(getenv('SERVER_URL', "http://{}/".format(FQDN)))
    
    # Ensure URL ends with /
    if not URL.endswith('/'):
        URL = URL + '/'
        
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://developerbro723_db_user:9axC7c7iQm0G3ESO@cluster0.dr8m75m.mongodb.net/?appName=Cluster0')) #Required
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'TeamCinderella')) #Required without @
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) #Leave as it is.
