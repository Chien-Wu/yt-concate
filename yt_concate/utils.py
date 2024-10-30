import os

from yt_concate.settings import DOWNLOADS_DIR, CAPTIONS_DIR, VIDEOS_DIR, OUTPUTS_DIR


class Utils:
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(OUTPUTS_DIR, exist_ok=True)

    def caption_file_exists(self, yt):
        filepath = yt.caption_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def video_file_exists(self, yt):
        filepath = yt.video_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0


    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exist(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_output_filepath(self, channel_id, search_word):
        file_name = f'{channel_id}_{search_word}.mp4'
        return os.path.join(OUTPUTS_DIR, file_name)