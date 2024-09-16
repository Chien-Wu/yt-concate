from .steps.step import StepException

class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        d = None
        for step in self.steps:
            try:
                d = step.process(d, inputs)
            except StepException as e:
                print("Exception happened: ", e)
                break