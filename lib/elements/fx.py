from lib.elements.sample import Sample

class FX(Sample):
    def __init__(self, bpm, wav):
        super().__init__(wav)
        self.bpm = bpm
        