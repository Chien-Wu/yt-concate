import yt_dlp
from .step import Step
from yt_concate.settings import VIDEOS_DIR

class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        # 設定影片下載的目標資料夾
        output_path = f'./{VIDEOS_DIR}/%(id)s.%(ext)s'  # 可將 './videos/' 換成你想要的路徑

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # 指定下載 mp4 格式，優先合併最佳畫質與音質
            'merge_output_format': 'mp4',  # 若下載後需要合併，則儲存為 mp4 格式
            'outtmpl': output_path,  # 設定下載的檔案名稱及儲存路徑
            'quiet': True,  # 禁用所有輸出
        }

        print(len(data))
        yt_set = set([found.yt for found in data])
        print(f'{len(yt_set)} videos to download')


        for yt in yt_set:
            url = yt.url

            if utils.video_file_exists(yt):
                print(f'found existing video for {url}')
                continue

            print(f'Downloading {url}')
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

            except yt_dlp.utils.DownloadError as e:
                print(f"Video download failed: {url}, error message: {e}")

        return data

