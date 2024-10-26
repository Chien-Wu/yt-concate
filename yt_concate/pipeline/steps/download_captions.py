import yt_dlp
import time

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import CAPTIONS_DIR


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:
            if utils.caption_file_exist(yt):
                print(f'Use Existing caption file for {yt.url}')
                continue
            try:
                self.download_subtitles(yt, utils)
            except Exception as e:
                print(e)
        end = time.time()
        print('Downloading captions took', end-start, 'seconds')
        return data

    def download_subtitles(self, yt, utils):
        outtmpl = yt.caption_filepath
        ydl_opts = self.get_ydl_opts(outtmpl)
        video_url = yt.url

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            if not self.check_caption_available(info_dict):
                print(f"No subtitles available for {video_url}")
                return

            print(f"Download caption for {video_url}")
            ydl.download([video_url])


    def get_ydl_opts(self, outtmpl):
        return {
            'skip_download': True,  # Skip video download, only download subtitles
            'subtitlesformat': 'vtt',  # Use vtt subtitle format
            'writesubtitles': True,  # Download subtitles
            'subtitleslangs': ['zh-TW'],  # Language for Chinese Traditional subtitles
            'outtmpl': outtmpl,  # File naming format using video ID
            'subtitlesformat': 'best',  # Select the best available subtitles
            'quiet': True,  # Suppress output
            'no_warnings': True,  # Suppress warnings
        }

    def check_caption_available(self, info_dict):
        subtitles = info_dict.get('subtitles', {})
        return any('zh' in lang for lang in subtitles)

