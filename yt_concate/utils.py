import os

from yt_concate.settings import DOWNLOADS_DIR, CAPTIONS_DIR, VIDEOS_DIR

class Utils:
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    def get_caption_output_path(self, url):
        return os.path.join(CAPTIONS_DIR, '%(id)s.%(ext)s')

    @staticmethod
    def get_caption_id_from_url(url):
        return url.split('watch?v=')[-1]

    def caption_file_exist(self, url):
        path = self.get_caption_output_path(url)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exist(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0




