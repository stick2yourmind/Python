import sys
sys.path.append('..')
from observer.observable import Observable

class Weather(Observable):
    def __init__(self, name):
        Observable.__init__(self, name)
