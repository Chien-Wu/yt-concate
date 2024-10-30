from .step import Step

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue
            captions = {}
            with open(yt.caption_filepath, 'r') as f:
                record_next_line = False
                time = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        record_next_line = True
                        time = line
                        continue
                    if record_next_line:
                        captions[line] = time
                        record_next_line = False
            yt.captions = captions

        return data











