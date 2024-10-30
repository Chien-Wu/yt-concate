import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

DOWNLOADS_DIR = 'downloads'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
OUTPUTS_DIR = 'outputs'

VIDEOS_DOWNLOAD_LIMIT = 20
SEARCH_WORD = 'hiho～大家好，我是志祺！'
CHANNEL_ID = "UCiWXd0nmBjlKROwzMyPV-Nw"

