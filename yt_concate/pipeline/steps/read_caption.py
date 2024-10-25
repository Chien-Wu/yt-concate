import os
from pprint import pprint
from .step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}

        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                record_next_line = False
                time = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        record_next_line = True
                        time = line
                        continue
                    if record_next_line:
                        captions[line] = time.split(' --> ')
                        record_next_line = False

            data[caption_file] = captions
        pprint(data)
        return data











