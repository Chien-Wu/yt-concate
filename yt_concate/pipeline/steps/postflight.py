from yt_concate.pipeline.steps.step import Step

class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Post flight')
        pass