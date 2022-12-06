import os
from dotenv import load_dotenv

load_dotenv()

PROJECTS_ID = {
    'api_gw': 190,
    'consumer_bus': 205,
    'hs_fe': 253,
    'isz_be': 173,
    'isz_fe': 174,
    'market_be': 235,
    'payment_be': 240,
    'passport_be': 170,
    'passport_fe': 169,
    'schedule_be': 269
}

FORMAT_DATE_FROM = '%Y-%m-%dT%H:%M:%S.%f%z'
FORMAT_DATE_TO = '%d.%m.%Y %H:%M:%S'

# Token gitlab. Получить: URL_GITLAB/-/profile/personal_access_tokens
TOKEN = {
    "PRIVATE-TOKEN": os.getenv('GITLAB_TOKEN')
}

URL_GITLAB = os.getenv('HOST_GITLAB')
