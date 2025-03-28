import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN","7557612085:AAFs9uRaD8C0nZr4kBFM1ST30MzsWpKEZyA")
    API_ID = int(os.environ.get("API_ID","26468828"))
    API_HASH = os.environ.get("API_HASH","4693513c08d1ac6af15f95b116c29478")
    VIP_USER = os.environ.get('VIP_USERS', '7517045929').split(',')
    VIP_USERS = [int(7517045929) for user_id in VIP_USER]
