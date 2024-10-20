import yt_dlp
import time
from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import CAPTIONS_DIR


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            if utils.caption_file_exist(url):
                continue
            try:
                self.download_subtitles(url, utils)
            except Exception as e:
                print(e)
        end = time.time()
        print('took', end-start, 'seconds')

    def download_subtitles(self, video_url, utils):
        outtmpl = utils.get_caption_output_path(video_url)
        ydl_opts = self.get_ydl_opts(outtmpl)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            if not self.check_caption_available(info_dict):
                print(f"No subtitles available for {video_url}")
                return

            ydl.download([video_url])
            print(f"Subtitles downloaded for {video_url} and saved to {CAPTIONS_DIR}")


    def get_ydl_opts(self, outtmpl):
        return  {
            'skip_download': True,  # Skip video download, only download subtitles
            'subtitlesformat': 'vtt',  # Use vtt subtitle format
            'writesubtitles': True,  # Download subtitles
            'subtitleslangs': ['zh-TW'],  # Language for English and auto-generated English subtitles
            'outtmpl': outtmpl,  # File naming format using video ID
            'subtitlesformat': 'best'  # Select the best available subtitles
        }

    def check_caption_available(self, info_dict):
        subtitles = info_dict.get('subtitles', {})
        return any('zh' in lang for lang in subtitles)

